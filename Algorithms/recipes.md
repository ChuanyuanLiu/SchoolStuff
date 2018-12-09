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
