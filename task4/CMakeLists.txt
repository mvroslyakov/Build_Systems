cmake_minimum_required(VERSION 2.8)
project( TransformImage )
add_custom_target(RunGenerator 
COMMENT "generate array.h"
WORKING_DIRECTORY "${CMAKE_CURRENT_SOURCE_DIR}"
COMMAND python3 ./generate.py)
find_package( OpenCV REQUIRED )
include_directories( ${OpenCV_INCLUDE_DIRS} )
add_executable( TransformImage main.cpp )
add_dependencies(TransformImage RunGenerator)
target_link_libraries(TransformImage ${OpenCV_LIBS} )
target_include_directories(TransformImage PRIVATE ${CMAKE_BINARY_DIR})
