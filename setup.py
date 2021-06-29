#!/usr/bin/env python3

from setuptools import setup

setup(
    name="turtlerevenge",
    version="0.0.1",
    packages=["turtlerevenge"],
    entry_points={
        "console_scripts": [
            "turtlerevenge = turtlerevenge.__main__:main"
        ]
    },
)
