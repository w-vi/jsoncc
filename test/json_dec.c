/*
 * IMPORATNT 
 * This file has been generated with jsoncc from json_struct.h, DO NOT modify directly.
 */
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <stddef.h>
#include "frozen.h"

typedef struct jsn_buf_s 
{
    char *base;
    size_t len;
} jsn_buf_t;


#include "json_dec.h"

#define JSN_ALLOC_CHUNK 512

jsn_error_t buf_realloc(jsn_buf_t *buf, size_t len)
{
  char *base = NULL;
  if (!(base = (char *) realloc(buf->base, buf->len + len)))
    return JSN_EMEM;

  memset(&base[buf->len], 0, len);
  buf->base = base;
  buf->len += len - 1;
  return JSN_OK;
}

jsn_error_t jsn_encode_trace_get_desc_rq(trace_get_desc_rq_t *s, char **b, size_t *len)
{
  jsn_error_t status = JSN_OK;
  size_t p1 = 1;
  size_t p2 = 0;
  jsn_buf_t buf = {NULL, 0};
  if (JSN_OK != (status = buf_realloc(&buf, JSN_ALLOC_CHUNK)))
    return status;

  buf.base[0] = '{';
  {
    {
      p2 += snprintf(&buf.base[p1], buf.len - p1, "\"actID\":" );
      if (p2 >= (buf.len - p1))
      {
        if (JSN_OK != (status = buf_realloc(&buf, p2 + JSN_ALLOC_CHUNK)))
          return status;

        p1 += snprintf(&buf.base[p1], buf.len - p1, "\"actID\":");
      }
      else
      {
        p1 += p2;
      }

      p2 = 0;
    }
    {
      if (s->actID)
      {
        p2 += snprintf(&buf.base[p1], buf.len - p1, "\"%s\",", s->actID);
        if (p2 >= (buf.len - p1))
        {
          if (JSN_OK != (status = buf_realloc(&buf, p2 + JSN_ALLOC_CHUNK)))
            return status;

          p1 += snprintf(&buf.base[p1], buf.len - p1, "\"%s\",", s->actID);
        }
        else
        {
          p1 += p2;
        }

        p2 = 0;
      }
      else
      {
        p2 += snprintf(&buf.base[p1], buf.len - p1, "null,");
        if (p2 >= (buf.len - p1))
        {
          if (JSN_OK != (status = buf_realloc(&buf, p2 + JSN_ALLOC_CHUNK)))
            return status;

          p1 += snprintf(&buf.base[p1], buf.len - p1, "null,");
        }
        else
        {
          p1 += p2;
        }

        p2 = 0;
      }

    }
    {
      p2 += snprintf(&buf.base[p1], buf.len - p1, "\"valid\":");
      if (p2 >= (buf.len - p1))
      {
        if (JSN_OK != (status = buf_realloc(&buf, p2 + JSN_ALLOC_CHUNK)))
          return status;

        p1 += snprintf(&buf.base[p1], buf.len - p1, "\"valid\":");
      }
      else
      {
        p1 += p2;
      }

      p2 = 0;
    }
    {
      p2 += s->valid ? snprintf(&buf.base[p1], buf.len, "true,") : snprintf(&buf.base[p1], buf.len, "false,");
      if (p2 >= (buf.len - p1))
      {
        if (JSN_OK != (status = buf_realloc(&buf, p2 + JSN_ALLOC_CHUNK)))
          return status;

        p1 += s->valid ? snprintf(&buf.base[p1], buf.len, "true,") : snprintf(&buf.base[p1], buf.len, "false,");
      }
      else
      {
        p1 += p2;
      }

      p2 = 0;
    }
    {
      p2 += snprintf(&buf.base[p1], buf.len - p1, "\"userID\":");
      if (p2 >= (buf.len - p1))
      {
        if (JSN_OK != (status = buf_realloc(&buf, p2 + JSN_ALLOC_CHUNK)))
          return status;

        p1 += snprintf(&buf.base[p1], buf.len - p1, "\"userID\":");
      }
      else
      {
        p1 += p2;
      }

      p2 = 0;
    }
    {
      p2 += snprintf(&buf.base[p1], buf.len - p1, "%hd,", s->userID);
      if (p2 >= (buf.len - p1))
      {
        if (JSN_OK != (status = buf_realloc(&buf, p2 + JSN_ALLOC_CHUNK)))
          return status;

        p1 += snprintf(&buf.base[p1], buf.len - p1, "%hd,", s->userID);
      }
      else
      {
        p1 += p2;
      }

      p2 = 0;
    }
    {
      p2 += snprintf(&buf.base[p1], buf.len - p1, "\"inner\":" );
      if (p2 >= (buf.len - p1))
      {
        if (JSN_OK != (status = buf_realloc(&buf, p2 + JSN_ALLOC_CHUNK)))
          return status;

        p1 += snprintf(&buf.base[p1], buf.len - p1, "\"inner\":");
      }
      else
      {
        p1 += p2;
      }

      p2 = 0;
    }
    {
      p2 += snprintf(&buf.base[p1], buf.len - p1, "%s,", s->inner);
      if (p2 >= (buf.len - p1))
      {
        if (JSN_OK != (status = buf_realloc(&buf, p2 + JSN_ALLOC_CHUNK)))
          return status;

        p1 += snprintf(&buf.base[p1], buf.len - p1, "%s,", s->inner);
      }
      else
      {
        p1 += p2;
      }

      p2 = 0;
    }
  }
  buf.base[p1 - 1] = '}';
  *b = buf.base;
  *len = p1;
  return status;
}

