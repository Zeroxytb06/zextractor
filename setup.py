from setuptools import setup, find_packages

clossifiers = [
    'Development Statut :: 5 - Produsction/Stable',
    'Intended Audience :: Education',
    'Operating System :: Microsoft :: Windows :: Windows 10',
    'License :: OSi Approved :: MIT License',
    'Programming Language :: Python :: 3'
]

setup(
name='zextractor',
version='0.0.1',
description='Its a python file for unpackage executable file to pyd file',
long_description=open('README.md').read() + '\n\n' + open('CHANGELOG.txt').read(),
url='',
author='Noam Sghaier Weil',
author_email='leprozerox76@gmail.com',
license='MIT'
classifiers=classifiers,
keywords='extractor',
packages=find_packages()
install_requires=['']
)