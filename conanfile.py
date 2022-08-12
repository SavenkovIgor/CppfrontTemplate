from conans import ConanFile
from conan.tools.cmake import CMakeToolchain, CMakeDeps, CMake


class TermGraphConan(ConanFile):
    generators = 'CMakeToolchain', 'CMakeDeps'
    settings = 'os', 'arch', 'compiler', 'build_type'

    requires = 'fmt/9.0.0'

    def generate(self):
        deps = CMakeDeps(self)
        deps.generate()

        tc = CMakeToolchain(self)
        tc.generate()

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()
