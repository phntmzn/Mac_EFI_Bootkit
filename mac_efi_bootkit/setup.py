from setuptools import setup, find_packages

setup(
    name="mac_efi_bootkit",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "pyfatfs",
        "pyobjc-framework-DiskArbitration",
        "pyobjc-framework-CoreFoundation",
        "binwalk"
    ],
    entry_points={
        'console_scripts': [
            'bootkit-build=bootkit.builder:main',
            'bootkit-inject=bootkit.injector:main'
        ]
    }
)
