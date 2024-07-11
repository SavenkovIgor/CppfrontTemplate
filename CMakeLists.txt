cmake_minimum_required (VERSION 3.30)

project (cpp_template)

# cppfront setup
include (FetchContent)

FetchContent_Declare (
    cppfront
    GIT_REPOSITORY https://github.com/modern-cmake/cppfront.git
    GIT_TAG        main
)

FetchContent_MakeAvailable (cppfront)

find_package (fmt REQUIRED)

add_executable (cpp_template src/main.cpp2)

set_property (TARGET cpp_template PROPERTY CXX_STANDARD 20)

target_link_libraries (cpp_template PUBLIC fmt::fmt)
