project('sdldemo', 'c', 'cpp', 'fortran', default_options : ['default_library=shared'])

# Fortran source files
fortran_src = ['src/bibfor/func.f90']  # Add your Fortran source files here
# Create a shared library from the Fortran sources
fort_lib = library('myfortlib', fortran_src, install : true, version : '1.0')

# Define the dependencies needed for linking (if any additional libs are needed)
dependencies = []

# C sources
c_sources = ['src/bibc/sdlprog.c']

# Create an executable that links against the Fortran shared library
executable('sdlprog', sources : c_sources, dependencies : dependencies,
           link_with : [fort_lib], install : true)