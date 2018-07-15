#
# Policies
#
if(POLICY CMP0048)
    cmake_policy(SET CMP0048 NEW)
endif()

#
# Project
#
CMAKE_MINIMUM_REQUIRED(VERSION 3.5)
PROJECT(libxml2
    VERSION 2.9.8
    )

#
# Use Conan.io
#
include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()
conan_define_targets()

# TESTS
include (CTest)
    
#============================================================
# CONFIGURE
#
set(VERSION ${PROJECT_VERSION})
set(LIBXML_VERSION_NUMBER 20908)
set(LIBXML_VERSION_EXTRA "")
set(WITH_TRIO 0)
set(WITH_THREADS 0)
set(WITH_THREAD_ALLOC 0)
set(WITH_TREE 1)
set(WITH_OUTPUT 1)
set(WITH_PUSH 1)
set(WITH_READER 1)
set(WITH_PATTERN 1)
set(WITH_WRITER 1)
set(WITH_SAX1 1)
set(WITH_FTP 0)
set(WITH_HTTP 0)
set(WITH_VALID 1)
set(WITH_HTML 1)
set(WITH_LEGACY 0)
set(WITH_C14N 1)
set(WITH_CATALOG 1)
set(WITH_DOCB 1)
set(WITH_XPATH 1)
set(WITH_XPTR 1)
set(WITH_XINCLUDE 1)
set(WITH_ICONV 1) # TODO: Set from conan
set(WITH_ICU 0)
set(WITH_ISO8859X 1)
set(WITH_DEBUG 0)
set(WITH_MEM_DEBUG 0)
set(WITH_RUN_DEBUG 0)
set(WITH_REGEXPS 0)
set(WITH_SCHEMAS 0)
set(WITH_SCHEMATRON 0)
set(WITH_MODULES 0)
set(WITH_ZLIB 0) # TODO: Set from conan
set(WITH_LZMA 0)

CONFIGURE_FILE( ${CMAKE_CURRENT_SOURCE_DIR}/include/libxml/xmlversion.h.in ${CMAKE_CURRENT_BINARY_DIR}/include/libxml/xmlversion.h @ONLY)

#
# DONE CONFIGURE
#==================================================

#============================================================
# CONFIGURE
#

INCLUDE (CheckIncludeFiles)
INCLUDE (CheckFunctionExists)
INCLUDE (CheckLibraryExists) 

# Define if IPV6 support is there
SET(SUPPORT_IP6 OFF)

# Define if getaddrinfo is there
CHECK_FUNCTION_EXISTS(getaddrinfo HAVE_GETADDRINFO)

# Define to 1 if you have the <ansidecl.h> header file.
CHECK_INCLUDE_FILES(ansidecl.h HAVE_ANSIDECL_H)

# Define to 1 if you have the <arpa/inet.h> header file.
CHECK_INCLUDE_FILES(arpa/inet.h HAVE_ARPA_INET_H)

# Define to 1 if you have the <arpa/nameser.h> header file. 
CHECK_INCLUDE_FILES(arpa/nameser.h HAVE_ARPA_NAMESER_H)

# Whether struct sockaddr::__ss_family exists
SET(HAVE_BROKEN_SS_FAMILY OFF)

# Define to 1 if you have the `class' function. 
SET(HAVE_CLASS OFF)

# Define to 1 if you have the <ctype.h> header file. 
CHECK_INCLUDE_FILES(ctype.h HAVE_CTYPE_H)

# Define to 1 if you have the <dirent.h> header file.
CHECK_INCLUDE_FILES(dirent.h HAVE_DIRENT_H)

# Define to 1 if you have the <dlfcn.h> header file.
CHECK_INCLUDE_FILES(dlfcn.h HAVE_DLFCN_H)

# Have dlopen based dso 
CHECK_LIBRARY_EXISTS(dl dlopen "" HAVE_DLOPEN)

# Define to 1 if you have the <dl.h> header file. 
CHECK_INCLUDE_FILES(dl.h HAVE_DL_H)

# Define to 1 if you have the <errno.h> header file.
CHECK_INCLUDE_FILES(errno.h HAVE_ERRNO_H)

