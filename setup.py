# -*- coding: utf-8 -*-
"""
Setup configuration for kinqimen package.
"""

from setuptools import setup, find_packages
from pathlib import Path

# Read the README file
readme_file = Path(__file__).parent / "README.md"
long_description = readme_file.read_text(encoding="utf-8") if readme_file.exists() else ""

setup(
    name="kinqimen",
    version="0.2.0",
    description="Python Qimen Dunjia (奇門遁甲) library - 堅奇門排盤",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="kentang2017",
    author_email="",
    maintainer="honza",
    url="https://github.com/YOUR_USERNAME/kinqimen",  # Update with your GitHub URL
    package_dir={"": "src"},
    packages=find_packages(where="src", exclude=["tests", "tests.*"]),
    install_requires=[
        "sxtwl>=2.0.6",
        "ephem>=4.2",
        "bidict>=0.23.1",
    ],
    extras_require={
        "streamlit": [
            "pendulum>=2.1.2",
            "streamlit>=1.34.0",
            "streamlit-aggrid>=1.0.5",
        ],
        "advanced": [
            "kinliuren>=0.1.2.9",
            "eacal>=0.0.3",
        ],
        "dev": [
            "pytest>=8.0.0",
            "pytest-cov>=4.0.0",
        ],
    },
    python_requires=">=3.8",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Religion",
    ],
    keywords="qimen dunjia chinese metaphysics divination astrology",
)
