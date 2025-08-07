from setuptools import setup, find_packages
from pathlib import Path

# Load long description from README.md
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text(encoding="utf-8")

setup(
    name="pytest-htmlx",
    version="0.3.1",
    description="Custom HTML report plugin for Pytest with charts and tables",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Devaraju Garigapati",
    author_email="devaraju.garigapati@gmail.com",
    url="https://github.com/devrajug/pytest-htmlx",
    packages=find_packages(),
    install_requires=[
        "pytest",
        "jinja2"
    ],
    python_requires=">=3.7",
    entry_points={
        "pytest11": [
            "htmlx = pytest_htmlx.plugin"
        ]
    },
    classifiers=[
        "Development Status :: 3 - Beta",
        "Framework :: Pytest",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Testing",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    license="MIT",
    include_package_data=True,
    zip_safe=False,
)
