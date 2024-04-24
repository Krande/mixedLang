project(MiniF C Fortran)

if (CMAKE_Fortran_COMPILER MATCHES "flang")
    message(STATUS "Using flang-new compiler")
else ()
    SET(CMAKE_Fortran_FLAGS "/iface:mixed_str_len_arg /nologo /fpp /fixed /dll /MD ${CMAKE_Fortran_FLAGS}")
endif ()

SET(fi_SOURCES
        src/medstructelement.f
)

ADD_LIBRARY(_fi OBJECT ${fi_SOURCES})

SET(medfort_wrap_SOURCES
        $<TARGET_OBJECTS:_fi>
)

SET(_export_group "medfileTargets")

ADD_LIBRARY(medfwrap SHARED ${medfort_wrap_SOURCES})
SET_TARGET_PROPERTIES(medfwrap PROPERTIES
        SOVERSION 11
        VERSION 11.1.1
        WINDOWS_EXPORT_ALL_SYMBOLS ON
        POSITION_INDEPENDENT_CODE ON
)

INSTALL(TARGETS medfwrap
        EXPORT ${_export_group}
        RUNTIME DESTINATION bin
        ARCHIVE DESTINATION lib${LIB_SUFFIX})

#SET(INSTALL_CMAKE_CONFIG_DIR cmake)
#INSTALL(EXPORT medfileTargets DESTINATION "${INSTALL_CMAKE_CONFIG_DIR}" FILE ${PROJECT_NAME}Targets.cmake)