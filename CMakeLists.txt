# Copyright © 2016-2022. Savenkov Igor
# SPDX-License-Identifier: GPL-3.0-or-later

cmake_minimum_required (VERSION 3.22.0)

project (cpp_template)

find_package (fmt REQUIRED)
find_package (cppfront REQUIRED)

set (cppfront_CMD "${cppfront_PACKAGE_FOLDER_RELEASE}/bin/cppfront")

# Run before build cpp2 file
add_custom_command (
    OUTPUT ${CMAKE_CURRENT_SOURCE_DIR}/src/main.cpp
    COMMAND ${cppfront_CMD} ${CMAKE_CURRENT_SOURCE_DIR}/src/main.cpp2
    DEPENDS ${CMAKE_CURRENT_SOURCE_DIR}/src/main.cpp2
    COMMENT "Run cppfront on cpp2 file"
)

add_executable (cpp_template src/main.cpp)

set_property (TARGET cpp_template PROPERTY CXX_STANDARD 20)

target_link_libraries (cpp_template PUBLIC fmt::fmt)
target_link_libraries (cpp_template PUBLIC cppfront::cppfront)
