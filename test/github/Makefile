CC = gcc
CFLAGS = -std=c99 -O0 -g -Wall
INC = -I. -I/usr/include
LDFLAGS = -L/usr/local/ssl/lib
LIB= -lcurl -lssl -lcrypto

SRC= github.c frozen.c jsonio.c
OBJ=$(SRC:%.c=%.o)
EXE=github_test

all: $(SRC) $(EXE)

$(EXE): $(OBJ) 
	$(CC) $(LDFLAGS) $(LIB) $(OBJ) -o $@

%.o: %c
	$(CC) $(CFLAGS) $(INC) $< -o $@

jsonio.c:
	python ../../jsoncc/jsoncc.py -i json_github.h  -o jsonio

clean:
	rm -f jsonio.* *.o $(EXE) *.py

.PHONY: all clean
