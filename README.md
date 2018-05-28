# code name - Hawthorn ( irl REESTR SERVICE )

  description:

* * *

## Used tech
- RAILS 5
- MONGO DB 3
- SELENIUM
- REDIS


## Packets for reestr

  description:

### query for `/searching`

  description:
```
  searching:
  {
     required id: uint32
     required serarch_type: string
     repeated querys: query
  }
```
```
  query:
  {
     optional kdastr_id: uint32
     optional useg_сadastr: bool
     required region: string
     optional district: string
     optional populated_area: string
     required street_type: string
     required street_name: string
     required house_number: string
     required apartment: string
  }
```
### answer for `/searching`

  description:
```
  answer:
  {
      required id: uint32
      repeated search_uid: uint32
  }
 ```
## structs for reestr base

### struct of search object

  description: maby separate
```
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
```
### struct of the task of request

  description:
```
  task:
  {
      required task_uid: uint32
      repeated realtys: realty
  }
```
  ========================Selenium======================
  login by token, step first:
  url: <https://rosreestr.ru/wps/portal/p/cc_present/ir_egrn>
  token: c5793610-b33b-476f-bebf-53a0f1366383

  =====================================================

## Work with API: How to update status on location

```
curl -v -H "Accept: application/json" -H "Content-type: application/json" -X PATCH -d '{"location":{"status":"готово"}}' http://127.0.0.1:3000/search_queries/5b06edc86135e43b1b91b858/locations/5b06edc86135e43b1b91b859
```

`127.0.0.1` - adress

`3000` - port

`search_queries/5b06edc86135e43b1b91b858/locations/5b06edc86135e43b1b91b859` - url

`5b06edc86135e43b1b91b858` - search_querie id

`5b06edc86135e43b1b91b859` - location id

`{"location":{"status":"готово"}}` - data

`PATCH` - HTTP request method

status may be ``готово`` or `в обработке` .

correct answer is: `{"message":"saved"}`
