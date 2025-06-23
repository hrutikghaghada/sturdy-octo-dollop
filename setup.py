import wheel  # noqa
from setuptools import find_packages, setup

setup(
    name="packaging-demo",
    version="0.0.0",
    packages=find_packages(),
    # package metadata
    author="Author Name",
    author_email="your_email@example.com",
    description="A small example package",
    license="MIT",
    install_requires=[
        "numpy",
    ],
)
