# Selenium python
---

## Install and prepare to useg (ubuntu 16.04)
before to start:
```
$ sudo apt update && sudo apt dist-upgrade
$ sudo apt install python3-pip firefox
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

## Help
```
Welcome to the help for zip loader v.1.

optional arguments:
  -h, --help            show this help message and exit
  -v, --virtual         Enabled useg virtual display
  -t [TOKEN], --token [TOKEN]
                        Set token for loggin on site, it's have default value.
  -q [QUERY], --query [QUERY]
                        As a query, specify the search_uid. uid separate by ','.
  -f, --file            Send result to file bin/result.json.
  -wb, --websocket      Send result to web socket, do not work.
  -o [OUTPUT], --output [OUTPUT]
                        Set output path for download files, default ~/download
```

## Useg zip_loader.py
Example: 
```
$ python3 zip_loader.py -f -wb -v -q "80-39089147,80-39089144,80-39089138" -t "c5793610-b33b-476f-bebf-53a0f1366383"

```
Example for test with default token and query: 
```
$ python3 zip_loader.py -f -v

```