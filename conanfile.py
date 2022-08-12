from conans import ConanFile
from conan.tools.cmake import CMakeToolchain, CMakeDeps #, CMake


class TermGraphConan(ConanFile):

    generators = 'CMakeToolchain' #, 'CMakeDeps'
    settings = 'os', 'arch', 'compiler', 'build_type'

    requires = 'fmt/9.0.0'

    def generate(self):
        tc = CMakeToolchain(self)
        tc.generate()

        deps = CMakeDeps(self)
        deps.generate()

    # def build(self):
        # cmake = CMake(self)
        # cmake.configure()
        # cmake.build()


# from conans import ConanFile
# from conan.tools.cmake import CMakeToolchain, CMakeDeps, CMake


# class TermGraphConan(ConanFile):

#     generators = 'CMakeToolchain', 'CMakeDeps'
#     settings = 'os', 'arch', 'compiler', 'build_type'

#     requires = 'outcome/2.2.3'

#     def generate(self):
#         tc = CMakeToolchain(self)
#         tc.generate()

#         deps = CMakeDeps(self)
#         deps.generate()

#     def build(self):
#         cmake = CMake(self)
#         cmake.configure()
#         cmake.build()
