import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="bwcrypt-pkg-buchingerwilhelmi",
    version="0.0.1",
    author="Justin Guese",
    author_email="guese.justin@gmail.com",
    description="A package to have coherent encryption and decryption in the BW Cloud",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/BuchingerWilhelmiApp/pip-encryption-module",
    project_urls={
        "Bug Tracker": "https://github.com/BuchingerWilhelmiApp/pip-encryption-module/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.8",
)