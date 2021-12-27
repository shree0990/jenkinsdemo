from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in jenkinsdemo/__init__.py
from jenkinsdemo import __version__ as version

setup(
	name="jenkinsdemo",
	version=version,
	description="Jenkins Demo",
	author="Shree",
	author_email="spawar@dexciss.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
