import pathlib

from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.txt").read_text()

setup(
    name = "maggi",
    packages = ["maggi"],
    long_description=README,
    entry_points = {
        "console_scripts": ['maggi = maggi.__main__:main']
        },
    version = "0.1.1",
    description = "Instant images for instant deployment",
    author="Anurag Sarkar",
    author_email="sarkar.anurag@outlook.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    )