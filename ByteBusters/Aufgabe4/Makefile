
CFLAGS= -O2  -Wall -Wextra 
OBJ=main.o
.SUFFIXES: .c.o .o .c

test: fünf
	./fünf krocket1.txt


%.o: %.c
	gcc -o $@ -c $(CFLAGS) $<

fünf: $(OBJ) 
	gcc -o fünf $(OBJ) -lm $(CFLAGS) 

