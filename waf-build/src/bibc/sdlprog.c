#include <stdio.h>

// Declare the Fortran subroutine
extern void greet_fortran(const char *name);

int main(int argc, char **argv) {
    printf("App is running.\n");
    const char *name = "C User";
    greet_fortran(name);
    return 0;
}
