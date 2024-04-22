@echo off
setlocal

call conda_env.bat
set FC=ifx.exe

waf distclean

waf configure ^
    --check-fortran-compiler=ifort ^
    --prefix=%LIBRARY_PREFIX%

waf install src -v

endlocal