# Define to 1 if you have the <fcntl.h> header file.
CHECK_INCLUDE_FILES(fcntl.h HAVE_FCNTL_H)

# Define to 1 if you have the `finite' function. 
CHECK_LIBRARY_EXISTS(m finite "" HAVE_FINITE)

# Define to 1 if you have the <float.h> header file. 
CHECK_INCLUDE_FILES(float.h HAVE_FLOAT_H)

# Define to 1 if you have the `fpclass' function. 
CHECK_FUNCTION_EXISTS(fpclass HAVE_FPCLASS)

# Define to 1 if you have the `fprintf' function. 
CHECK_FUNCTION_EXISTS(fprintf HAVE_FPRINTF)

# Define to 1 if you have the `fp_class' function. 
CHECK_FUNCTION_EXISTS(fp_class HAVE_FP_CLASS)

# Define to 1 if you have the <fp_class.h> header file.
CHECK_INCLUDE_FILES(fp_class.h HAVE_FP_CLASS_H)

# Define to 1 if you have the `ftime' function. 
CHECK_FUNCTION_EXISTS(ftime HAVE_FTIME)

# Define if getaddrinfo is there 
CHECK_FUNCTION_EXISTS(getaddrinfo HAVE_GETADDRINFO)

# Define to 1 if you have the `gettimeofday' function. 
CHECK_FUNCTION_EXISTS(gettimeofday HAVE_GETTIMEOFDAY)

# Define to 1 if you have the <ieeefp.h> header file. 
CHECK_INCLUDE_FILES(ieeefp.h HAVE_IEEEFP_H)

# Define to 1 if you have the <inttypes.h> header file. 
CHECK_INCLUDE_FILES(inttypes.h HAVE_INTTYPES_H)

# Define if math library is there (-lm)
CHECK_LIBRARY_EXISTS(m sin "" HAVE_LIBM)

# Define if isinf is there 
CHECK_FUNCTION_EXISTS(isinf HAVE_ISINF)

# Define if isnan is there 
CHECK_FUNCTION_EXISTS(isnan HAVE_ISNAN)

# Define to 1 if you have the `isnand' function.
CHECK_FUNCTION_EXISTS(isnand HAVE_ISNAND)

# Define if history library is there (-lhistory)
SET(HAVE_LIBHISTORY OFF)

# Define if pthread library is there (-lpthread)
SET(HAVE_LIBPTHREAD OFF)
IF (WITH_THREADS)
CHECK_LIBRARY_EXISTS(pthread pthread_create "" HAVE_LIBPTHREAD)
ENDIF (WITH_THREADS)

# Define if readline library is there (-lreadline) 
SET(HAVE_LIBREADLINE OFF)

# Have compression library
SET(HAVE_LIBZ OFF)
if (WITH_ZLIB)
SET(HAVE_LIBZ ON)
endif()

# Define to 1 if you have the <limits.h> header file.
CHECK_INCLUDE_FILES(limits.h HAVE_LIMITS_H)

# Define to 1 if you have the `localtime' function.
CHECK_FUNCTION_EXISTS(localtime HAVE_LOCALTIME)

# Define to 1 if you have the <malloc.h> header file.
CHECK_INCLUDE_FILES(malloc.h HAVE_MALLOC_H)

# Define to 1 if you have the <math.h> header file.
CHECK_INCLUDE_FILES(math.h HAVE_MATH_H)

# Define to 1 if you have the <memory.h> header file. 
CHECK_INCLUDE_FILES(memory.h HAVE_MEMORY_H)

# Define to 1 if you have the <nan.h> header file. 
CHECK_INCLUDE_FILES(nan.h HAVE_NAN_H)

# Define to 1 if you have the <ndir.h> header file, and it defines `DIR'.
CHECK_INCLUDE_FILES(ndir.h HAVE_NDIR_H)

# Define to 1 if you have the <netdb.h> header file. 
CHECK_INCLUDE_FILES(netdb.h HAVE_NETDB_H)

# Define to 1 if you have the <netinet/in.h> header file.
CHECK_INCLUDE_FILES(netinet/in.h HAVE_NETINET_IN_H)

