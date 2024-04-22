! A simple subroutine in Fortran
subroutine greet_fortran(name) bind(C, name = "greet_fortran")
    use, intrinsic :: iso_c_binding
!    character(kind = c_char), intent(in) :: name(*)
    character(len=*), intent(in) :: name

    print *, "Hello from Fortran: "
    print *, name
end subroutine greet_fortran