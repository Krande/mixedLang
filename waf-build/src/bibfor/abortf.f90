subroutine abortf()
    implicit none
#ifdef _WIN32
#include "abort_custom.h"
    call abort_custom()
#else
    call abort()
#endif
end subroutine