jsn_error_t get_unsignedshortint(const struct json_token *tok, unsigned short int *val)
{
  if (tok->type == JSON_TYPE_NUMBER)
  {
    for (int i = 0; i < tok->len; ++i)
    {
      if (((tok->ptr[i] == 'e') || (tok->ptr[i] == 'E')) || (tok->ptr[i] == '.'))
      {
        return JSN_EINVAL;
      }

    }

    sscanf(tok->ptr, "%hu", val);
    return JSN_OK;
  }

  if (tok->type == JSON_TYPE_TRUE)
  {
    *val = 1;
    return JSN_OK;
  }

  if (tok->type == JSON_TYPE_FALSE)
  {
    *val = 0;
    return JSN_OK;
  }

  return JSN_EINVAL;
}

char *jsn_strdup(const char *s, size_t len)
{
  char *dst = (char *) calloc(1, len + 1);
  return dst ? (char *) memcpy(dst, s, len) : NULL;
}

jsn_error_t get_str(const struct json_token *tok, char **val)
{
  if ((tok->type == JSON_TYPE_STRING) || (tok->type == JSON_TYPE_OBJECT))
  {
    *val = jsn_strdup(tok->ptr, tok->len);
    return JSN_OK;
  }

  return JSN_EINVAL;
}

jsn_error_t get_str_array(const struct json_token *toks, int index, char ***val)
{
  int status = JSN_OK;
  const struct json_token *tok = &toks[index];
  char **ptr = NULL;
  if (tok->type == JSON_TYPE_ARRAY)
  {
    ptr = (char **) calloc(tok->num_desc + 1, sizeof(char *));
    if (!ptr)
      return JSN_EMEM;

    *val = ptr;
    for (int i = index; i < (index + tok->num_desc); ++i)
    {
      if ((!JSN_OK) == (status = get_str(&toks[i + 1], ptr)))
        goto end;

      ++ptr;
    }

  }
  else
  {
    return JSN_EINVAL;
  }

  end:
  if (status)
  {
    for (char *p = *ptr; p != NULL; p = *(++ptr))
      free(p);

    free(ptr);
    *val = NULL;
  }


  return status;
}

jsn_error_t get_int(const struct json_token *tok, int *val)
{
  if (tok->type == JSON_TYPE_NUMBER)
  {
    for (int i = 0; i < tok->len; ++i)
    {
      if (((tok->ptr[i] == 'e') || (tok->ptr[i] == 'E')) || (tok->ptr[i] == '.'))
      {
        return JSN_EINVAL;
      }

    }

    sscanf(tok->ptr, "%d", val);
    return JSN_OK;
  }

  if (tok->type == JSON_TYPE_TRUE)
  {
    *val = 1;
    return JSN_OK;
  }

  if (tok->type == JSON_TYPE_FALSE)
  {
    *val = 0;
    return JSN_OK;
  }

  return JSN_EINVAL;
}

