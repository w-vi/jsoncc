#ifndef JSON_GITHUB_H_
#define JSON_GITHUB_H_ 1

//+json:decode:free
typedef struct github_user_s
{
    char *login;//+json:login
    char *name;//+json:name
    unsigned long id;//+json:id
    char *url;//+json:html_url
    char *company;//+json:company:optional
    char *bio;//+json:bio:optional
} github_user_t;

//+json:decode:free
typedef struct search_extension_res_s
{
    int count;//+json:total_count
    char **items;//+json:items
} search_extension_res_t;

//+json:decode:free
typedef struct search_item_s
{
    char *name;//+json:name
    char *path;//+json:path
    char *repo;//+json:repository.name
    char *file_url;//+json:html_url
} search_item_t;


#endif /* JSON_GITHUB_H_ */
