#!/usr/bin/env python

from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

requirements = ["fastjsonschema", "jsonschema"]
test_requirements = ["pytest", "flake8"]
setup_requirements = ["pytest-runner", "setuptools>=40.5.0"]

extras = {"test": test_requirements}

setup(
    name="event",
    version="0.0.03",
    author="Mozilla",
    description="A custom event module.",
    long_description=long_description,
    url="https://github.com/mozilla/mozdef_aws_event_framework_template",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)",
        "Operating System :: OS Independent",
    ],
    install_requires=requirements,
    license="Mozilla Public License 2.0",
    include_package_data=True,
    packages=find_packages(include=["event", "event/zoom", "event/zoom/schemas", "event/aws"]),
    package_data={
        "event": [
            "*.py",
            "zoom/*.py",
            "zoom/schemas/*.py",
            "aws/*.py"
        ]
    },
    setup_requires=setup_requirements,
    tests_require=test_requirements,
    extras_require=extras,
    test_suite="tests",
    zip_safe=True,
)
