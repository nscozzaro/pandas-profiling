from pathlib import Path

from setuptools import setup, find_packages

# Read the contents of README file
source_root = Path(".")
with (source_root / "README.md").open(encoding="utf-8") as f:
    long_description = f.read()

# Read the requirements
with (source_root / "requirements.txt").open(encoding="utf8") as f:
    requirements = f.readlines()

version = "2.5.3"

with (source_root / "src" / "pandas_profiling" / "version.py").open(
    "w", encoding="utf-8"
) as f:
    f.writelines(
        [
            '"""This file is auto-generated by setup.py, please do not alter."""\n',
            f'__version__ = "{version}"\n',
            "",
        ]
    )

setup(
    name="pandas-profiling",
    version=version,
    author="Simon Brugman",
    author_email="pandasprofiling@gmail.com",
    packages=find_packages("src"),
    package_dir={"": "src"},
    url="https://github.com/pandas-profiling/pandas-profiling",
    license="MIT",
    description="Generate profile report for pandas DataFrame",
    python_requires=">=3.6",
    install_requires=requirements,
    extras_require={
        "notebook": ["jupyter-client==6.1.1", "jupyter-core==4.6.3"],
        "app": ["pyqt5==5.14.1"],
    },
    include_package_data=True,
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: MIT License",
        "Environment :: Console",
        "Operating System :: OS Independent",
        "Intended Audience :: Science/Research",
        "Intended Audience :: Developers",
        "Intended Audience :: Financial and Insurance Industry",
        "Intended Audience :: Healthcare Industry",
        "Topic :: Scientific/Engineering",
        "Framework :: IPython",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    keywords="pandas data-science data-analysis python jupyter ipython",
    long_description=long_description,
    long_description_content_type="text/markdown",
    entry_points={
        "console_scripts": [
            "pandas_profiling = pandas_profiling.controller.console:main"
        ]
    },
    options={"bdist_wheel": {"universal": True}},
)
