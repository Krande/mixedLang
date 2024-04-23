//
// Created by ofskrand on 23.04.2024.
//
// C++ code calling Fortran subroutine
#include <iostream>
#include "cpplib.h"


int main() {
    std::cout << "App (C++) is starting" << std::endl;
    greet_all_from_cpp();
    std::cout << "App (C++) is closing" << std::endl;
    return 0;
}