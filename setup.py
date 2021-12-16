from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in sa_stack/__init__.py
from sa_stack import __version__ as version

setup(
	name="sa_stack",
	version=version,
	description="A stack of South Africa documents prices and places.",
	author="RC Keogh",
	author_email="it@theyouthmall.co.za",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
