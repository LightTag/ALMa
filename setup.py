import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ALMa", # Replace with your own username
    version="0.0.2",
    author="Tal Perry",
    author_email="tal@lighttag.io",
    description="Easily track labeled and unlabeled data for active learning",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/lighttag/ALMa",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
