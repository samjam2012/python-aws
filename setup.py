from setuptools import setup

# Used in pypi.org as the README description of your package
with open("README.md", 'r') as f:
    long_description = f.read()

setup(
        name='python-aws',
        version='1.0.0',
        description='test app for deploying python to aws',
        author='Sam Jamal',
        author_email='',
        license="",
        url="",
        packages=['python_aws'],
        entry_points={
                'console_scripts': [
                    'run=python_aws.main:main',
                ],
        },
        #install_requires=['foo', 'bar'], # Install External packages 'foo' and 'bar' as dependencies
        long_description=long_description
)
