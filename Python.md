---
title: "Install Python"
author: "[Jérôme Desquilbet](mailto:jeromede@fr.ibm.com)"
date: "2020"
lang: "en"
toc: "Table of Contents"
---

# Install Python 3.8.2

[Check the latest source](https://www.python.org/downloads/source/)
-> [3.8.2](https://www.python.org/downloads/release/python-381/)

```
sudo apt update
sudo apt install build-essential zlib1g-dev \
  libncurses5-dev libgdbm-dev \
  libnss3-dev libssl-dev \
  libreadline-dev libffi-dev \
  wget
cd /home/soft
wget https://www.python.org/ftp/python/3.8.2/Python-3.8.2.tgz
tar zxf Python-3.8.2.tgz
cd Python-3.8.2
sudo ./configure --enable-optimizations
sudo make altinstall
which python3
#> /usr/bin/python3
python3 --version
#> Python 3.6.9
which python3.8
#> /usr/local/bin/python3.8
python3.8 --version
#> Python 3.8.2
```

# Initialize environment

```
cd $PROJECT
python3.8 -m venv .
python --version
#> Python 2.7.17
source ./bin/activate
python --version
#> Python 3.8.2
pip install --upgrade pip
#> Successfully installed pip-20.0.2
```

Note: if a venv is not used, then replace `python` by `python3.8` and `pip` by `python3.8 -m pip`

# Initialize application

```
cd $PROJECT
python3.8 -m venv . # only once
source ./bin/activate # each new shell session
mkdir app
touch app/__init__.py
echo 'print("Hello, world")' > app/hello.py
python -m app.hello
#> Hello, world
```