# Define to 1 if you have the `printf' function.
CHECK_FUNCTION_EXISTS(printf HAVE_PRINTF)

# Define if <pthread.h> is there 
SET(HAVE_PTHREAD_H OFF)
IF (WITH_THREADS)
CHECK_INCLUDE_FILES(pthread.h HAVE_PTHREAD_H)
ENDIF (WITH_THREADS)

# Define to 1 if you have the <resolv.h> header file. 
CHECK_INCLUDE_FILES(resolv.h HAVE_RESOLV_H)

# Have shl_load based dso 
CHECK_FUNCTION_EXISTS(shl_load HAVE_SHLLOAD)

# Define to 1 if you have the `signal' function. 
CHECK_FUNCTION_EXISTS(signal HAVE_SIGNAL)

# Define to 1 if you have the <signal.h> header file. 
CHECK_INCLUDE_FILES(signal.h HAVE_SIGNAL_H)

# Define to 1 if you have the `snprintf' function. 
CHECK_FUNCTION_EXISTS(snprintf HAVE_SNPRINTF)

# Define to 1 if you have the `sprintf' function. 
CHECK_FUNCTION_EXISTS(sprintf HAVE_SPRINTF)

# Define to 1 if you have the `sscanf' function. 
CHECK_FUNCTION_EXISTS(sscanf HAVE_SSCANF)

# Define to 1 if you have the `stat' function.
CHECK_FUNCTION_EXISTS(stat HAVE_STAT)

# Define to 1 if you have the <stdarg.h> header file. 
CHECK_INCLUDE_FILES(stdarg.h HAVE_STDARG_H)

# Define to 1 if you have the <stdint.h> header file.
CHECK_INCLUDE_FILES(stdint.h HAVE_STDINT_H)

# Define to 1 if you have the <stdlib.h> header file. 
CHECK_INCLUDE_FILES(stdlib.h HAVE_STDLIB_H)

# Define to 1 if you have the `strdup' function. 
CHECK_FUNCTION_EXISTS(strdup HAVE_STRDUP)

# Define to 1 if you have the `strerror' function. 
CHECK_FUNCTION_EXISTS(strerror HAVE_STRERROR)

# Define to 1 if you have the `strftime' function. 
CHECK_FUNCTION_EXISTS(strftime HAVE_STRFTIME)

# Define to 1 if you have the <strings.h> header file. 
CHECK_INCLUDE_FILES(strings.h HAVE_STRINGS_H)

# Define to 1 if you have the <string.h> header file.
CHECK_INCLUDE_FILES(string.h HAVE_STRING_H)

# Define to 1 if you have the `strndup' function. 
CHECK_FUNCTION_EXISTS(strndup HAVE_STRNDUP)

# Define to 1 if you have the <sys/dir.h> header file, and it defines `DIR'.
CHECK_INCLUDE_FILES(sys/dir.h HAVE_SYS_DIR_H)

# Define to 1 if you have the <sys/mman.h> header file. 
CHECK_INCLUDE_FILES(sys/mman.h HAVE_SYS_MMAN_H)

# Define to 1 if you have the <sys/ndir.h> header file, and it defines `DIR'.
CHECK_INCLUDE_FILES(sys/ndir.h HAVE_SYS_NDIR_H)

# Define to 1 if you have the <sys/select.h> header file.
CHECK_INCLUDE_FILES(sys/select.h HAVE_SYS_SELECT_H)

# Define to 1 if you have the <sys/socket.h> header file.
CHECK_INCLUDE_FILES(sys/socket.h HAVE_SYS_SOCKET_H)

# Define to 1 if you have the <sys/stat.h> header file. 
CHECK_INCLUDE_FILES(sys/stat.h HAVE_SYS_STAT_H)

# Define to 1 if you have the <sys/timeb.h> header file.
CHECK_INCLUDE_FILES(sys/timeb.h HAVE_SYS_TIMEB_H)

# Define to 1 if you have the <sys/time.h> header file. 
CHECK_INCLUDE_FILES(sys/time.h HAVE_SYS_TIME_H)

