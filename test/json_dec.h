#ifndef JSON_DEC_H_ 
#define JSON_DEC_H_ 1
/*
 * IMPORATNT 
 * This file has been generated with jsoncc from json_struct.h, DO NOT modify directly.
 */
#include "json_struct.h"

#ifdef __cplusplus
extern "C" {
#endif

typedef enum jsn_error_e {JSN_OK = 0, JSN_EPARSE, JSN_ENOTFOUND, JSN_EINVAL, JSN_EMEM} jsn_error_t;
jsn_error_t jsn_encode_trace_get_desc_rq(trace_get_desc_rq_t *s, char **b, size_t *len);
jsn_error_t jsn_decode_trace_desc(trace_desc_t *s, char *json_data, size_t json_len);
void jsn_free_trace_desc(trace_desc_t *s);

#ifdef __cplusplus
}
#endif
#endif /* #ifndef JSON_DEC_H_ */
