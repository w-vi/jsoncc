#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <curl/curl.h>
#include "jsonio.h"
#include <assert.h>

typedef struct
{
    char *base;
    size_t len;
    size_t pos;
} pos_buf_t;

typedef struct ctx_s
{
    pos_buf_t rcv_buf;
    github_user_t user;
    search_extension_res_t search;
    search_item_t search_item;
} CTX;

int
pos_buf_realloc(pos_buf_t *buf, size_t len)
{
    char *base = NULL;
    if (!(base = (char *)realloc(buf->base, len))) goto error;

    buf->base = base;
    buf->len = len;
    return 0;

error:
    if (base) free(base);
    return -1;
}

size_t
write_cb(void *data, size_t size, size_t nmemb, void *userp)
{
    CTX *ctx = (CTX *)userp;
    size_t realsize = size * nmemb;
    if ((ctx->rcv_buf.len - ctx->rcv_buf.pos) < realsize) {
        if (pos_buf_realloc(&ctx->rcv_buf, ctx->rcv_buf.len + realsize)) {
            fprintf(stderr, "Memory error\n");
            exit(EXIT_FAILURE);


        }
    }
    memcpy(&ctx->rcv_buf.base[ctx->rcv_buf.pos], data, realsize);
    ctx->rcv_buf.pos += realsize;
    ctx->rcv_buf.base[ctx->rcv_buf.pos] = 0;
    return realsize;
}

int
main(int argc, char *argv[])
{
    CURL *curl;
    CURLcode res;
    CTX ctx;
    char req[1024];
    jsn_error_t jsn_err = JSN_OK;
    char **ptr = NULL;
    char *p = NULL;
    
    if (argc < 3) {
        fprintf(stderr, "Not enough command paramters.\n");
        fprintf(stderr, "Usage: github_test github-user-name file extension\n");
        fprintf(stderr, "Examples:\n github_test w-vi py\n github_test w-vi md\n");
        fprintf(stderr, " github_test w-vi c\n github_test w-vi txt\n");
        exit(EXIT_FAILURE);
    }

    memset(&ctx, 0, sizeof(CTX));
    if (! (ctx.rcv_buf.base = (char *)malloc(4096))) {
        fprintf(stderr, "Memory error\n");
        exit(EXIT_FAILURE);
    }
    
    curl_global_init(CURL_GLOBAL_DEFAULT);
    curl = curl_easy_init();
    if(curl) {
        snprintf(req, 1024, "https://api.github.com/users/%s", argv[1]);
        curl_easy_setopt(curl, CURLOPT_URL, req);
 
        /* Set user agent as required by github api */
        curl_easy_setopt(curl, CURLOPT_USERAGENT, "jsoncc-test/0.1");

        /* send all data to this function  */ 
        curl_easy_setopt(curl, CURLOPT_WRITEFUNCTION, write_cb);
  
        /* we pass our 'chunk' struct to the callback function */ 
        curl_easy_setopt(curl, CURLOPT_WRITEDATA, (void *)&ctx);
        
        /* Perform the request, res will get the return code */ 
        res = curl_easy_perform(curl);
        /* Check for errors */ 
        if(res != CURLE_OK) {
            fprintf(stderr, "curl_easy_perform() failed: %s\n",
                    curl_easy_strerror(res));
            exit(EXIT_SUCCESS);
        }
        if(JSN_OK != (jsn_err = jsn_decode_github_user(&ctx.user,
                                              ctx.rcv_buf.base,
                                              ctx.rcv_buf.pos))) {
            fprintf(stderr, "Decode error %d\n", jsn_err);
            fprintf(stderr, "Received:\n%s\n", ctx.rcv_buf.base);
            exit(EXIT_FAILURE);
        }
        printf("User info:\n");
        printf("Name:\t%s\nID:   \t%lu\nURL: \t%s\n", ctx.user.name,
               ctx.user.id, ctx.user.url);
        if (ctx.user.company) {
            printf("Company:\t%s\n", ctx.user.company);
        }
        if (ctx.user.bio) {
            printf("Bio: \t%s\n", ctx.user.bio);
        }
        printf("(%lu bytes retrieved)\n", (long)ctx.rcv_buf.pos);

        snprintf(req, 1024,
                 "https://api.github.com/search/code?q=user:%s+extension:%s",
                 ctx.user.login, argv[2]);

        jsn_free_github_user(&ctx.user);
        ctx.rcv_buf.pos = 0;
        curl_easy_setopt(curl, CURLOPT_URL, req);
        /* Perform the request, res will get the return code */ 
        res = curl_easy_perform(curl);
        /* Check for errors */ 
        if(res != CURLE_OK) {
            fprintf(stderr, "curl_easy_perform() failed: %s\n",
                    curl_easy_strerror(res));
            exit(EXIT_SUCCESS);
        } 
        if(JSN_OK != (jsn_err = jsn_decode_search_extension_res(&ctx.search,
                                              ctx.rcv_buf.base,
                                              ctx.rcv_buf.pos))) {
            fprintf(stderr, "Decode error %d\n", jsn_err);
            fprintf(stderr, "Received:\n%s\n", ctx.rcv_buf.base);
            exit(EXIT_FAILURE);
        }
        ptr = ctx.search.items;
        for(p = *ptr; p != NULL; p = *(++ptr))
        {
            search_item_t s;
            memset(&s, 0, sizeof(search_item_t));
            
            jsn_decode_search_item(&s, p, strlen(p));

            printf("\n");
            printf("file.name: %s\n", s.name);
            printf("file.path: %s\n", s.path);
            printf("file.repo: %s\n", s.repo);
            jsn_free_search_item(&s);
        }    
        printf("Call the search.\n");

        jsn_free_search_extension_res(&ctx.search);
        printf("(%lu bytes retrieved)\n", (long)ctx.rcv_buf.pos);
        
        /* always cleanup */ 
        curl_easy_cleanup(curl);
        free(ctx.rcv_buf.base);
    }
 
    curl_global_cleanup();

    return 0;
}
