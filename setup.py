from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    install_requires=[
        "aiohttp==3.6.2",
        "async-timeout==3.0.1",
        "attrs==19.3.0",
        "beautifulsoup4==4.9.0",
        "bs4==0.0.1",
        "chardet==3.0.4",
        "chromedriver-autoinstaller==0.2.0",
        "datetime==4.3",
        "discord==1.0.1",
        "discord.py==1.3.3",
        "idna==2.9",
        "multidict==4.7.5",
        "pytz==2019.3",
        "selenium==4.0.0a5",
        "soupsieve==2.0",
        "urllib3==1.25.8",
        "websockets==8.1",
        "yarl==1.4.2",
        "zope.interface==5.1.0",
    ],
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
