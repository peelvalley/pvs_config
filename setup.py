import setuptools
from pvs_config.__version__ import __version__
setuptools.setup(
    name='pvs_config',
    version=__version__,
    author="Peel Valley Software",
    author_email="info@peelvalley.com.au",
    description="Simple config base class",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)
