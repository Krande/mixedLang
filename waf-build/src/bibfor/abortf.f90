subroutine abortf()
    implicit none
#include "abort_custom.h"
    call abort_custom()
end subroutine