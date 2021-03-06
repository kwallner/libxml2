from conans import ConanFile, CMake

class libxml2Conan(ConanFile):
    name = "libxml2"
    version = "2.9.8"
    branch = "master"
    generators = "cmake"
    settings =  "os", "compiler", "arch", "build_type"
    options = {"shared": [True, False], "fPIC": [True, False]}
    default_options = "shared=False", "fPIC=True"
    url = "http://github.com/kwallner/libxml2"
    scm = { "type": "git", "url": "auto", "revision": "auto" }

    def config_options(self):
        del self.settings.compiler.libcxx

    def requirements(self):
        if self.settings.os == "Windows":
            self.requires("libiconv/1.15.0@%s/%s" % ("kwallner", "testing"))

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()
        # cmake.test() # FIXME
        cmake.install()

    def package_info(self):
        self.env_info.libxml2_DIR = self.package_folder
