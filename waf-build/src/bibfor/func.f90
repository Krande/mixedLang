! A simple subroutine in Fortran
subroutine greet_fortran(name) bind(C, name = "greet_fortran")
    use, intrinsic :: iso_c_binding
    implicit none
#include "abortf.h"
    character(kind=c_char), intent(in) :: name(*)
    character(len=256) :: fort_name
    integer :: i
    ! Check if the first character is the null terminator
    if (name(0) == c_null_char) then
        print*, "C string is empty at start."

        print*, "Calling abortf()..."
        call abortf()
        return
    endif

    i = 0
    do
        if (name(i) == c_null_char) then
            print*, "End of C string reached."
            exit
        else
            print*, "Character: ", name(i)
            fort_name(i+1:i+1) = name(i)
        endif
        i = i + 1
    end do
    fort_name = adjustl(fort_name(1:i))  ! Adjust left to remove any leading spaces

    ! Use the Fortran string
    print*, "Hello ", trim(fort_name), "! Regards from Fortran."

end subroutine greet_fortran