# Define to 1 if you have the <sys/types.h> header file. 
CHECK_INCLUDE_FILES(sys/types.h HAVE_SYS_TYPES_H)

# Define to 1 if you have the <time.h> header file. 
CHECK_INCLUDE_FILES(time.h HAVE_TIME_H)

# Define to 1 if you have the <unistd.h> header file. 
CHECK_INCLUDE_FILES(unistd.h HAVE_UNISTD_H)
IF (WIN32)
SET(HAVE_UNISTD_H OFF)
ENDIF (WIN32)

# Whether va_copy() is available
IF (WIN32)
UNSET(HAVE_VA_COPY)
ELSE()
#CHECK_FUNCTION_EXISTS(va_copy HAVE_VA_COPY)
SET(HAVE_VA_COPY 1)
ENDIF()

# Define to 1 if you have the `vfprintf' function. 
CHECK_FUNCTION_EXISTS(vfprintf HAVE_VFPRINTF)

# Define to 1 if you have the `vsnprintf' function. 
CHECK_FUNCTION_EXISTS(vsnprintf HAVE_VSNPRINTF)

# Define to 1 if you have the `vsprintf' function. 
CHECK_FUNCTION_EXISTS(vsprintf HAVE_VSPRINTF)

# Define to 1 if you have the <zlib.h> header file. 
SET(HAVE_ZLIB_H OFF)
if (WITH_ZLIB)
set(HAVE_ZLIB_H ON)
endif()

# Define to 1 if you have the `_stat' function. 
CHECK_FUNCTION_EXISTS(_stat HAVE__STAT)

# Whether __va_copy() is available
IF (WIN32)
UNSET(HAVE___VA_COPY)
ELSE()
CHECK_FUNCTION_EXISTS(__va_copy HAVE___VA_COPY)
ENDIF()


# Name of package 
SET(PACKAGE)

# Define to the address where bug reports for this package should be sent. 
SET(PACKAGE_BUGREPORT)

# Define to the full name of this package. 
SET(PACKAGE_NAME)

# Define to the full name and version of this package. 
SET(PACKAGE_STRING)

# Define to the one symbol short name of this package. 
SET(PACKAGE_TARNAME)

# Define to the version of this package.
SET(PACKAGE_VERSION)

# Define to 1 if the C compiler supports function prototypes. 
SET(PROTOTYPES ON)

# Define to 1 if you have the ANSI C header files. 
SET(STDC_HEADERS ON)

# Support for IPv6 
SET(SUPPORT_IP6 OFF)

# Version number of package 
SET(VERSION)

# Determine what socket length (socklen_t) data type is 
SET(XML_SOCKLEN_T "unsigned int")

# Using the Win32 Socket implementation 
IF (WIN32)
SET(_WINSOCKAPI_ ON)
ENDIF (WIN32)

# Define like PROTOTYPES; this can be used by system headers. 
SET(__PROTOTYPES ON)

# Win32 Std C name mangling work-around
#IF (WIN32)
#SET(snprintf _snprintf)
#ENDIF (WIN32)

# ss_family is not defined here, use __ss_family instead
SET(ss_family)

# Win32 Std C name mangling work-around 
#IF (WIN32)
#SET(vsnprintf _vsnprintf)
#ENDIF (WIN32)


CONFIGURE_FILE( ${CMAKE_CURRENT_SOURCE_DIR}/xml2conf.h.cmake-in ${CMAKE_CURRENT_BINARY_DIR}/include/libxml/xml2conf.h)


#
# DONE CONFIGURE
#==================================================

IF (WITH_ZLIB)
find_package(zlib REQUIRED)
ENDIF (WITH_ZLIB)

IF (WITH_ICONV)
find_package(libiconv REQUIRED)
ENDIF (WITH_ICONV)

INCLUDE_DIRECTORIES(${CMAKE_CURRENT_BINARY_DIR}/include ${CMAKE_CURRENT_SOURCE_DIR}/include )

IF (WIN32)
ADD_DEFINITIONS(-D_CRT_SECURE_NO_WARNINGS)
ENDIF (WIN32)

