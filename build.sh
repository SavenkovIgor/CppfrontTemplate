git clean -df                      &&
conan remove -f '*'                &&
conan install --build=missing .    &&
cmake --preset=release -G Ninja ./ &&
cmake --build ./                   &&
./conan_test
