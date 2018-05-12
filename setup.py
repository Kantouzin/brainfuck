# coding: utf-8

from setuptools import setup, find_packages

with open("README.md") as f:
    README = f.read()

with open("LICENSE") as f:
    LICENSE = f.read()

setup(
    name="brainfuck",
    version="0.1.0",
    description="Brainfuck interpreter package for Python",
    long_description=README,
    author="Kantouzin",
    author_email="kantouzin0113@gmail.com",
    url="https://github.com/Kantouzin/brainfuck",
    license=LICENSE,
    packages=find_packages(exclude=("tests", "docs")),
    test_suite="tests"
)
