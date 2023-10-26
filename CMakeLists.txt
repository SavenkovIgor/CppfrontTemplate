cmake_minimum_required (VERSION 3.22.0)

project (cpp_template)

find_package (fmt REQUIRED)
find_package (cppfront REQUIRED)

set (cppfront_CMD "${cppfront_PACKAGE_FOLDER_RELEASE}/bin/cppfront")

# Set variable for generated files directory
set(GEN_DIR ${CMAKE_BINARY_DIR}/gen)

# Make directory for generated files
file(MAKE_DIRECTORY ${GEN_DIR})

set(CPP2_SOURCES
    src/main.cpp2
)

# Function to generate a cpp file from a cpp2 file using cppfront
function (generate_cpp cpp2_file cpp_file_path)
    get_filename_component(cpp_file ${cpp2_file} NAME_WE)
    set(cpp_file "${cpp_file}.cpp")
    add_custom_command (
        COMMAND ${cppfront_CMD} ${cpp2_file} -o ${GEN_DIR}/${cpp_file}
        DEPENDS ${cpp2_file}
        OUTPUT ${GEN_DIR}/${cpp_file}
        COMMENT "Cppfront: ${cpp2_file} -> ${GEN_DIR}/${cpp_file}"
    )
    set(${cpp_file_path} ${GEN_DIR}/${cpp_file} PARENT_SCOPE)
endfunction()

# Call the function to generate main.cpp
generate_cpp("${CMAKE_CURRENT_SOURCE_DIR}/src/main.cpp2" "RES_PATH")

message(STATUS "RES_PATH: ${RES_PATH}")

add_custom_target (cpp2 ALL DEPENDS ${CMAKE_BINARY_DIR}/gen/main.cpp)

add_executable (cpp_template ${CMAKE_BINARY_DIR}/gen/main.cpp)

add_dependencies (cpp_template cpp2)

set_property (TARGET cpp_template PROPERTY CXX_STANDARD 20)

target_link_libraries (cpp_template PUBLIC fmt::fmt)
target_link_libraries (cpp_template PUBLIC cppfront::cppfront)
