from setuptools import find_packages
from setuptools import setup


long_description = open("README.md", encoding="utf-8").read()
description = "GoogleMapsPY aim to scrape data from Google Maps without Google API"

version = "1.0"


setup(
    name="GoogleMapsPY",
    version=version,
    license="MIT License",
    author="Ammar Alkotb",
    author_email="ammar.alkotb@gmail.com",
    description=description,
    packages=find_packages(),
    url="https://github.com/3mora2/GoogleMapsPY",
    project_urls={"Bug Report": "https://github.com/3mora2/GoogleMapsPY/issues/new"},
    install_requires=[
        "requests",
        "numpy",
        "fake-useragent",
    ],
    long_description=long_description,
    long_description_content_type="text/markdown",
    package_dir={"": "."},
    # package_data={"GoogleMapsPY": ["*.md"]},
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Developers",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",

    ],

)