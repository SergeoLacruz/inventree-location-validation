# -*- coding: utf-8 -*-

import setuptools
from inventree_location_validation.version import PLUGIN_VERSION


with open('README.md', encoding='utf-8') as f:
    long_description = f.read()

setuptools.setup(
    name="inventree-location-validation",
    version=PLUGIN_VERSION,
    author="Michael Buchmann",
    author_email="michael@buchmann.ruhr",
    description="Validates if stockitem movement is valid",
    long_description="long_description",
    long_description_content_type='text/markdown',
    keywords="inventree stocklocation stockitem inventory",
    url="https://github.com/SergeoLacruz/inventree-location-validation",
    license="MIT",
    packages=setuptools.find_packages(),
    install_requires=[
    ],
    setup_requires=[
        "wheel",
        "twine",
    ],
    python_requires=">=3.6",
    entry_points={
        "inventree_plugins": [
            "LocationValidatorPlugin = inventree_location_validation.location_plugin:LocationValidatorPlugin"
        ]
    },
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "Framework :: InvenTree",
    ],
)
