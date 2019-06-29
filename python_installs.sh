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
pip3 install --upgrade pip
pip3 install python-dateutil
pip3 install lxml
pip3 install httplib2
pip3 install psutil
pip3 install beautifulsoup4
pip3 install numpy
pip3 install virtualenv
# pip install pep8 *** renamed to pycodestyle ***
pip3 install ipython
pip3 install scikit-learn
pip3 install mypy
pip3 install selenium
pip3 install twilio
pip3 install python-nmap
pip3 install scrapy
pip3 install twisted
pip3 install validators
pip3 install wheel
pip3 install pandas
pip3 install tweepy
pip3 install pycodestyle
pip3 install wget
