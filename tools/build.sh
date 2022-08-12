conan install -if ../conanfiles -pr:b=default --build=missing ../ &&
conan build   -if ../conanfiles -bf ../build ../                  &&
../build/conan_test
