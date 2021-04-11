cmake_minimum_required(VERSION 2.8)

project(GenerateIndex)

add_custom_command( 
  OUTPUT index.h
  COMMAND python ${PROJECT_SOURCE_DIR}/preparing.py
  DEPENDS preparing.py
  COMMENT "Generating index.h"
)


