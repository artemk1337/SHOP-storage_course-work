import os
from setuptools import setup


# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(file_name):
    return open(os.path.join(os.path.dirname(__file__), file_name)).read()


setup(
    name="headphones_store",
    version="0.0.1",
    author="Stanislav SK, Artem K",
    author_email="racoononword@gmail.com",
    description="Stores for choosing headphone on archlinux",
    license="MIT",
    keywords="pyqt store",
    url="https://github.com/artemk1337/SHOP-storage_course-work.git",
    packages=['store', 'tests'],
    long_description=read('README.md'),
    classifiers=[
        "Development Status :: 1 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: MIT License",
    ],
)
