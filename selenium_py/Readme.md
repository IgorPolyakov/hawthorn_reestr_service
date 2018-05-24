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

## zip_loader.py
### Help zip_loader.py
```
Welcome to the help for zip loader v.1.

optional arguments:
  -h, --help            show this help message and exit.
  -v, --virtual         Enabled useg virtual display.
  -t [TOKEN], --token [TOKEN]
                        Set token for loggin on site, it's have default value.
  -q [QUERY], --query [QUERY]
                        As a query, specify the search_uid. uid separate by ','.
  -f, --file            Send result to file bin/result.json.
  -http, --http         Send result to http url.
  -o [OUTPUT], --output [OUTPUT]
                        Set output path for download files, default ~/download.
```

### Useg zip_loader.py
Example: 
```
$ python3 zip_loader.py -f -wb -v -q "80-39089147,80-39089144,80-39089138" -t "c5793610-b33b-476f-bebf-53a0f1366383"

```
Example for test with default token and query: 
```
$ python3 zip_loader.py -f -v

```

### Answer from zip_loader
```
[
    {
        "date_request": dd.mm.yyyy HH:MM,
        "root_path"   : string, // file location on server 
        "search_uid"  : string,
        "status"      : string, // not utf-8
        "zip_url"     : string
    }
]

```

## query_sender.py
### Help query_sender.py
```
Welcome to the help for query sender v.1.

optional arguments:
  -h, --help            show this help message and exit.
  -d  --debug           Disable send statement to server.
  -v, --virtual         Enabled useg virtual display.
  -t [TOKEN], --token [TOKEN]
                        Set token for loggin on site, it's have default value.
  -q [QUERY], --query [QUERY]
                        Query for search. support only json format.
  -f, --file            Send result to file bin/send_query.json.
  -http, --http         Send result to http url.
```

### Useg query_sender.py
Example query: 
```
[
  {
    "id"            : int,
    "kdastr_id"     : string,
    "use_kdastr"    : bool,
    "region"        : string,
    "district"      : string,
    "populated_area": string,
    "street_type"   : string,
    "street_name"   : string,
    "house_number"  : string,
    "apartment"     : string
  }
]

'[{"id":1,"kdastr_id":null,"use_kdastr":false,"region":"Томская область","district":null,"populated_area":null,"street_type":"Улица","street_name":"Красноармейская","house_number":"148","apartment":"10"},{"id":2,"kdastr_id":null,"use_kdastr":false,"region":"Томская область","district":null,"populated_area":null,"street_type":"Улица","street_name":"Красноармейская","house_number":"148","apartment":"6"}]'

```

Example:
```
python3 zip_loader.py -f -v -q '[{"id":1,"kdastr_id":null,"use_kdastr":false,"region":"Томская область","district":null,"populated_area":null,"street_type":"Улица","street_name":"Красноармейская","house_number":"148","apartment":"17"}]'
```

Example for test with default token and query: 
```
$ python3 query_sender.py -f -v

```
or if you don't want send statement to server: 
```
$ python3 query_sender.py -f -v --debug

```

### Answer from query_sender
```
[
  {
    id        : int,
    search_uid: string,
    date      : dd.mm.yyyy HH:MM,
  }
]
```