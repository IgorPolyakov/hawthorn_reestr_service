# Запрос данных из росреестра
## Пример запроса:
```
python3 query_sender.py -v -http -q $DATA
```
где $DATA :
```
'[
   {
      "id":1,
      "location_id":1,
      "kdastr_id":null,
      "use_kdastr":false,
      "region":"Томская область",
      "district":null,
      "populated_area":null,
      "street_type":"Улица",
      "street_name":"Красноармейская",
      "house_number":"148",
      "apartment":"26"
   },
   {
      "id":1,
      "location_id":2,
      "kdastr_id":null,
      "use_kdastr":false,
      "region":"Томская область",
      "district":null,
      "populated_area":null,
      "street_type":"Улица",
      "street_name":"Красноармейская",
      "house_number":"148",
      "apartment":"29"
   }
]'
```

## Пример ответа:
В случае успеха хотя бы одной локации в ответ будет высылаться следующая нагрузка (на url по смене статусов):
```
{
  "location": {
    "id": "5b04fd51839be764fecd2a0d",
    "location_id": "5b04fd51839be764fecd2a0e",
    "search_uid": "80-39089153",
    "date": "27.05.2018 22:07",
    "date_request": null,
    "status": "в обработке",
    "zip_url": null,
    "root_path": null
  }
}

```
где:
* поле status:
‘в обработке’ - запрос отправлен успешно
[deprecated] ‘ошибка’ - что то пошло не так, и данную локацию надо будет перезапросить,
* поле  search_uid - по этому номеру в дальнейшем я смогу найти какой файл нужно скачать

В случае если все наебнулось и не дошло даже до запроса, ответ будет высылаться следующая нагрузка (на url "сам придумай какой"):
```
{
    "error_id": 500,
    "error_text": "suffer bitch"
}
```

## [deprecated] Пожелания - in review
В дальнейшем хотелось бы избавиться от поля "location":
```
[
  {
    "id": "5b04fd51839be764fecd2a0d",
    "location_id": "5b04fd51839be764fecd2a0e",
    "search_uid": "80-39866427",
    "status": "в обработке",
    "date": "27.05.2018 22:07"
  },
  {
    "id": "5b04fd51839be764fecd2a0d",
    "location_id": "5b04fd51839be764fecd2a0e",
    "search_uid": "80-39866427",
    "status": "в обработке",
    "date": "27.05.2018 22:07"
  }
  ```
]

# Загрузка zip из росреестра
## Пример запроса:
```
python3 zip_loader.py -v -http -q $DATA
```
где $DATA :
```
[{"id":1,"location_id":1,"search_uid":"80-39089153"}]
```

## Пример ответа:
В случае успеха хотя бы одной локации в ответ будет высылаться следующая нагрузка (на url по смене статусов):
```
{
  "location": {
    "id": "5b04fd51839be764fecd2a0d",
    "location_id": "5b04fd51839be764fecd2a0e",
    "search_uid": "80-39089153",
    "date": null,
    "date_request": "28.05.2018 22:07",
    "status": "готово",
    "zip_url": "http//",
    "root_path": "/home/user/2i.zip"
  }
}
```
где:
* поле status:
‘в обработке’ - запрос отправлен успешно
[deprecated] ‘ошибка’ - что то пошло не так, и данную локацию надо будет перезапросить,

В случае если все наебнулось и не дошло даже до запроса, ответ будет высылаться следующая нагрузка (на url "сам придумай какой"):
```
{
    "error_id": 500,
    "error_text": "suffer bitch"
}
```

## Пожелания
смотри выше
