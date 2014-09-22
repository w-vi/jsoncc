#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <stddef.h>
#include "frozen.h"
#include "json_dec.h"
#include "json_struct.h"


int main(int argc, char *argv[])
{
    int status = JSN_OK;
    char **ptr = NULL;
    trace_desc_t *trc = (trace_desc_t *)calloc(1, sizeof(trace_desc_t));
    char *source = NULL;
    FILE *fp = fopen("json.txt", "r");
    if (fp != NULL) {
        /* Go to the end of the file. */
        if (fseek(fp, 0L, SEEK_END) == 0) {
            /* Get the size of the file. */
            long bufsize = ftell(fp);
            if (bufsize == -1) {
                fprintf(stderr, "buffsize -1 file not found.\n");
                return -1;
            }

            /* Allocate our buffer to that size. */
            source = malloc(sizeof(char) * (bufsize + 1));
            
            /* Go back to the start of the file. */
            if (fseek(fp, 0L, SEEK_SET) != 0) {
                fprintf(stderr, "SEEK_SET file not found.\n");
                return -1;
            }

            /* Read the entire file into memory. */
            size_t newLen = fread(source, sizeof(char), bufsize, fp);
            if (newLen == 0) {
                fputs("Error reading file", stderr);
            } else {
                source[++newLen] = '\0'; /* Just to be safe. */
            }
        }
    
        fclose(fp);
    }
    else
    {
        fprintf(stderr, "fp NULL = file not found.\n");
        return -1;
        
    }

    printf("%s\n",source);

    status = jsn_decode_trace_desc(trc, source, strlen(source));
    printf("Status %d\n", status);

    if (JSN_OK == status)
    {
        ptr = trc->states;

        printf("user.activeDays = %d\n", trc->activedays);
        printf("user.domain = %s\n", trc->domain);
        printf("gateway url = %s\n", trc->gatewayurl);
        printf("events url = %s\n", trc->eventurl);
        printf("long %lf, lat %f\n", trc->lon, trc->lat);
        printf("user.states =");
        for(char *p = *ptr; p != NULL; p = *(++ptr))
        {
            printf(" %s", p);
        }
        printf("\n");
        printf("user.statenos =");
        for(int i = 0; i < trc->statenos_count_; ++i)
        {
            printf(" %d", trc->statenos[i]);
        }
        printf("\n");
    }

    jsn_free_trace_desc(trc);
    
    
    trace_get_desc_rq_t tgr = {"asdcvl", 1, 356, "{\"foo\": 123}"};
    char *buf = NULL;
    size_t len = 0;

    status = jsn_encode_trace_get_desc_rq(&tgr, &buf, &len);
    printf("Status %d\n", status);

    if(!status)
        printf("%s\n", buf);

    for(int i = 0; i < len; ++i)
    {
        printf(" %d", buf[i]);
    }
    printf("\n");

    return  status;
}
