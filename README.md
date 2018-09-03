# code name - Hawthorn ( irl REESTR SERVICE )

  description:

* * *

## Used tech

-   RAILS
-   MONGODB
-   SELENIUM

## Packets for reestr

  description:

### query for `/searching`

  description:

      searching:
      {
         required id: string
         required title: string
         repeated querys: query
      }

      query:
      {
         optional kdastr_id: string
         optional use_kdastr: bool
         required region: string
         optional district: string
         optional populated_area: string
         required street_type: string
         required street_name: string
         required house_number: string
         required apartment: string
      }

### answer for `/searching`

  description:

      answer:
      {
          required id: uint32
          repeated search_uid: uint32
      }

## structs for reestr base

### struct of search object

  description: maby separate

      realty :
      {
          required search_uid: uint32
          required date_request: yyyy-dd-MMThh:mm:ss (or some like this)
          required date_response: yyyy-dd-MMThh:mm:ss (or some like this)
          optional kdastr_id: uint32
          required region: string
          optional district: string
          optional populated_area: string
          required street_type: string
          required street_name: string
          required house_number: string
          required apartment: string
          required zip_url:string
      }

### struct of the task of request

  description:

      task:
      {
          required task_uid: uint32
          repeated realtys: realty
      }

      ========================Selenium======================
      login by token, step first:
      url: <https://rosreestr.ru/wps/portal/p/cc_present/ir_egrn>
      token: c5793610-b33b-476f-bebf-53a0f1366383

      =====================================================

## Work with API

### How to update status on **location**

    curl -v -H "Accept: application/json" -H "Content-type: application/json" -H "X-User-Email: your@somemail.com" -H "X-User-Token: eoJ5d2Zd2sBA6gsah2xx" -X PATCH -d '{"location":{"status":"готово"}}' http://127.0.0.1:3000/search_queries/5b156b496135e45f9be745f6/locations/5b06edc86135e43b1b91b859

-   for update use `PATCH` HTTP request method
-   status may be `готово` or `в обработке`.
-   api user email `X-User-Email`
-   api user token `X-User-Token`
-   correct answer is: `{"message":"saved"}`
-   `127.0.0.1` - adress
-   `3000` - port
-   `search_queries/5b156b496135e45f9be745f6/locations/5b06edc86135e43b1b91b859` - url
-   `5b156b496135e45f9be745f6` - search_querie id
-   `5b06edc86135e43b1b91b859` - location id

data:

    {
       "location" : {
          "status" : "готово"
       }
    }

### How to update **search_query**

    curl -v -H "Accept: application/json" -H "Content-type: application/json" -H "X-User-Email: your@somemail.com" -H "X-User-Token: eoJ5d2Zd2sBA6gsah2xx" -X PATCH -d '{ "search_query" : { "locations_attributes" : { "0" : { "kdastr_id" : "70:21:0200026:2953", "use_kdastr" : "true" }, "1" : { "kdastr_id" : "70:21:0200026:2954", "use_kdastr" : "true" } } } }' http://127.0.0.1:3000/search_queries/5b16b7a66135e42b1a04a6f8

-   for update use `PATCH` HTTP request method
-   api user email `X-User-Email`
-   api user token `X-User-Token`
-   correct answer is: `{"message":"saved"}`
-   url `http://127.0.0.1:3000/search_queries/5b16b7a66135e42b1a04a6f8`
-   `5b16b7a66135e42b1a04a6f8` - search_query_id

data:

    {
       "search_query" : {
          "locations_attributes" : {
             "0" : {
                "kdastr_id" : "70:21:0200026:2953",
                "use_kdastr" : "true"
             },
             "1" : {
                "use_kdastr" : "true",
                "kdastr_id" : "70:21:0200026:2954"
             }
          }
       }
    }

### How to create new **search_query**

    curl -v -H "Accept: application/json" -H "Content-type: application/json" -H "X-User-Email: your@somemail.com" -H "X-User-Token: eoJ5d2Zd2sBA6gsah2xx" POST -d '{ "search_query" : { "title" : "some_title", "locations_attributes" : { "0" : { "kdastr_id" : "70:21:0200026:2953", "use_kdastr" : "true" }, "1" : { "kdastr_id" : "70:21:0200026:2954", "use_kdastr" : "true" } } } }' http://127.0.0.1:3000/search_queries.json

-   for create use `POST` HTTP request method
-   api user email `X-User-Email`
-   api user token `X-User-Token`
-   url `http://127.0.0.1:3000/search_queries.json`
-   correct answer is: `{"message":"saved"}`

data:

    {
       "search_query" : {
          "title" : "some_title",
          "locations_attributes" : {
             "0" : {
                "kdastr_id" : "70:21:0200026:2953",
                "use_kdastr" : "true"
             },
             "1" : {
                "use_kdastr" : "true",
                "kdastr_id" : "70:21:0200026:2954"
             }
          }
       }
    }

### How to update a **location**

    curl -v -H "Accept: application/json" -H "Content-type: application/json" -H "X-User-Email: your@somemail.com" -H "X-User-Token: eoJ5d2Zd2sBA6gsah2_x" -X PATCH -d '{ "location" : { "house_number": "3953" } }' http://127.0.0.1:3000/search_queries/5b61ee256135e40de56514b1/locations/5b61ee256135e40de56514af.json

data:

    {
       "location" : {
            "house_number" : "3953"
          }
    }

## Deploy on **production server**

### install dependency

first install `ruby`

then run

    gem install mina

### for deploy last commit on server run:

    mina deploy

## Changelog

All changes you can see [here](CHANGELOG.md).
