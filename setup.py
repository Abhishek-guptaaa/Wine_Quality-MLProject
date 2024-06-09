from setuptools import find_packages, setup
from typing import List
import setuptools



setuptools.setup(
    name="Wine_quality",
    version="0.0.1",
    author="Abhishek",
    author_email="Abhishek18895gupta@gmail.com",
    package_dir={"":"src"},
    packages=setuptools.find_packages(where="src"),

)