## Debug macro

This is from Design of Algorithm material

```c
#define DEBUG 1
#if DEBUG
#define DUMPINT(x) printf("line %3d: %s = %d\n", __LINE__, #x, x)
#else
#define DUMPINT(x)
#endif
```



## Makefile

### Resources: 

[Using "make" and writing Makefiles](https://www.cs.oberlin.edu/~kuperman/help/make.html) Highly recommended reading. ❤️

[Makefile tutorial by Alex Allain](https://www.cprogramming.com/tutorial/makefiles.html) 

[Makefile template by Maxwell](http://www.cs.colby.edu/maxwell/courses/tutorials/maketutor/) 

### How are files compiled ![img](https://www3.ntu.edu.sg/home/ehchua/programming/cpp/images/GCC_CompilationProcess.png)

From [Nanyang Technological University](https://www3.ntu.edu.sg/home/ehchua/programming/cpp/gcc_make.html)

### Template

**What I am doing here?**

I want to compile two different executables, where each executable uses arrayList.

```makefile
# set compiler to gcc
CC     = gcc
# -Wall means show all errors
CFLAGS = -Wall
 
# Name the two different executables
# List object files for each executables
EXE1   = part1
OBJ1    = part1.o arrayList.o
EXE2   = part2
OBJ2    = part2.o arrayList.o

# This is where Makefile compiles part1
$(EXE1): $(OBJ1)
	$(CC) $(CFLAGS) -o $@ $^

# This is where Makefile compiles part2
$(EXE2): $(OBJ2)
	$(CC) $(CFLAGS) -o $@ $^

# list all the object files and their dependency on header files
# and set rules for making them
arrayList.o: arrayList.c arrayList.h
	$(CC) $(CFLAGS) -c $^

# define all the methods
.PHONEY: all runPart1 runPart2 clean

# make everything
all: $(EXE1) $(EXE2)

# removes everything
clean:
	rm -f $(OBJ1) $(OBJ2) $(EXE1) $(EXE2)

# make and run part1
runPart1: $(EXE1)
	./$^ 

# make and run part2
runPart2: $(EXE2)
	./$^ 
```

### Example usages

**Make everything**

```bash
$ make all
gcc -Wall   -c -o part1.o part1.c
gcc -Wall -o part1 part1.o arrayList.o
gcc -Wall   -c -o part2.o part2.c
gcc -Wall -o part2 part2.o arrayList.o
```

**Make and run**

```bash
$ make runPart2
./part2
Kelvin is  tired tired
```

**Delete object and executable files**

```bash
$ make clean
rm -f part1.o arrayList.o part2.o arrayList.o part1 part2
```



### Explaination

#### Macros

 'variables' that you can assign values to and reuse

**Set** your C compiler to gcc. `CC=gcc` 

**Set** composite macros. `TEST = CC FILES`

**Retreve** the values stored in macro. `$(CC)` this will give `gcc`

| Macro            | meaning                             |
| ---------------- | ----------------------------------- |
| `CC = gcc`       | Compiler set as `gcc`               |
| `FILES = main.c` | Set c file to `main.c`              |
| `EXE = main`     | Set output executive file to `main` |
| `DEPS = main.h`  | Set header file to `main.h`         |
| `CFLAGS = -Wall` | Compiling flag set to `-Wall`       |

#### Special Macros

| Macros | meaning            |
| ------ | ------------------ |
| $@     | Name of the target |
| $?     | List of dependents |

### Note:

Must follow indentation

File must be called `Makefile` or `makefile` without any file types

