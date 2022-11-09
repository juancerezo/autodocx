from setuptools import setup, find_namespace_packages

setup(
    name="autodocx",
    description="A tool for automating Microsoft Word Documents generation"
    version="0.1.0",
    packages=find_namespace_packages(exclude=["build", "build.*"]),
    install_requires=["click==8.1.3", "python-docx==0.8.11", "openpyxl==3.0.10"],
    entry_points={
        "console_scripts": [
            "autodocx = autodocx:cli",
        ],
    },
)
