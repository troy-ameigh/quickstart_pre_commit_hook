from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals
from setuptools import find_packages
from setuptools import setup

with open("requirements.txt", encoding="utf-8") as f:
    REQUIRED = f.read().splitlines()

setup(
    name='pre-commit-hooks-quickstart',
    description='A pre-commit hook to check your QuickStarts Template Files',
    url='https://github.com/troy-ameigh/pre-commit-hook-quickstart',
    version='0.1',

    author='Troy Ameigh',
    author_email='ameighta@amazon.com',

    platforms='linux',
    classifiers=[
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Operating System :: POSIX :: Linux",
        "Operating System :: MacOS :: MacOS X ",
    ],
    entry_points={
        'console_scripts': [
            'quickstart_check = quickstart_check:main',
        ],
    },

    packages=find_packages('.'),
    install_requires=REQUIRED,
)