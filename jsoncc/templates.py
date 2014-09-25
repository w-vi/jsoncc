#-----------------------------------------------------------------
# jsoncc: templates.py
#
# json en/decoding related C code templates
#
# Copyright (C) 2014, wvi
# License: GPLv3
#-----------------------------------------------------------------
warning_comment = "/*\n * IMPORATNT \n * This file has been generated with jsoncc from %s, DO NOT modify directly.\n */"
file_prelude = '#include <stdio.h>\n#include <string.h>\n#include <stdlib.h>\n#include <stddef.h>\n#include "frozen.h"\n\n\
typedef struct jsn_buf_s \n\
{\n\
    char *base;\n\
    size_t len;\n\
} jsn_buf_t;\n\n'

realloc = 'jsn_error_t buf_realloc(jsn_buf_t *buf, size_t len){ char *base = NULL; if (!(base = (char *)realloc(buf->base, buf->len + len))) return JSN_EMEM; memset(&base[buf->len], 0, len); buf->base = base; buf->len += len - 1; return JSN_OK;}'

strdup = "char * jsn_strdup(const char *s, size_t len){ char *dst = (char *) calloc(1, len + 1); return (dst) ? (char *) memcpy(dst, s, len) : NULL;}"

file_h_prelude = 'typedef enum jsn_error_e { JSN_OK = 0, JSN_EPARSE, JSN_ENOTFOUND, JSN_EINVAL, JSN_EMEM } jsn_error_t;\n\n'

get_str = "jsn_error_t get_str(const struct json_token *tok, char **val){ if (tok->type == JSON_TYPE_STRING || tok->type == JSON_TYPE_OBJECT) { *val = jsn_strdup(tok->ptr, tok->len); return JSN_OK; } if (tok->type == JSON_TYPE_NULL) { *val = NULL; return JSN_OK;} return JSN_EINVAL;}"

get_double = 'jsn_error_t get_double(const struct json_token *tok, double *val){ if (tok->type == JSON_TYPE_NUMBER) { sscanf(tok->ptr, "%lf", val); return JSN_OK; } return JSN_EINVAL; }'

get_int = "jsn_error_t get_int(const struct json_token *tok, int *val){ if (tok->type == JSON_TYPE_NUMBER) { for (int i = 0; i < tok->len; ++i) { if (tok->ptr[i] == 'e' || tok->ptr[i] == 'E' || tok->ptr[i] == '.') { return JSN_EINVAL; } } sscanf(tok->ptr, \"%hu\", val); return JSN_OK; } if (tok->type == JSON_TYPE_TRUE) { *val = 1; return JSN_OK; } if (tok->type == JSON_TYPE_FALSE) { *val = 0; return JSN_OK; } return JSN_EINVAL; }"

get_str_array = "jsn_error_t get_str_array(const struct json_token *toks, int index, char ***val) \
{ \
    int status  = JSN_OK; \
    const struct json_token *tok = &toks[index]; \
    char **ptr = NULL; \
 \
    if (tok->type == JSON_TYPE_ARRAY) { \
        ptr = (char **)calloc(tok->num_desc + 1, sizeof(char *)); \
        if (!ptr) return JSN_EMEM;\
        *val = ptr; \
        for (int i = index; i < index + tok->num_desc; ++i) \
        { \
            if(! JSN_OK == (status = get_str(&toks[i + 1], ptr))) goto end; \
            ++ptr; \
        } \
    } else {  \
        return JSN_EINVAL; \
    } \
end: \
    if (status) { \
        for(char *p = *ptr; p != NULL; p = *(++ptr)) \
            free(p); \
        free(ptr); \
        *val = NULL; \
    } \
    return status; \
}"

get_array = "jsn_error_t get_array_int(const struct json_token *toks, int index, int **val, int *count) \
{ \
    int status  = JSN_OK; \
    const struct json_token *tok = &toks[index]; \
    int *ptr = NULL; \
 \
    if (tok->type == JSON_TYPE_ARRAY) { \
        ptr = (int *)calloc(tok->num_desc, sizeof(int)); \
        if (!ptr) return JSN_EMEM;\
        *val = ptr; \
        *count = tok->num_desc; \
        for (int i = index; i < index + tok->num_desc; ++i) \
        { \
            if(JSN_OK != (status = get_int(&toks[i + 1], &ptr[i - index]))) goto end; \
        } \
    } else {  \
        return JSN_EINVAL; \
    } \
end: \
    if (status) { \
        free(ptr); \
        *val = NULL; \
    } \
    return status; \
}"

