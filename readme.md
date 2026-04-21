This repository attempts to clean up the barely readable content of exclusive articles on “The Information” in the HTML code.

It allows anyone who does not have a subscription, to read the first few sentences and get an overview of the article.


# Depencies:

## Windows:
- Google Chrome (for requesting)
- choco
- git
- python3 (py.exe)
- pip
- selenium
- BeautifulSoup


# Verify the Depencies:

### Python:

Open cmd and type in
`py --version` 
this should output `Python 3.x`

If not, you can download and install python [here](https://www.python.org/downloads/)


### pip

type `py -m pip --version`

The output should look like this 
`pip 24.3.1 from pip 24.3.1 from C:\Users\USERNAME\Path\to\python\Python312\site-packages\pip (python 3.12)`

If not, download and install pip. [Here's an example](https://www.activestate.com/resources/quick-reads/how-to-install-pip-on-windows/)


### choco

type in `choco --version`
This should output the version

If not, you can download and install choco [here](https://chocolatey.org/install)


### Git

type in `git --version`
This should output the Git version

If not, you can download and install Git via `choco install git` (This needs elevated privileges )


## Install the modules with

This also needs elevated privileges to successfully install it, type in:

`py -m pip install selenium --force` 

`py -m pip install BeautifulSoup --force`



# How to use it

Open your cmd, go into the folder you want the files to be downloaded in and type:

`git clone https://github.com/haasele/paywallremover-theinformation-exclusive.git`

`cd paywallremover-theinformation-exclusive`

`py remover.py`


Now just enter the Link of the article from `theinformation.com` and the Script will extract the Article from the Sites Sourcecode.
