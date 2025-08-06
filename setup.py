from setuptools import setup, find_packages

setup(
    name="pytest-htmlx",
    version="0.1.1",
    description="Custom HTML report plugin for Pytest with charts and tables",
    author="Devaraju Garigapati",
    author_email="devaraju.garigapati@gmail.com",
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
        "Framework :: Pytest",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    include_package_data=True,
    zip_safe=False,
)
