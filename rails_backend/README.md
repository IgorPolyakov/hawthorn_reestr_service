# HAWTHORN REESTR SERVICE

## Used tech
- RAILS 5
- MONGO DB 3
- SELENIUM
- REDIS

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
