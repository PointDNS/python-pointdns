import os
from setuptools import setup, find_packages


def read(filename):
    return open(os.path.join(os.path.dirname(__file__), filename)).read()


setup(
    name = 'pointdns',
    version = '0.1.0',
    license = 'ISC',
    description = 'pointhq.com API client with support for Python 3.x (based on pointhq package)',
    long_description = read('README.md'),
    url = 'https://github.com/copper/python-pointdns',
    author = 'Copper.io',
    author_email = 'accounts@copper.io',
    packages = find_packages(),
    install_requires = [
        'requests',
    ],
    classifiers = [
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: ISC License (ISCL)',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.0',
        'Programming Language :: Python :: 3.1',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Internet :: WWW/HTTP',
    ],
)
