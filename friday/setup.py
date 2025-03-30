from setuptools import setup, find_packages

setup(
    name = "friday",
    version = "0.1.0",
    description = "The local AI assistant with voice capabilities and MacOS integration."
    author = "arpan",
    author_email = "arpansethi30@gmail.com",
    packages = find_packages(),
    python_requires = ">=3.9",
    install_requires = [

    ],
    classifiers = [
        "Developed Status :: 3 - Alpha",
        "Inttended Audience :: Developers",
        "License :: OSI Approved :: MIT Liscence",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
)