decode_func ="jsn_error_t jsn_decode_name(int *s, char *json_data, size_t json_len){struct json_token *arr; const struct json_token *tok; int status = JSN_OK; arr = parse_json2(json_data, json_len); if (!arr) return JSN_EPARSE;}"

free_func = "void jsn_destroy_name(int *s){ if (s) {}}"

free_item = "void xxx(){if (s->xxx) free(s->xxx);}"

free_str_arr = "void xxx (){ if (s->xxx) { char **ptr = s->xxx; for(char *p = *ptr; p != NULL; p = *(++ptr)) { free(p); } free(s->xxx);}}"

encode_func="jsn_error_t jsn_encode_name(int *s, char **b, size_t *len){ jsn_error_t status = JSN_OK; size_t p1 = 1; size_t p2 = 0; jsn_buf_t buf = {NULL, 0}; if (JSN_OK != (status = buf_realloc(&buf, JSN_ALLOC_CHUNK))) return status; buf.base[0]='{'; {} buf.base[p1-1]='}'; *b = buf.base; *len = p1; return status;}"

find_opt_token = 'void x(){tok = find_json_token(arr, "path"); if (tok) { \
if (JSN_OK != (status = func())) goto end;}}'

find_token = 'void x(){tok = find_json_token(arr, "path");if (!tok) \
{status = JSN_ENOTFOUND;  goto end; } if (JSN_OK != (status = func())) goto end;}'

emit_bool = 'void x(){p2 += (s->XXX) ? snprintf(&buf.base[p1], buf.len, "true,") : snprintf(&buf.base[p1], buf.len, "false,");if (p2 >= (buf.len - p1)) { if (JSN_OK != (status = buf_realloc(&buf, p2 + JSN_ALLOC_CHUNK))) return status; p1 += (s->XXX) ? snprintf(&buf.base[p1], buf.len, "true,") : snprintf(&buf.base[p1], buf.len, "false,");} else { p1 += p2; } p2 = 0;}'

emit_key = 'void x(){p2 += snprintf(&buf.base[p1], buf.len - p1, "XXXX"); if (p2 >= (buf.len - p1)) { if (JSN_OK != (status = buf_realloc(&buf, p2 + JSN_ALLOC_CHUNK))) return status; p1 += snprintf(&buf.base[p1], buf.len - p1, "XXXX");} else { p1 += p2; } p2 = 0;}'

emit_quoted = 'void x(){p2 += snprintf(&buf.base[p1], buf.len - p1, "\\"%s\\",",s->XXXX); if (p2 >= (buf.len - p1)) { if (JSN_OK != (status = buf_realloc(&buf, p2 + JSN_ALLOC_CHUNK))) return status; p1 += snprintf(&buf.base[p1], buf.len - p1, "\\"%s\\",",s->XXXX); } else { p1 += p2; } p2 = 0;}'

emit_number = 'void x(){p2 += snprintf(&buf.base[p1], buf.len - p1, "FMT", s->XXXX); if (p2 >= (buf.len - p1)) { if (JSN_OK != (status = buf_realloc(&buf, p2 + JSN_ALLOC_CHUNK))) return status; p1 += snprintf(&buf.base[p1], buf.len - p1, "FMT", s->XXXX);} else { p1 += p2; } p2 = 0;}'

emit_str = 'void x(){p2 += snprintf(&buf.base[p1], buf.len - p1, "%s,", s->XXXX); if (p2 >= (buf.len - p1)) { if (JSN_OK != (status = buf_realloc(&buf, p2 + JSN_ALLOC_CHUNK))) return status; p1 += snprintf(&buf.base[p1], buf.len - p1, "%s,", s->XXXX); } else {p1 += p2;} p2 = 0;}'

emit_optional='void x(){if (s->XXXX) { } else { p2 += snprintf(&buf.base[p1], buf.len - p1, "null,");if (p2 >= (buf.len - p1)) { if (JSN_OK != (status = buf_realloc(&buf, p2 + JSN_ALLOC_CHUNK))) return status; p1 += snprintf(&buf.base[p1], buf.len - p1, "null,"); } else { p1 += p2; } p2 = 0; }}'
