#!/usr/bin/env python
#-----------------------------------------------------------------
# jsoncc: runtime.py
#
# json en/decoding related C code templates and code generator
#
# Copyright (C) 2014, wvi
# License: BSD
#-----------------------------------------------------------------
import sys
import logging
import os
import copy
from pycparser import c_parser, c_generator
from pycparser.c_ast import *
from templates import *

sys.path.extend(['.', '..'])

std = "typedef int size_t;typedef int jsn_error_t;typedef int jsn_buf_t;\n"

class JsonCCGen(object):
    
    def __init__(self):
        self._parser = c_parser.CParser(lex_optimize=True, 
                                  lextab='jsoncc.lextab', 
                                  yacc_optimize=True, 
                                  yacctab='jsoncc.yacctab', 
                                  yacc_debug=False)

        self._asts = {'strdup': self.parse(strdup), 
                      'realloc': self.parse(realloc), 
                      'get_int': self.parse(get_int), 
                      'get_double': self.parse(get_double),
                      'get_str': self.parse(get_str),
                      'get_str_array': self.parse(get_str_array),
                      'get_array': self.parse(get_array),
                      'decode_func': self.parse(decode_func),
                      'encode_func': self.parse(encode_func),
                      'free_func': self.parse(free_func),
                      'free_item': self.parse(free_item),
                      'free_str_arr': self.parse(free_str_arr),
                      'find_opt_token': self.parse(find_opt_token),
                      'find_token': self.parse(find_token),
                      'emit_key': self.parse(emit_key),
                      'emit_quoted': self.parse(emit_quoted),
                      'emit_number': self.parse(emit_number),
                      'emit_bool': self.parse(emit_bool),
                      'emit_str': self.parse(emit_str),
                      'emit_optional': self.parse(emit_optional),
                  }

        self._type_fmt_map = {"unsigned int": "%u", 
                              "unsigned short int": "%hu",
                              "int": "%d",
                              "short int": "%hd",
                              "unsigned long": "%lu",
                              "long": "%ld", 
                              "float": "%f", 
                              "double": "%lf",
                          }
        
    def create(self, src_file, out_file, alloc_blk=512):
        self._out_file = out_file
        self._src_file = src_file
        self.name_h = ".".join((out_file, "h"))
        self.name_c = ".".join((out_file, "c"))
        self._funcset = set()

        self.define = self.name_h.upper().replace('.', '_') + '_'
        header_guard = "#ifndef %s \n#define %s 1"%(self.define, self.define)

        self.hAST = FileAST([Any(header_guard),
                             Any(warning_comment%(src_file)),
                             Any('#include "%s"\n'%(src_file)),
                             Any('#ifdef __cplusplus\nextern "C" {\n#endif\n'),
                         ])
        self.h = self.hAST.ext

        self.cAST = FileAST([Any(warning_comment%(src_file)),
                             Any(file_prelude),
                             Any('#include "%s"\n'%(self.name_h)),
                             Any("#define JSN_ALLOC_CHUNK %d\n"%(alloc_blk)),
                         ])

        self.c = self.cAST.ext
        self._utilFunDefs = {}

        fh_parse = self.parse(file_h_prelude)
        self.h.append(fh_parse)

    def parse(self, code, debuglvl=0):
        return self._parser.parse("\n".join((std, code)), debuglevel=debuglvl).ext[3]

    def done(self):
        self.h.append(Any("\n#ifdef __cplusplus\n}\n#endif"))
        self.h.append(Any("#endif /* #ifndef %s */" %(self.define)))

    def genC(self):
        generator = c_generator.CGenerator()
        return generator.visit(self.cAST)

    def genH(self):
        generator = c_generator.CGenerator()
        return generator.visit(self.hAST)

    def dump_Asts(self):
        for a in self._asts.values():
            a.show()

    def _addFuncDecl(self, name, op='decode', free=False):
        nm = name[:-2] if name.endswith("_t") else name
        
        if op == 'decode':
            freefunc = None
            declname = "jsn_decode_%s" %(nm)
            funcdef = copy.deepcopy(self._asts['decode_func'])
            funcdef.decl.name = declname
            funcdef.decl.type.type.declname = declname
            funcdef.decl.type.args.params[0].type.type.type.names[0] = name
            self.h.append(funcdef.decl)
            if free:
                freefunc = copy.deepcopy(self._asts['free_func'])
                freefunc.decl.name = "jsn_free_%s" %(nm)
                freefunc.decl.type.type.declname = "jsn_free_%s" %(nm)
                freefunc.decl.type.args.params[0].type.type.type.names[0] = name
                self.h.append(freefunc.decl)

        elif op == 'encode':
            freefunc = None
            declname = "jsn_encode_%s" %(nm)
            funcdef = copy.deepcopy(self._asts['encode_func'])
            funcdef.decl.name = declname
            funcdef.decl.type.type.declname = declname
            funcdef.decl.type.args.params[0].type.type.type.names[0] = name
            self.h.append(funcdef.decl)

        else:
            raise RuntimeError("Unsupported operation %s" %(op))

        return funcdef, freefunc
        

    def _addUtilFunc(self, name, func):
        self._funcset.add(name)
        self.c.append(func)
        self._utilFunDefs[name] = func


    def _getUtilFunc(self, name):
        if name in self._utilFunDefs.keys():
            return self._utilFunDefs[name]
        else:
            return None

    
    def _newUtilFunc(self, func_name, td):
        if func_name not in self._funcset:
            t = " ".join(td.type.names)
            fmt_str = self._type_fmt_map[t];
            i = 1
            if 'double' in td.type.names or 'float' in td.type.names:
                func = copy.deepcopy(self._asts['get_double'])
                i = 0
            else:
                func = copy.deepcopy(self._asts['get_int'])

            func.body.block_items[0].iftrue.block_items[i].args.exprs[1].value \
            = '"'+ fmt_str + '"'
            func.decl.name = func_name
            func.decl.type.type.declname = func_name
            func.decl.type.args.params[1].type.type.type.names = td.type.names
            self._addUtilFunc(func_name, func)
            return func
        else:
            return self._getUtilFunc(func_name)


    def _tok_fncall(self, json):
        if 'optional' in json:
            tok = copy.deepcopy(self._asts['find_opt_token'].body) 
            fncall = tok.block_items[1].iftrue.block_items[0].cond.expr.right.rvalue
        else:
            tok = copy.deepcopy(self._asts['find_token'].body)
            fncall = tok.block_items[2].cond.expr.right.rvalue

        return tok, fncall


    def _decodeTypeDecl(self, func, td, json):
        assert(isinstance(td, TypeDecl))
        func_name = 'get_%s' %(''.join(td.type.names))
        get_func = self._newUtilFunc(func_name, td)

        tok, fncall = self._tok_fncall(json)
        tok.block_items[0].rvalue.args.exprs[1].value = '"' + json[0] + '"'
        fncall.name.name = get_func.decl.name
        fncall.args = ExprList([])
        fncall.args.exprs.append(ID('tok'))
        fncall.args.exprs.append(UnaryOp('&', StructRef(ID('s'), '->', ID(td.declname))))

        func.body.block_items += tok.block_items


    def _decodePtrPtrDecl(self, func, pd, json):
        if 'char' not in pd.type.type.names:
            t = " ".join(pd.type.type.names)
            raise RuntimeError("%s is not supported decoding type" % t)

        if 'get_str_array' not in self._funcset:

            if 'get_str' not in self._funcset:
                self.c.append(self._asts['strdup'])
                self._addUtilFunc('get_str', self._asts['get_str'])

            get_func = self._asts['get_str_array']
            self._addUtilFunc('get_str_array', get_func)
            
        tok, fncall = self._tok_fncall(json)
        tok.block_items[0].rvalue.args.exprs[1].value = '"' + json[0] + '"'
        fncall.name.name = get_func.decl.name
        fncall.args = ExprList([])
        fncall.args.exprs.append(ID('arr'))
        fncall.args.exprs.append(ID('(tok - arr)'))
        fncall.args.exprs.append(UnaryOp('&', StructRef(ID('s'), '->', ID(pd.type.declname))))
        func.body.block_items += tok.block_items


    def _decodeCStr(self, declname, json):
        if 'get_str' not in self._funcset:
            self.c.append(self._asts['strdup'])
            get_func = self._asts['get_str']
            self._addUtilFunc('get_str', get_func)
        else:
            get_func = self._getUtilFunc('get_str')
        
        tok, fncall = self._tok_fncall(json)
        tok.block_items[0].rvalue.args.exprs[1].value = '"' + json[0] + '"'
        fncall.name.name = get_func.decl.name
        fncall.args = ExprList([])
        fncall.args.exprs.append(ID('tok'))
        fncall.args.exprs.append(UnaryOp('&', StructRef(ID('s'), '->', ID(declname))))
        return tok


    def _decodePtrDecl(self, func, pd, json):
        assert(isinstance(pd, PtrDecl))

        if (isinstance(pd.type, PtrDecl)):
           self. _decodePtrPtrDecl(func, pd.type, json)
           return

        if 'char' in pd.type.type.names:
            tok = self._decodeCStr(pd.type.declname, json)
            func.body.block_items += tok.block_items
        else:
            func_name = 'get_array_%s' %(''.join(pd.type.type.names))
            if func_name not in self._funcset:
                t = " ".join(pd.type.type.names)   
                get_func = copy.deepcopy(self._asts['get_array'])
                decl = get_func.decl
                body = get_func.body.block_items
                cast = body[3].iftrue.block_items[0].rvalue.to_type
                fncall = body[3].iftrue.block_items[4].stmt.block_items[0].cond.right.rvalue
                decl.name = func_name
                decl.type.type.declname = func_name
                decl.type.args.params[1].type.type.names = pd.type.type.names
                body[2].type.type.type.names = pd.type.type.names
                cast.type.type.type.names =  pd.type.type.names
                fncall.name.name = 'get_%s' %t
                if fncall.name.name not in self._funcset:
                    self._newUtilFunc(fncall.name.name, pd.type)
                self._addUtilFunc(func_name, get_func)
            else:
                get_func = self._getUtilFunc(func_name)

            tok, fncall = self._tok_fncall(json)
            tok.block_items[0].rvalue.args.exprs[1].value = '"' + json[0] + '"'
            fncall.name.name = get_func.decl.name
            fncall.args = ExprList([])
            fncall.args.exprs.append(ID('arr'))
            fncall.args.exprs.append(ID('(tok - arr)'))
            fncall.args.exprs.append(UnaryOp('&', StructRef(ID('s'), '->', ID(pd.type.declname))))
            fncall.args.exprs.append(UnaryOp('&', StructRef(ID('s'), '->', ID(pd.type.declname + '_count_'))))

            func.body.block_items += tok.block_items


    def decodeTypedefStruct(self, name, s, options=[]):
        assert(isinstance(s, Struct))
        free = True if 'free' in options else False
        fundef, freefunc = self._addFuncDecl(name, free=free)
        for d in s.decls:
            if d.json == []:
                continue

            if isinstance(d.type, TypeDecl):
                self._decodeTypeDecl(fundef, d.type, d.json)
            elif isinstance(d.type, PtrDecl):
                self._decodePtrDecl(fundef, d.type, d.json)
            else:
                raise RuntimeError("%s not supported in decoding." % str(d.type))

        fundef.body.block_items.append(Label("end", FuncCall(ID("free"), ExprList([ID("arr")]))))
        fundef.body.block_items.append(Return(ID("status")))
        
        self.c.append(fundef)

        if free:
            frbody = freefunc.body.block_items[0].iftrue
            frbody.block_items = []
            for d in s.decls:
                if d.json == []:
                    continue
                if isinstance(d.type, PtrDecl):
                    if isinstance(d.type.type, PtrDecl):
                        ff = copy.deepcopy(self._asts['free_str_arr'].body.block_items[0])
                        ff.cond.field.name =  d.type.type.type.declname
                        ff.iftrue.block_items[0].init.field.name = d.type.type.type.declname
                        ff.iftrue.block_items[2].args.exprs[0].field.name = d.type.type.type.declname
                    else:
                        ff = copy.deepcopy(self._asts['free_item'].body.block_items[0])
                        ff.cond.field.name = d.type.type.declname
                        ff.iftrue.args.exprs[0].field.name = d.type.type.declname

                    frbody.block_items.append(ff)

            self.c.append(freefunc)


    def _encodeTypeDecl(self, func, td, json, array=False):
        assert(isinstance(td, TypeDecl))

        if not array:
            key = copy.deepcopy(self._asts['emit_key'].body)
            key.block_items[0].rvalue.args.exprs[2].value = '"\\"%s\\":"' %(td.declname)
            key.block_items[1].iftrue.block_items[1].rvalue.args.exprs[2].value = '"\\"%s\\":"' %(td.declname)
            func.append(key)
        
        if 'boolean' in json:
            val = copy.deepcopy(self._asts['emit_bool'].body)
            val.block_items[0].rvalue.cond.field.name = td.declname
            val.block_items[1].iftrue.block_items[1].rvalue.cond.field.name = td.declname
        else:
            val = copy.deepcopy(self._asts['emit_number'].body)
            fmt_str = self._type_fmt_map[" ".join(td.type.names)]  
            val.block_items[0].rvalue.args.exprs[2].value = '"%s,"' % fmt_str
            val.block_items[0].rvalue.args.exprs[3].field.name = td.declname
            val.block_items[1].iftrue.block_items[1].rvalue.args.exprs[2].value = '"%s,"' % fmt_str
            val.block_items[1].iftrue.block_items[1].rvalue.args.exprs[3].field.name = td.declname

        func.append(val)


    def _encodePtrPtrDecl(self, func, pd, json, array=False):
        if 'char' not in pd.type.type.names:
            t = " ".join(pd.type.type.names)
            raise RuntimeError("%s is not supported encoding type" % t)
        else:
            t = " ".join(pd.type.type.names)
            raise RuntimeError("%s is not supported encoding type" % t)


    def _encodePtrDecl(self, func, pd, json, array=False):
        assert(isinstance(pd, PtrDecl))
        if (isinstance(pd.type, PtrDecl)):
            self. _encodePtrPtrDecl(func, pd.type, json, array)
            return

        if 'char' not in pd.type.type.names:
            t = " ".join(pd.type.type.names)
            raise RuntimeError("%s is not supported encoding type" % t)

        if not array:
            key = copy.deepcopy(self._asts['emit_key'].body)
            key.block_items[0].rvalue.args.exprs[2].value = '"\\"%s\\":" ' %(pd.type.declname)
            key.block_items[1].iftrue.block_items[1].rvalue.args.exprs[2].value = '"\\"%s\\":"' %(pd.type.declname)
            func.append(key)
        
        if 'json' in json:
            val = copy.deepcopy(self._asts['emit_str'].body)
            val.block_items[0].rvalue.args.exprs[3].field.name = pd.type.declname
            val.block_items[1].iftrue.block_items[1].rvalue.args.exprs[3].field.name = pd.type.declname
        else:
            val = copy.deepcopy(self._asts['emit_quoted'].body)
            val.block_items[0].rvalue.args.exprs[3].field.name = pd.type.declname
            val.block_items[1].iftrue.block_items[1].rvalue.args.exprs[3].field.name = pd.type.declname

        if 'optional' in json:
            optval = copy.deepcopy(self._asts['emit_optional'].body)
            optval.block_items[0].cond.field.name = pd.type.declname
            optval.block_items[0].iftrue.block_items = val.block_items
            func.append(optval)
        else:
            func.append(val)

            
    def encodeTypedefStruct(self, name, s, options=[]):
        array = True if 'array' in options else False

        if 'realloc' not in self._funcset:
            self._addUtilFunc('realloc', self._asts['realloc'])
        fundef, freefunc = self._addFuncDecl(name, op='encode')
        body = fundef.body.block_items[6]
        body.block_items = []

        if array :
            fundef.body.block_items[5].rvalue.value = "'['"

        for d in s.decls:
            if isinstance(d.type, TypeDecl):
                self._encodeTypeDecl(body.block_items, d.type, d.json, array)
            elif isinstance(d.type, PtrDecl):
                self._encodePtrDecl(body.block_items, d.type, d.json, array)
            else:
                raise RuntimeError("%s not supported in encoding." % str(d.type))
        
        if array:
            fundef.body.block_items[-4].rvalue.value = "']'"

        self.c.append(fundef)


def main():
    from pycparser.plyparser  import ParseError

    # parser = c_parser.CParser()
    # try:
    #     ast = parser.parse(get_int, filename="get_int", debuglevel=0)
    #     if ast is None:
    #         print("Parsing failed ...")
    #     else:
    #         ast.show()
    # except ParseError as e:
    #     print(e)

    run = JsonCCGen()
    run.create("some.h", "xxx")
    print(run.generateH())
    print(run.generateC())
    

if __name__ == '__main__':
    main()



