//
// Created by ofskrand on 23.04.2024.
//

#include "include/bibclib.h"

#include <stdlib.h>

// Function to abort the program
void abort_custom() {
    printf("Abort called from C\n");
    abort();
}


void greet_c(char* str) {
    printf("Hello '%s!' Regards from C\n", str);
}

void greet_all_from_c(){
    char c_string[] = "CUser";
    greet_c(c_string);
    greet_fortran(c_string);
}