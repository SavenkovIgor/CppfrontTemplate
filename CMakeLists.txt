# Copyright © 2016-2022. Savenkov Igor
# SPDX-License-Identifier: GPL-3.0-or-later

cmake_minimum_required (VERSION 3.22.0)

project (cpp_template)

find_package (fmt REQUIRED)

add_executable (cpp_template src/main.cpp)

target_link_libraries (cpp_template PUBLIC fmt::fmt)

