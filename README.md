# AcornsTest

This project requires python 3.7.

## Install Dependencies

This project uses `pipenv`, an environment and dependency manager for Python.
https://pipenv.readthedocs.io

Installation of pipenv requires pip, and can be done by using the command `pip install pipenv` or with `brew install pipenv` for macOS.

Once pipenv is installed, navigate to the cloned project folder, which will contain a `Pipfile` and `Pipfile.lock`, and use the command `pipenv install` to install all dependencies

This project also requires ChromeDriver to be downloaded and its location added to your system PATH
http://chromedriver.chromium.org/getting-started

##Run test
Once pipenv is installed, the test can be launched using the command `pipenv run py.test test_redfin_search.py -s -vv`
