#include <stdio.h>
#include "include/bibclib.h"



int main(int argc, char **argv) {
    printf("App (C) is running.\n");
    greet_all_from_c();
    printf("App (C) is closing.\n");
    return 0;
}
