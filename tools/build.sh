git clean -df                                                     &&
conan remove -f '*'                                               &&
conan install -pr:b=default -if ../conanfiles --build=missing ../ &&
conan build -if ../conanfiles -bf ../ ../                         &&
../conan_test
