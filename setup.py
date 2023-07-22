from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in superstart_rides/__init__.py
from superstart_rides import __version__ as version

setup(
	name="superstart_rides",
	version=version,
	description="Frappe Developer Course 2022",
	author="Omar M. K. Shehada",
	author_email="o.shehada@ard.ly",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
