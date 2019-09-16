import os
from setuptools import setup, find_packages

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "PyStorekeeper",
    version = read(".version"),
    author = "Ytturi",
    author_email = "ytturi@protonmail.com",
    description = (
        "A Python Backup tool for Databases and files. Dump,"
        " compress and unify your data in a single archive."
    ),
    license = "GNU GENERAL PUBLIC LICENSE v3",
    keywords = "backup tool click",
    url = "https://github.com/ytturi/PyStorekeeper",
    packages=find_packages(),
    long_description=read('README.md'),
    install_requires=[
        'click',
    ],
    entry_points='''
        [console_scripts]
        py_archive=PyStorekeeper.py_archive:py_archive
    '''
)
