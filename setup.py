import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="research-base",
    version="0.0.1",
    author="Jae Yong Lee",
    author_email="lee896@illinois.edu",
    description="Research Base Repository",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/leejaeyong7/research-base",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
