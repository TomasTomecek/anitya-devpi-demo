#!/usr/bin/python


from setuptools import setup, find_packages


setup(
    name='demo_package',
    version='0.1',
    description="Demo package",
    author='Tomas Tomecek',
    author_email='ttomecek@redhat.com',
    url="https://github.com/TomasTomecek/anitya-devpi-demo",
    license="MIT",
    packages=find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
)
