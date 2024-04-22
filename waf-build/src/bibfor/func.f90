! A simple subroutine in Fortran
subroutine greet_fortran(name) bind(C, name = "greet_fortran")
    use, intrinsic :: iso_c_binding
    character(kind = c_char), intent(in) :: name(*)
#include "abortf.h"
!    character(len=*), intent(in) :: name
! How to print the name in Fortran?
    print *, "Hello from Fortran: "
end subroutine greet_fortran