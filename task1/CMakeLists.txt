cmake_minimum_required(VERSION 2.8)

project(CLibrary)
message(info ${CMAKE_CURRENT_SOURCE_DIR})

set(MAIN_SOURCE ${CMAKE_CURRENT_SOURCE_DIR}/C/main.cpp)
set(CMAKE_BINARY_DIR ${CMAKE_SOURCE_DIR}/bin)
set(EXECUTABLE_OUTPUT_PATH ${CMAKE_BINARY_DIR})
set(LIBRARY_OUTPUT_PATH ${CMAKE_SOURCE_DIR}/lib)

add_subdirectory(B)
include_directories(A)

add_executable(C ${MAIN_SOURCE} 
		${CMAKE_CURRENT_SOURCE_DIR}/C/main.h)

add_custom_target(RunGenerator 
COMMENT "generate index.h"
WORKING_DIRECTORY "${CMAKE_CURRENT_SOURCE_DIR}/A"
COMMAND python3 ./preparing.py) 



add_dependencies(C RunGenerator)

target_include_directories(C PRIVATE ${CMAKE_CURRENT_SOURCE_DIR})

target_link_libraries(C ClassLibrary)


