#ifndef JSON_STRUCT_H_
#define JSON_STRUCT_H_ 1


//+json:encode
typedef struct trace_get_desc_rq_s
{
    char *actID; //+json:optional
    int valid; //+json:boolean
    short int userID ;
    char *inner; //+json:json
} trace_get_desc_rq_t ;


//+json:decode
typedef struct trace_desc_s
{
    unsigned short int activedays; //+json:user.activeDays
    char *domain; //+json:user.domain:optional
    char **states; //+json:user.state:optional
    int *statenos; //+json:user.stateno
    int statenos_count_;
    char *gatewayurl; //+json:userServer[0].url
    char *eventurl; //+json:userServer[0].events.url
    float lat; //+json:user.location.latitude
    double lon; //+json:user.location.longitude
} trace_desc_t ;


extern int xxx;

typedef struct xxx_s
{
    int fff;
    char *wtf;
} xxx_t;

int json_emit_int(char *buf, int buf_len, long int value);


#endif /* JSON_STRUCT_H_ */