jsn_error_t get_array_int(const struct json_token *toks, int index, int **val, int *count)
{
  int status = JSN_OK;
  const struct json_token *tok = &toks[index];
  int *ptr = NULL;
  if (tok->type == JSON_TYPE_ARRAY)
  {
    ptr = (int *) calloc(tok->num_desc, sizeof(int));
    if (!ptr)
      return JSN_EMEM;

    *val = ptr;
    *count = tok->num_desc;
    for (int i = index; i < (index + tok->num_desc); ++i)
    {
      if ((!JSN_OK) == (status = get_int(&toks[i + 1], &ptr[i - index])))
        goto end;

    }

  }
  else
  {
    return JSN_EINVAL;
  }

  end:
  if (status)
  {
    free(ptr);
    *val = NULL;
  }


  return status;
}

jsn_error_t get_float(const struct json_token *tok, float *val)
{
  if (tok->type == JSON_TYPE_NUMBER)
  {
    sscanf(tok->ptr, "%f", val);
    return JSN_OK;
  }

  return JSN_EINVAL;
}

jsn_error_t get_double(const struct json_token *tok, double *val)
{
  if (tok->type == JSON_TYPE_NUMBER)
  {
    sscanf(tok->ptr, "%lf", val);
    return JSN_OK;
  }

  return JSN_EINVAL;
}

jsn_error_t jsn_decode_trace_desc(trace_desc_t *s, char *json_data, size_t json_len)
{
  struct json_token *arr;
  const struct json_token *tok;
  int status = JSN_OK;
  arr = parse_json2(json_data, json_len);
  if (!arr)
    return JSN_EPARSE;

  tok = find_json_token(arr, "user.activeDays");
  if (!tok)
  {
    status = JSN_ENOTFOUND;
    goto end;
  }

  if (!(JSN_OK == (status = get_unsignedshortint(tok, &s->activedays))))
    goto end;

  tok = find_json_token(arr, "user.domain");
  if (tok)
  {
    if (!(JSN_OK == (status = get_str(tok, &s->domain))))
      goto end;

  }

  tok = find_json_token(arr, "user.state");
  if (tok)
  {
    if (!(JSN_OK == (status = get_str_array(arr, (tok - arr), &s->states))))
      goto end;

  }

  tok = find_json_token(arr, "user.stateno");
  if (!tok)
  {
    status = JSN_ENOTFOUND;
    goto end;
  }

  if (!(JSN_OK == (status = get_array_int(arr, (tok - arr), &s->statenos, &s->statenos_count_))))
    goto end;

  tok = find_json_token(arr, "userServer[0].url");
  if (!tok)
  {
    status = JSN_ENOTFOUND;
    goto end;
  }

  if (!(JSN_OK == (status = get_str(tok, &s->gatewayurl))))
    goto end;

  tok = find_json_token(arr, "userServer[0].events.url");
  if (!tok)
  {
    status = JSN_ENOTFOUND;
    goto end;
  }

  if (!(JSN_OK == (status = get_str(tok, &s->eventurl))))
    goto end;

  tok = find_json_token(arr, "user.location.latitude");
  if (!tok)
  {
    status = JSN_ENOTFOUND;
    goto end;
  }

  if (!(JSN_OK == (status = get_float(tok, &s->lat))))
    goto end;

  tok = find_json_token(arr, "user.location.longitude");
  if (!tok)
  {
    status = JSN_ENOTFOUND;
    goto end;
  }

  if (!(JSN_OK == (status = get_double(tok, &s->lon))))
    goto end;

  end:
  free(arr);

  return status;
}

void jsn_free_trace_desc(trace_desc_t *s)
{
  if (s)
  {
    if (s->domain)
      free(s->domain);

    if (s->states)
    {
      char **ptr = s->states;
      for (char *p = *ptr; p != NULL; p = *(++ptr))
      {
        free(p);
      }

      free(s->states);
    }

    if (s->statenos)
      free(s->statenos);

    if (s->gatewayurl)
      free(s->gatewayurl);

    if (s->eventurl)
      free(s->eventurl);

  }

}

