from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in custom_workspaces/__init__.py
from custom_workspaces import __version__ as version

setup(
	name="custom_workspaces",
	version=version,
	description="A custom Frappe app to auto-generate workspaces",
	author="Custom App Author",
	author_email="author@example.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
