#!/usr/bin/env python
#-----------------------------------------------------------------
# jsoncc: jsoncc.py
#
# Main jsoncc module, code generator and parser
#
# Copyright (C) 2014, wvi
# License: BSD
#-----------------------------------------------------------------

__all__ = ['JsonCC', 'slurp_file']

import sys
import argparse
import logging
sys.path.extend(['.', '..'])
import os
from string import Template
from pycparser import c_parser, c_ast
from subprocess import Popen, PIPE
from jsngen import JsonCCGen

class JsonVisitor(c_ast.NodeVisitor):
    def __init__(self, generator):
        self.code = ""
        self.decls = ""
        self.gen = generator
        
    def visit_Json(self, node):
        t = node.decl
        s = t.type.type
        if isinstance(s, c_ast.Struct):
            if node.mode == 'decode' or node.mode == 'both':
                logging.debug("Generate decoding of struct %s typedef'd to %s"
                              % (s.name, t.name))
                self.gen.decodeTypedefStruct(t.name, s, node.flags)
            if node.mode == 'encode' or node.mode == 'both':
                logging.debug("Generate encoding of struct %s typedef'd to %s"
                              % (s.name, t.name))
                self.gen.encodeTypedefStruct(t.name, s, node.flags)
        else:
            raise RuntimeError(
                "Only structs are supported ATM no support for %s"
                %(s.name))

class JsonCC(object):
    """
    Main Jsoncc object 
    """
    def __init__(self, src, filename,  output=None, debug=False, parse_debug=0):
        """
        """
        self.code = src
        self.filename = filename
        self.parse_dbg_lvl = 5 if parse_debug else 0
        self.output = output
        self.debug = debug
        self.generator = JsonCCGen()
        self.generator.create(filename, output)


    def parse(self):
        """ Run the parser and get the AST"""
        if self.debug:
            print(self.code)

        logging.debug("Running the parser ...")
        parser = c_parser.CParser(lex_optimize=True, 
                                  lextab='lextab', 
                                  yacc_optimize=True, 
                                  yacctab='yacctab', 
                                  yacc_debug=False)

        self.ast = parser.parse(self.code, filename=self.filename, debuglevel=self.parse_dbg_lvl)
        if self.ast is None:
            logging.error("Parsing failed ...")
            raise RuntimeError("Parsing failed ...")

        if debug:
            self.ast.show()

    def gen(self):
        """ Generate the code!"""
        self.parse()
        logging.debug("Generate the C code")
        jv = JsonVisitor(self.generator)
        jv.visit(self.ast)
        self.generator.done()

        if self.debug:
            print(self.generator.genH())
            print(self.generator.genC())

        if self.output is not None:
            logging.debug("Writing the generated functions to %s.n and %s.c" %(self.output, self.output))
            hname = ".".join((self.output, "h"))
            cname = ".".join((self.output, "c"))
            with open(cname, "w") as f:
                f.write(self.generator.genC())
            logging.debug("Writing the generated function declarations to %s" % (hname))
            with open(hname, "w") as f:
                f.write(self.generator.genH())
        else:
            sys.stdout.write("/* function bodies */\n")
            sys.stdout.write(self.generator.genC())
            sys.stdout.write("/* function declarations */\n")
            sys.stdout.write(self.generator.genH())


def preprocess_file(filename, cpp_path='mcpp', cpp_args=''):
    """ Preprocess a file using mcpp.

        filename:
            Name of the file you want to preprocess.

        cpp_path:
        cpp_args:
            Refer to the documentation of parse_file for the meaning of these
            arguments.

        When successful, returns the preprocessed file's contents.
        Errors from mcpp will be printed out.
    """
    path_list = [cpp_path]
    if isinstance(cpp_args, list):
        path_list += cpp_args
    elif cpp_args != '':
        path_list += [cpp_args]
    path_list += [filename]

    try:
        # Note the use of universal_newlines to treat all newlines
        # as \n for Python's purpose
        #
        print(path_list)
        pipe = Popen(   path_list,
                        stdout=PIPE,
                        universal_newlines=True)
        text = pipe.communicate()[0]
        ret_code = pipe.returncode
    except OSError as e:
        raise RuntimeError("Unable to invoke 'mcpp'.  " +
            'Make sure its path was passed correctly\n' +
            ('Original error: %s' % e))
    
    if (ret_code != 0):
        text = ""
    return text


def slurp_file(filepath):
    text = ""
    with open(filepath) as f:
        text = f.read()
    
    return text


def main():
    """Main entry point for json c code generator """
    global debug

    usage = 'Usage: %prog [options]'
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input', metavar="FILE", help='Input file, default is stdin', 
                        nargs=1, default="") 
    parser.add_argument('-o', '--output', metavar="FILE", 
                        help='Output file, default is stdout. Appends .h and .c to given name', 
                        nargs=1, default=None)
    parser.add_argument('-p', '--preprocess', help='Run the preprocessor first.', 
                        action='store_true')
    parser.add_argument('-v', '--verbose', help='be verbose mode',
                        action='store_true', default=False)
    parser.add_argument('-d', '--debug', help='debug the generator',
                        action='store_true', default=False)
    parser.add_argument('-a', '--astdebug', help='debug parser',
                        action='store_true', default=False)
    args = parser.parse_args()

    debug = args.debug

    loglevel = "INFO"
    if args.verbose:
        loglevel = "DEBUG"

    logging.basicConfig(format='%(message)s', 
                        datefmt='%I:%M:%S', level=loglevel)

    if args.input != "":
        if args.preprocess:
            logging.debug("Preprocessing file %s" % args.input)
            logging.error("Preprocessing files not fully supported yet, if you need it modify \
            jsoncc.py to have correct -I, see commented out call to preprocess_file function in jsoncc.py:467")
            # code = preprocess_file(args.input, cpp_path="mcpp", 
            #                        cpp_args =['-@std', '-C','-P','-DGCLX_NATIVE',
            #                                   '-I utils/fake_libc_include/',
            #                                   '-I ','-I ../../gclx/gclx/include/',
            #                                   '-I ../../gclx/gclx/src/',
            #                                   '-I ../../gclx/gclp/include/',
            #                                   '-I ../../gclx/gcln/include/',
            #                                   '-I ../../gclx/external/libuv/include/'])
        else:
            logging.debug("Read file %s" % args.input[0])
            code = slurp_file(args.input[0])
        
        if code == "":
            logging.error("Failed to read or preprocess the source ...")
            sys.exit(1)

        jsoncc = JsonCC(src=code, filename=args.input[0], output=args.output[0], debug=debug, parse_debug=args.astdebug)
            
        jsoncc.gen()

    else:
        logging.error("Reading from stdin not implemented yet ...sorry")
        sys.exit(1)
        
if __name__ == '__main__':
    main()
