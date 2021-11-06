import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="SchemdrawDIN",
    version="0.0.1",
    author="Christian Siegl",
    author_email="christian.siegl@gmail.com",
    description="Provide element styles of Deutsches Institut für Normung for schemdraw.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/csiegl182/MPLayout",
    project_urls={
        "Bug Tracker": "https://github.com/csiegl182/SchemdrawDIN/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.7",
)