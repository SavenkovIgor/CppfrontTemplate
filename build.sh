git clean -df                                 &&
conan remove -f '*'                           &&
conan install -pr:b=default --build=missing . &&
conan build .                                 &&
./conan_test
