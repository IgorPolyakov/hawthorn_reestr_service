# Selenium python
---

## Install and prepare to useg (ubuntu 16.04)
before to start:
```
$ sudo apt update && sudo apt dist-upgrade
$ sudo apt install python3-pip
```

virtual display:
```
$ sudo apt-get install xvfb
$ sudo pip3 install pyvirtualdisplay
```

selenium:
```sh
$ pip3 install selenium
$ mkdir thirdparty
$ cd thirdparty
$ wget https://github.com/mozilla/geckodriver/releases/download/v0.20.1/geckodriver-v0.20.1-linux64.tar.gz
$ tar -xvf geckodriver-v0.20.1-linux64.tar.gz
$ export PATH=$PATH:$PWD
```


ssh-keygen -t rsa -b 4096 -C "neverhooda@gmail.com"