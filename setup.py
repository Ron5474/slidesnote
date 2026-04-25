from setuptools import setup, find_packages

setup(
    name="slidenotes",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "pdfplumber",
        "openai",
        "python-dotenv",
    ],
    entry_points={
        "console_scripts": [
            "slidenotes=slidenotes.slidenotes:main",
        ],
    },
)
