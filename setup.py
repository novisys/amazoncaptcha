# -*- coding: utf-8 -*-

import setuptools
import os

#--------------------------------------------------------------------------------------------------------------

def get_about_data():
    """Retrieve metadata about the package from the version file."""
    here = os.path.abspath(os.path.dirname(__file__))
    version_file_path = os.path.join(here, 'amazoncaptcha', '__version__.py')

    if not os.path.exists(version_file_path):
        raise FileNotFoundError(f"Version file not found: {version_file_path}")

    with open(version_file_path, 'r', encoding='utf-8') as f:
        file_data = [line.strip().replace('\'', '').split(' = ') for line in f.readlines()]
        about = {key: value for key, value in file_data}

    return about

def read_readme(logo_end_line=14):
    """Extracts the logo from README file before pushing to PyPi."""
    if not os.path.exists('README.md'):
        raise FileNotFoundError("README.md file not found")

    with open('README.md', 'r', encoding='utf-8') as fh:
        long_description = ''.join(fh.readlines()[logo_end_line:])

    return long_description

classifiers = [
    "Programming Language :: Python",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.9",
    "Programming Language :: Python :: 3.10",
    "Programming Language :: Python :: 3.11",
    "Programming Language :: Python :: 3.12",
    "Programming Language :: Python :: 3.13",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
    "Development Status :: 5 - Production/Stable",
    "Natural Language :: English",
    "Intended Audience :: Developers",
    "Intended Audience :: Education",
    "Intended Audience :: Information Technology",
]

requires = [
    "pillow >= 9.0.1,< 12.0",
    "requests ~= 2.27.1"
]

about = get_about_data()

#--------------------------------------------------------------------------------------------------------------

setuptools.setup(
    name=about['__title__'],
    version=about['__version__'],
    description=about['__description__'],
    packages=['amazoncaptcha'],
    py_modules=['devtools', 'exceptions', 'solver', 'utils'],
    include_package_data=True,
    package_data={'': ['*.json'], 'amazoncaptcha': ['training_data/*.*']},
    classifiers=classifiers,
    long_description=read_readme(),
    long_description_content_type="text/markdown",
    install_requires=requires,
    author=about['__author__'],
    author_email=about['__author_email__'],
    url=about['__url__'],
    project_urls={
        'Documentation': 'https://amazoncaptcha.readthedocs.io/en/latest/',
        'Source': about['__url__'],
    },
)

#--------------------------------------------------------------------------------------------------------------
