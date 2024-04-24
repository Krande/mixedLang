# CMake build issue

This simple example was created to demonstrate missing symbols in an exported dll library when using CMake on Windows.

~~However, for now it seems all symbols are properly exported in this minimal example.~~

The issue is reproduced, and the reason behind it is found: https://gitlab.kitware.com/cmake/cmake/-/issues/25598

