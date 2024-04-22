# Mixing C Languages

Experimenting with different build systems and mixing C, Fortran, C++ and Python. 

Work is primarily targeting MSVC in order to see how "easy" it is to make different build systems 
cope with the MSVC link-time requirement when resolving circular dependencies.

The examples are originally based on https://www.paulnorvig.com/guides/interoperability-of-fortran-with-cc.html
and on the [source code of Code Aster](https://gitlab.com/codeaster/src).