cmake_minimum_required(VERSION 2.8)
project(ClassLibrary)

set(SOURCE_LIB lib.h lib.cpp)
add_library(ClassLibrary SHARED ${SOURCE_LIB})