IF (MSVC)
ADD_DEFINITIONS(/wd4013)
ADD_DEFINITIONS(/wd4018)
ADD_DEFINITIONS(/wd4047)
ADD_DEFINITIONS(/wd4244)
ADD_DEFINITIONS(/wd4267)
ENDIF (MSVC)

ADD_LIBRARY(xml2 
    DOCBparser.c
    HTMLparser.c
    HTMLtree.c
    SAX.c
    SAX2.c
    buf.c
    c14n.c
    catalog.c
    chvalid.c
    debugXML.c
    dict.c
    encoding.c
    entities.c
    error.c
    globals.c
    hash.c
    legacy.c
    list.c
    nanoftp.c
    nanohttp.c
    parser.c
    parserInternals.c
    pattern.c
    relaxng.c
    #rngparser.c
    schematron.c
    threads.c
    tree.c
    trio.c
    trionan.c
    triostr.c
    uri.c
    valid.c
    xinclude.c
    xlink.c
    xmlIO.c
    xmlcatalog.c
    xmllint.c
    xmlmemory.c
    xmlmodule.c
    xmlreader.c
    xmlregexp.c
    xmlsave.c
    xmlschemas.c
    xmlschemastypes.c
    xmlstring.c
    xmlunicode.c
    xmlwriter.c
    xpath.c
    xpointer.c
    xzlib.c
	)
    
IF (WITH_ZLIB)
    TARGET_LINK_LIBRARIES(xml2 zlib)
ENDIF ()
IF (WIN32 AND WITH_ICONV)
    TARGET_LINK_LIBRARIES(xml2 iconv)
ENDIF()
set_target_properties(xml2 PROPERTIES 
  VERSION 2.9.8
  SOVERSION 2.9
)

target_include_directories(xml2
    PUBLIC
        $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/include;${CMAKE_CURRENT_BINARY_DIR}>
        $<INSTALL_INTERFACE:include>
    )

# Tests
function(add_xml2_test TEST_NAME)
    add_executable(${TEST_NAME} ${TEST_NAME}.c)

    # Link
    target_link_libraries(${TEST_NAME} PRIVATE xml2)

    add_test(NAME ${TEST_NAME} COMMAND $<TARGET_FILE:${TEST_NAME}>)
endfunction()

add_executable(testHTML testHTML.c)
target_link_libraries(testHTML PRIVATE xml2)
 
add_executable(runtest runtest.c)
target_link_libraries(runtest PRIVATE xml2)

# Install
install(FILES 
	${CMAKE_CURRENT_SOURCE_DIR}/libxml.h
	DESTINATION include
	)

install(TARGETS xml2
    EXPORT Targets
    LIBRARY DESTINATION lib
    ARCHIVE DESTINATION lib
    RUNTIME DESTINATION bin
    INCLUDES DESTINATION include
    )
    
#
# Export
#
include(CMakePackageConfigHelpers)

write_basic_package_version_file("${CMAKE_CURRENT_BINARY_DIR}/${PROJECT_NAME}ConfigVersion.cmake"
    VERSION ${PROJECT_VERSION}
    COMPATIBILITY SameMajorVersion
    )

configure_file(
    "${CMAKE_CURRENT_SOURCE_DIR}/LibraryConfig.cmake.in"
    "${CMAKE_CURRENT_BINARY_DIR}/${PROJECT_NAME}Config.cmake"
    @ONLY
    )

install(
    FILES
        "${CMAKE_CURRENT_BINARY_DIR}/${PROJECT_NAME}ConfigVersion.cmake"
        "${CMAKE_CURRENT_BINARY_DIR}/${PROJECT_NAME}Config.cmake"
    DESTINATION
        . # Root Directory
    )

install(
    FILES
        "${CMAKE_CURRENT_BINARY_DIR}/${PROJECT_NAME}Config.cmake"
    DESTINATION
        share/cmake/${PROJECT_NAME}/
    )

install(EXPORT Targets
    FILE ${PROJECT_NAME}Targets.cmake
    DESTINATION share/cmake/${PROJECT_NAME}
    )
