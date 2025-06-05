from setuptools import setup, find_packages

setup(
    name="fkeygen",
    version="1.0",
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'fkeygen=fkeygen.__main__:main',
        ],
    },
    author="Nils Thomsen",
    description="CLI-Tool to generate XML for fkeygen",
    long_description="A command-line tool to generate XML files for fkeygen based on a list of E164 numbers.",
    python_requires=">=3.6",
)
