//
// Created by ofskrand on 23.04.2024.
//

#ifndef BIBCLIB_H
#define BIBCLIB_H

void greet_all_from_c();

// Declare the external C and Fortran subroutines
#ifdef __cplusplus
extern "C" {
#endif

void greet_c(char* str);

extern void greet_fortran(const char *name);

#ifdef __cplusplus
}
#endif

#endif //BIBCLIB_H
