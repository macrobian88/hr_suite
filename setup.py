from setuptools import setup, find_packages

with open("requirements.txt") as f:
    install_requires = f.read().strip().split("\n")

# get version from __version__ variable in hr_suite/__init__.py
from hr_suite import __version__ as version

setup(
    name="hr_suite",
    version=version,
    description="Complete HR Management Solution with ERPNext",
    author="Your Company",
    author_email="support@yourcompany.com",
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=install_requires
)