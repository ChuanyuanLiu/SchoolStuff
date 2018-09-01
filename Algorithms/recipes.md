## Debug macro

This is from Design of Algorithm material

```c
#define DEBUG 1
#if 
#define DUMPINT(x) printf("line %3d: %s = %d\n", __LINE__, #x, x)
#else
#define DUMPINT(x)
#endif
```



## Makefile

### Resources: 

[Makefile tutorial by Alex Allain](https://www.cprogramming.com/tutorial/makefiles.html) Highly recommended reading. ❤️

[Makefile template by Maxwell](http://www.cs.colby.edu/maxwell/courses/tutorials/maketutor/) 



### Template

This is also from Design of Algorithm material

```makefile
CC     = gcc
CFLAGS = -Wall 
EXE    = stage1
OBJ    = main.o stage1.o

# top (default) target
all: $(EXE)

# how to link executable
$(EXE): $(OBJ)
	$(CC) $(CFLAGS) -o $(EXE) $(OBJ)
	
# other dependencies
main.o: stage1.h

# phony targets (these targets do not represent actual files)
.PHONY: clean cleanly all CLEAN

# `make clean` to remove all object files
# `make CLEAN` to remove all object and executable files
# `make cleanly` to `make` then immediately remove object files (inefficient)
clean:
	rm -f $(OBJ)
CLEAN: clean
	rm -f $(EXE)
cleanly: all clean
```



### Explaination

#### Macros

 'variables' that you can assign values to and reuse

**Set** your C compiler to gcc. `CC=gcc` 

**Set** composite macros. `TEST = CC FILES`

**Retreve** the values stored in macro. `$(CC)` this will give `gcc`

| Macro            | meaning                             |
| ---------------- | ----------------------------------- |
| `CC = gcc`       | Compiler set as gcc                 |
| `FILES = main.c` | Set c file to `main.c`              |
| `EXE = main`     | Set output executive file to `main` |
| `DEPS = main.h`  | Set header file to `main.h`         |
| `CFLAGS = -Wall` | Compiling flag set to `-Wall`       |



### Note:

There must be a tab at the beginning of any command.

