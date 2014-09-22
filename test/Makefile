CC = gcc
CFLAGS = -std=c99 -O0 -g -Wall
INC = -I.
LDFALGS=

SRC= main_test.c frozen.c json_dec.c
OBJ=$(SRC:%.c=%.o)
EXE=jsn_test

all: $(SRC) $(EXE)

$(EXE): $(OBJ) 
	$(CC) $(LDFLAGS) $(OBJ) -o $@

%.o: %c
	$(CC) $(CFLAGS) $(INC) $< -o $@

json_dec.c:
	python ../jsoncc/jsoncc.py -i json_struct.h  -o json_dec

clean:
	rm -f json_dec.*
	rm -f *.o
	rm -f $(EXE)

.PHONY: all clean
