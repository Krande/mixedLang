//
// Created by ofskrand on 30.04.2024.
//

#ifndef _MAIN_
#define _MAIN_ main

void initAsterModules() {
    PyImport_AppendInittab( "aster_core", PyInit_aster_core );
    PyImport_AppendInittab( "aster", PyInit_aster );

    /* Module définissant des opérations sur les objets fonction_sdaster */
    PyImport_AppendInittab( "aster_fonctions", PyInit_aster_fonctions );
#ifdef ASTER_HAVE_MED
    PyImport_AppendInittab( "med_aster", PyInit_med_aster );
#endif
}

int _MAIN_( int argc, char **argv ) {
    int ierr;

    initAsterModules();

    wchar_t **wargv = PyMem_Malloc( sizeof( wchar_t * ) * argc );
    int i;
    for ( i = 0; i < argc; i++ )
        wargv[i] = Py_DecodeLocale( argv[i], NULL );

    ierr = Py_Main( argc, wargv );
    return ierr;
}