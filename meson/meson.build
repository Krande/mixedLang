project('sdldemo', 'c', 'cpp', 'fortran', default_options : ['default_library=shared'])


ff = meson.get_compiler('fortran')
_intel_fflags = ff.get_supported_arguments(
    '/fp:strict', '/MD', '/names:lowercase', '/assume:underscore',
    '/assume:minus0'
  )
add_project_arguments(_intel_fflags, language: 'fortran')
# Fortran source files
fortran_src = ['src/bibfor/func.f90']  # Add your Fortran source files here
# Create a shared library from the Fortran sources
fort_lib = shared_library('myfortlib', fortran_src, install : true, version : '1.0')


# Define the dependencies needed for linking (if any additional libs are needed)
dependencies = []

# C sources
c_sources = ['src/bibc/sdlprog.c']

# Create an executable that links against the Fortran shared library
executable('sdlprog', sources : c_sources, dependencies : dependencies,
           link_with : [fort_lib], install : true)