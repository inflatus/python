#!/bin/bash

# pypi installs for Linux
# for Python3
# used with virtualenv

# show python versions
echo "Showing Python versions"
python --version
python3 --version

# upgrade pip3
echo "Upgrading pip"
pip install --upgrade pip

# upgrade pip and install pypi packages
echo "Installing pypi packages"
pip install --upgrade pip
pip install python-dateutil
pip install lxml
pip install httplib2
pip install psutil
pip install beautifulsoup4
pip install numpy
pip install virtualenv
# pip install pep8 *** renamed to pycodestyle ***
pip install ipython
pip install scikit-learn
pip install mypy
pip install selenium
pip install twilio
pip install python-nmap
pip install scrapy
pip install twisted
pip install validators
pip install wheel
pip install pandas
pip install tweepy
pip install pycodestyle
pip install wget
