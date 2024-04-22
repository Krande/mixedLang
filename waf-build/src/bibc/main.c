#include <stdio.h>

// Declare the Fortran subroutine
extern void greet_fortran(char* str, int len);


int main(int argc, char **argv) {
    printf("App is running.\n");
    char c_string[] = "CUser";
    greet_fortran(c_string, sizeof(c_string) - 1);
    printf("App is closing.\n");
    return 0;
}
