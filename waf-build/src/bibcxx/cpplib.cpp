//
// Created by ofskrand on 23.04.2024.
//

#include "cpplib.h"
#include "bibclib.h"

void greet_all_from_cpp(){

    char name[] = "C++ User";
    greet_fortran(name);
    greet_c(name);

}
