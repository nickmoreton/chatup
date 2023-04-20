import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="wordpress-json-fetch",
    version="0.1.0",
    author="Nick Moreton",
    author_email="nickmoreton@me.com",
    description="A cli to fetch json from a wordpress api",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/nickmoreton/chatup",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        "click", "requests"
    ],
    extras_require={
        "dev": [
            "pytest>=6.1.2",
            "flake8>=3.8.3",
            "coverage>=5.3",
        ]
    },
)
