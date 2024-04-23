project('sdldemo', 'c', 'cpp', 'fortran', default_options : ['default_library=shared'])


ff = meson.get_compiler('fortran')
_intel_fflags = ff.get_supported_arguments(
    '/fp:strict', '/MD', '/names:lowercase', '/assume:underscore',
    '/assume:minus0'
)
add_project_arguments(_intel_fflags, language : 'fortran')
# Fortran source files
fortran_src = ['src/bibfor/func.f90']  # Add your Fortran source files here
# Create a shared library from the Fortran sources
fort_lib = shared_library('myfortlib', fortran_src, install : true, version : '1.0')

# Get .obj file from the Fortran shared library
# Need to find a way to run this during build only (not during configuration)
#fort_obj_path = meson.current_source_dir() / 'buildDir' / 'myfortlib-1.dll.p' / 'src_bibfor_func.f90.obj'
#fort_lib_path = meson.current_source_dir() / 'buildDir' / 'myfortlib.lib'
#lib_program = find_program('LIB', required : false)
#custom_lib = custom_target('myfortlib_custom',
#                           input : fort_obj_path,
#                           output : 'myfortlib.lib',
#                           command : [lib_program, '/OUT:@0@'.format(fort_lib_path), '@INPUT@'],
#                           depends : fort_lib,
#                           depend_files : [fort_obj_path],
#                           build_by_default : true
)
#run_command(
#    [
#        find_program('LIB'),
#        '/OUT:@0@'.format(fort_lib_path),
#        fort_obj_path,
#    ],
#    check : true
#)

# Define the dependencies needed for linking (if any additional libs are needed)
dependencies = [custom_lib]

# C sources
c_sources = ['src/bibc/sdlprog.c']

# Create an executable that links against the Fortran shared library
executable('sdlprog', sources : c_sources, dependencies : dependencies,
           link_with : [fort_lib], install : true)