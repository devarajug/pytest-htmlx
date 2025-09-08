from setuptools import setup, find_packages
from pathlib import Path
import re

root_dir = Path(__file__).parent
long_description = (root_dir / "README.md").read_text(encoding="utf-8")

def get_version():
    init_file = root_dir / "pytest_htmlx" / "__init__.py"
    content = init_file.read_text()
    match = re.search(r'__version__ = "(.+)"', content)
    if not match:
        raise RuntimeError("Unable to find version string in __init__.py")
    return match.group(1)


setup(
    name="pytest-htmlx",
    version=get_version(),
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
        "Development Status :: 4 - Beta",
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
