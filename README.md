# PYTEST-HTMLX

![PyPI - Version](https://img.shields.io/pypi/v/pytest-htmlx) ![PyPI - Downloads](https://img.shields.io/pypi/dm/pytest-htmlx) ![Python Version](https://img.shields.io/pypi/pyversions/pytest-htmlx) ![License](https://img.shields.io/pypi/l/pytest-htmlx) ![GitHub Issues](https://img.shields.io/github/issues/devarajug/pytest-htmlx) ![GitHub Stars](https://img.shields.io/github/stars/devarajug/pytest-htmlx?style=social)

**pytest-htmlx** is a plugin for [`pytest`](https://docs.pytest.org/) that generate beautiful and customizable HTML reports for your `pytest` test suite with ease.

This package automatically creates a detailed HTML report after running your tests, helping you better visualize test results, errors, and logs.


---

## 📦 Installation

Install it via pip:

```bash
pip install pytest-htmlx
```

## 🚀 Usage
Simply run your tests with the `--htmlx` flag:
```bash
pytest --htmlx
```
This generates a report named `report.html` in the current directory.

To specify a custom report file path:
```bash
pytest --htmlx=results/my-report.html
```

## ✨ Features
- Interactive, modern HTML report
- Summary of passed/failed/skipped tests
- Stack traces and log capture

## 📸 HTML Report Screenshot

Below is an example of what the HTML report looks like:
![HTML Report Example](https://raw.githubusercontent.com/devarajug/pytest-htmlx/main/pytest-htmlx.png)

## 📝 License
This project is licensed under the MIT License.

## 🙌 Contributing
Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

