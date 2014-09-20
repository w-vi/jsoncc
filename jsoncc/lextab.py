# jsoncc.lextab.py. This file automatically created by PLY (version 3.4). Don't edit!
_tabversion   = '3.4'
_lextokens    = {'VOID': 1, 'LBRACKET': 1, 'WCHAR_CONST': 1, 'FLOAT_CONST': 1, 'MINUS': 1, 'RPAREN': 1, 'LONG': 1, 'PLUS': 1, 'ELLIPSIS': 1, 'GT': 1, 'GOTO': 1, 'ENUM': 1, 'PERIOD': 1, 'GE': 1, 'INT_CONST_DEC': 1, 'ARROW': 1, 'HEX_FLOAT_CONST': 1, 'DOUBLE': 1, 'MINUSEQUAL': 1, 'INT_CONST_OCT': 1, 'TIMESEQUAL': 1, 'OR': 1, 'SHORT': 1, 'RETURN': 1, 'RSHIFTEQUAL': 1, 'RESTRICT': 1, 'STATIC': 1, 'SIZEOF': 1, 'UNSIGNED': 1, 'UNION': 1, 'COLON': 1, 'WSTRING_LITERAL': 1, 'DIVIDE': 1, 'FOR': 1, 'PLUSPLUS': 1, 'EQUALS': 1, 'ELSE': 1, 'INLINE': 1, 'EQ': 1, 'AND': 1, 'TYPEID': 1, 'LBRACE': 1, 'PPHASH': 1, 'INT': 1, 'SIGNED': 1, 'CONTINUE': 1, 'JSON_COLON': 1, 'NOT': 1, 'OREQUAL': 1, 'MOD': 1, 'RSHIFT': 1, 'DEFAULT': 1, 'CHAR': 1, 'WHILE': 1, 'DIVEQUAL': 1, 'EXTERN': 1, 'CASE': 1, 'LAND': 1, 'REGISTER': 1, 'MODEQUAL': 1, 'NE': 1, 'SWITCH': 1, 'JSON_KEYWORD': 1, 'INT_CONST_HEX': 1, '_COMPLEX': 1, 'PLUSEQUAL': 1, 'JSON_MODE': 1, 'STRUCT': 1, 'CONDOP': 1, 'BREAK': 1, 'VOLATILE': 1, 'ANDEQUAL': 1, 'DO': 1, 'LNOT': 1, 'CONST': 1, 'LOR': 1, 'CHAR_CONST': 1, 'LSHIFT': 1, 'RBRACE': 1, '_BOOL': 1, 'LE': 1, 'SEMI': 1, 'LT': 1, 'COMMA': 1, 'TYPEDEF': 1, 'XOR': 1, 'AUTO': 1, 'TIMES': 1, 'LPAREN': 1, 'MINUSMINUS': 1, 'ID': 1, 'IF': 1, 'STRING_LITERAL': 1, 'FLOAT': 1, 'XOREQUAL': 1, 'LSHIFTEQUAL': 1, 'RBRACKET': 1}
_lexreflags   = 0
_lexliterals  = ''
_lexstateinfo = {'ppline': 'exclusive', 'pppragma': 'exclusive', 'INITIAL': 'inclusive', 'ppdirective': 'exclusive', 'ppjson': 'exclusive'}
_lexstatere   = {'ppline': [('(?P<t_ppline_FILENAME>"([^"\\\\\\n]|(\\\\(([a-zA-Z._~!=&\\^\\-\\\\?\'"])|(\\d+)|(x[0-9a-fA-F]+))))*")|(?P<t_ppline_LINE_NUMBER>(0(([uU]ll)|([uU]LL)|(ll[uU]?)|(LL[uU]?)|([uU][lL])|([lL][uU]?)|[uU])?)|([1-9][0-9]*(([uU]ll)|([uU]LL)|(ll[uU]?)|(LL[uU]?)|([uU][lL])|([lL][uU]?)|[uU])?))|(?P<t_ppline_NEWLINE>\\n)|(?P<t_ppline_PPLINE>line)', [None, ('t_ppline_FILENAME', 'FILENAME'), None, None, None, None, None, None, ('t_ppline_LINE_NUMBER', 'LINE_NUMBER'), None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, ('t_ppline_NEWLINE', 'NEWLINE'), ('t_ppline_PPLINE', 'PPLINE')])], 'pppragma': [('(?P<t_pppragma_NEWLINE>\\n)|(?P<t_pppragma_PPPRAGMA>pragma)|(?P<t_pppragma_STR>"([^"\\\\\\n]|(\\\\(([a-zA-Z._~!=&\\^\\-\\\\?\'"])|(\\d+)|(x[0-9a-fA-F]+))))*")|(?P<t_pppragma_ID>[a-zA-Z_$][0-9a-zA-Z_$]*)', [None, ('t_pppragma_NEWLINE', 'NEWLINE'), ('t_pppragma_PPPRAGMA', 'PPPRAGMA'), ('t_pppragma_STR', 'STR'), None, None, None, None, None, None, ('t_pppragma_ID', 'ID')])], 'INITIAL': [('(?P<t_PPHASH>[ \\t]*\\#)|(?P<t_JSON_START>[ \\t]*//\\+json:)|(?P<t_COMMENT>/\\*(.|\\n)*?\\*/)|(?P<t_SLASHCOMMENT>//.*\\n)|(?P<t_NEWLINE>\\n+)|(?P<t_LBRACE>\\{)|(?P<t_RBRACE>\\})|(?P<t_FLOAT_CONST>((((([0-9]*\\.[0-9]+)|([0-9]+\\.))([eE][-+]?[0-9]+)?)|([0-9]+([eE][-+]?[0-9]+)))[FfLl]?))|(?P<t_HEX_FLOAT_CONST>(0[xX]([0-9a-fA-F]+|((([0-9a-fA-F]+)?\\.[0-9a-fA-F]+)|([0-9a-fA-F]+\\.)))([pP][+-]?[0-9]+)[FfLl]?))|(?P<t_INT_CONST_HEX>0[xX][0-9a-fA-F]+(([uU]ll)|([uU]LL)|(ll[uU]?)|(LL[uU]?)|([uU][lL])|([lL][uU]?)|[uU])?)|(?P<t_BAD_CONST_OCT>0[0-7]*[89])|(?P<t_INT_CONST_OCT>0[0-7]*(([uU]ll)|([uU]LL)|(ll[uU]?)|(LL[uU]?)|([uU][lL])|([lL][uU]?)|[uU])?)|(?P<t_INT_CONST_DEC>(0(([uU]ll)|([uU]LL)|(ll[uU]?)|(LL[uU]?)|([uU][lL])|([lL][uU]?)|[uU])?)|([1-9][0-9]*(([uU]ll)|([uU]LL)|(ll[uU]?)|(LL[uU]?)|([uU][lL])|([lL][uU]?)|[uU])?))|(?P<t_CHAR_CONST>\'([^\'\\\\\\n]|(\\\\(([a-zA-Z._~!=&\\^\\-\\\\?\'"])|(\\d+)|(x[0-9a-fA-F]+))))\')|(?P<t_WCHAR_CONST>L\'([^\'\\\\\\n]|(\\\\(([a-zA-Z._~!=&\\^\\-\\\\?\'"])|(\\d+)|(x[0-9a-fA-F]+))))\')|(?P<t_UNMATCHED_QUOTE>(\'([^\'\\\\\\n]|(\\\\(([a-zA-Z._~!=&\\^\\-\\\\?\'"])|(\\d+)|(x[0-9a-fA-F]+))))*\\n)|(\'([^\'\\\\\\n]|(\\\\(([a-zA-Z._~!=&\\^\\-\\\\?\'"])|(\\d+)|(x[0-9a-fA-F]+))))*$))', [None, ('t_PPHASH', 'PPHASH'), ('t_JSON_START', 'JSON_START'), ('t_COMMENT', 'COMMENT'), None, ('t_SLASHCOMMENT', 'SLASHCOMMENT'), ('t_NEWLINE', 'NEWLINE'), ('t_LBRACE', 'LBRACE'), ('t_RBRACE', 'RBRACE'), ('t_FLOAT_CONST', 'FLOAT_CONST'), None, None, None, None, None, None, None, None, None, ('t_HEX_FLOAT_CONST', 'HEX_FLOAT_CONST'), None, None, None, None, None, None, None, ('t_INT_CONST_HEX', 'INT_CONST_HEX'), None, None, None, None, None, None, None, ('t_BAD_CONST_OCT', 'BAD_CONST_OCT'), ('t_INT_CONST_OCT', 'INT_CONST_OCT'), None, None, None, None, None, None, None, ('t_INT_CONST_DEC', 'INT_CONST_DEC'), None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, ('t_CHAR_CONST', 'CHAR_CONST'), None, None, None, None, None, None, ('t_WCHAR_CONST', 'WCHAR_CONST'), None, None, None, None, None, None, ('t_UNMATCHED_QUOTE', 'UNMATCHED_QUOTE')]), ('(?P<t_BAD_CHAR_CONST>(\'([^\'\\\\\\n]|(\\\\(([a-zA-Z._~!=&\\^\\-\\\\?\'"])|(\\d+)|(x[0-9a-fA-F]+))))[^\'\n]+\')|(\'\')|(\'([\\\\][^a-zA-Z._~^!=&\\^\\-\\\\?\'"x0-7])[^\'\\n]*\'))|(?P<t_WSTRING_LITERAL>L"([^"\\\\\\n]|(\\\\(([a-zA-Z._~!=&\\^\\-\\\\?\'"])|(\\d+)|(x[0-9a-fA-F]+))))*")|(?P<t_BAD_STRING_LITERAL>"([^"\\\\\\n]|(\\\\(([a-zA-Z._~!=&\\^\\-\\\\?\'"])|(\\d+)|(x[0-9a-fA-F]+))))*([\\\\][^a-zA-Z._~^!=&\\^\\-\\\\?\'"x0-7])([^"\\\\\\n]|(\\\\(([a-zA-Z._~!=&\\^\\-\\\\?\'"])|(\\d+)|(x[0-9a-fA-F]+))))*")|(?P<t_ID>[a-zA-Z_$][0-9a-zA-Z_$]*)|(?P<t_STRING_LITERAL>"([^"\\\\\\n]|(\\\\(([a-zA-Z._~!=&\\^\\-\\\\?\'"])|(\\d+)|(x[0-9a-fA-F]+))))*")|(?P<t_ELLIPSIS>\\.\\.\\.)|(?P<t_PLUSPLUS>\\+\\+)|(?P<t_LOR>\\|\\|)|(?P<t_XOREQUAL>\\^=)|(?P<t_OREQUAL>\\|=)|(?P<t_LSHIFTEQUAL><<=)|(?P<t_RSHIFTEQUAL>>>=)|(?P<t_PLUSEQUAL>\\+=)|(?P<t_TIMESEQUAL>\\*=)|(?P<t_PLUS>\\+)|(?P<t_MODEQUAL>%=)', [None, ('t_BAD_CHAR_CONST', 'BAD_CHAR_CONST'), None, None, None, None, None, None, None, None, None, None, ('t_WSTRING_LITERAL', 'WSTRING_LITERAL'), None, None, None, None, None, None, ('t_BAD_STRING_LITERAL', 'BAD_STRING_LITERAL'), None, None, None, None, None, None, None, None, None, None, None, None, None, ('t_ID', 'ID'), (None, 'STRING_LITERAL'), None, None, None, None, None, None, (None, 'ELLIPSIS'), (None, 'PLUSPLUS'), (None, 'LOR'), (None, 'XOREQUAL'), (None, 'OREQUAL'), (None, 'LSHIFTEQUAL'), (None, 'RSHIFTEQUAL'), (None, 'PLUSEQUAL'), (None, 'TIMESEQUAL'), (None, 'PLUS'), (None, 'MODEQUAL')]), ('(?P<t_DIVEQUAL>/=)|(?P<t_RBRACKET>\\])|(?P<t_CONDOP>\\?)|(?P<t_XOR>\\^)|(?P<t_LSHIFT><<)|(?P<t_LE><=)|(?P<t_LPAREN>\\()|(?P<t_ARROW>->)|(?P<t_EQ>==)|(?P<t_NE>!=)|(?P<t_MINUSMINUS>--)|(?P<t_OR>\\|)|(?P<t_TIMES>\\*)|(?P<t_LBRACKET>\\[)|(?P<t_GE>>=)|(?P<t_RPAREN>\\))|(?P<t_LAND>&&)|(?P<t_RSHIFT>>>)|(?P<t_ANDEQUAL>&=)|(?P<t_MINUSEQUAL>-=)|(?P<t_PERIOD>\\.)|(?P<t_EQUALS>=)|(?P<t_LT><)|(?P<t_COMMA>,)|(?P<t_DIVIDE>/)|(?P<t_AND>&)|(?P<t_MOD>%)|(?P<t_SEMI>;)|(?P<t_MINUS>-)|(?P<t_GT>>)|(?P<t_COLON>:)|(?P<t_NOT>~)|(?P<t_LNOT>!)', [None, (None, 'DIVEQUAL'), (None, 'RBRACKET'), (None, 'CONDOP'), (None, 'XOR'), (None, 'LSHIFT'), (None, 'LE'), (None, 'LPAREN'), (None, 'ARROW'), (None, 'EQ'), (None, 'NE'), (None, 'MINUSMINUS'), (None, 'OR'), (None, 'TIMES'), (None, 'LBRACKET'), (None, 'GE'), (None, 'RPAREN'), (None, 'LAND'), (None, 'RSHIFT'), (None, 'ANDEQUAL'), (None, 'MINUSEQUAL'), (None, 'PERIOD'), (None, 'EQUALS'), (None, 'LT'), (None, 'COMMA'), (None, 'DIVIDE'), (None, 'AND'), (None, 'MOD'), (None, 'SEMI'), (None, 'MINUS'), (None, 'GT'), (None, 'COLON'), (None, 'NOT'), (None, 'LNOT')])], 'ppdirective': [('(?P<t_ppdirective_line>.*\\n)', [None, ('t_ppdirective_line', 'line')])], 'ppjson': [('(?P<t_ppjson_NEWLINE>\\n)|(?P<t_ppjson_JSON_MODE>(decode|encode|both))|(?P<t_ppjson_JSON_KEYWORD>[a-zA-z0-9\\.\\[\\]]+(?= (: | \\n)))|(?P<t_ppjson_JSON_COLON>:)', [None, ('t_ppjson_NEWLINE', 'NEWLINE'), ('t_ppjson_JSON_MODE', 'JSON_MODE'), None, ('t_ppjson_JSON_KEYWORD', 'JSON_KEYWORD'), None, ('t_ppjson_JSON_COLON', 'JSON_COLON')])]}
_lexstateignore = {'ppjson': ' \t', 'ppline': ' \t', 'INITIAL': ' \t', 'ppdirective': ' \t', 'pppragma': ' \t<>.-{}();+-*/$%@&^~!?:,0123456789'}
_lexstateerrorf = {'ppline': 't_ppline_error', 'pppragma': 't_pppragma_error', 'INITIAL': 't_error', 'ppdirective': 't_ppdirective_error', 'ppjson': 't_ppjson_error'}