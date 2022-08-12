# Copyright © 2016-2022. Savenkov Igor
# SPDX-License-Identifier: GPL-3.0-or-later

cmake_minimum_required (VERSION 3.22.0)

project (conan_test)

message (STATUS "CMAKE_INCLUDE_PATH: ${CMAKE_INCLUDE_PATH}")
# find_library (FMT_PATH NAMES fmt REQUIRED)
find_package (fmt REQUIRED)

message (STATUS "fmt_FOUND: ${fmt_FOUND}")

add_executable (conan_test main.cpp)
target_link_libraries (conan_test PUBLIC fmt)
target_include_directories (conan_test PUBLIC "${CMAKE_INCLUDE_PATH}")

message (STATUS "CMAKE_INCLUDE_PATH: ${CMAKE_INCLUDE_PATH}")