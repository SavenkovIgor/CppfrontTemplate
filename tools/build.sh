git clean -df                                           &&
conan remove -f '*'                                     &&
conan install -pr:b=default -if ../ --build=missing ../ &&
conan build -bf ../ ../                                 &&
../conan_test
