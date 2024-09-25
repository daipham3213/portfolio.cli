import setuptools

setuptools.setup(
    command_options={
        "nuitka": {
            # boolean option, e.g. if you cared for C compilation commands
            "--show-scons": True,
            # options without value, e.g. enforce using Clang
            "--clang": None,
            # options with single values, e.g. enable a plugin of Nuitka
            "--enable-plugin": "pyside2",
            # options with several values, e.g. avoiding including modules
            "--nofollow-import-to": ["*.tests", "*.distutils"],
            "--standalone": None,
            "--onefile": None,
            " --assume-yes-for-downloads": None,
        },
    },
)
