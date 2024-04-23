! A simple subroutine in Fortran
subroutine greet_fortran(name) bind(C, name = "greet_fortran")
    use, intrinsic :: iso_c_binding
    implicit none
#include "abortf.h"
    character(kind=c_char), dimension(*), intent(IN) :: name
    integer :: len
    integer :: i

    len=0
    do
        if (name(len+1) == C_NULL_CHAR) exit
        len = len + 1
    end do

    print *, 'Hello ', (name(i),i=1,len), '! Regards from Fortran.'

end subroutine greet_fortran