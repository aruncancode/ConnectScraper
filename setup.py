from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="connect_scraper",
    version="0.0.1",
    author="urwrstkn8mare + aruncancode",
    description="An API that webscrapes Connect DET.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/aruncancode/connect-api",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
    ],
    python_requires="~=3.6",
)
