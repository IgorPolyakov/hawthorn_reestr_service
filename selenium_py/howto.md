# Запрос данных из росреестра
## Пример запроса:
```
python3 query_sender.py -v -http -q $DATA
```
где $DATA : 
```
'[{"id":1,"id_location":1,"kdastr_id":null,"use_kdastr":false,"region":"Томская область","district":null,"populated_area":null,"street_type":"Улица","street_name":"Красноармейская","house_number":"148","apartment":"26"},{"id":1,"id_location":2,"kdastr_id":null,"use_kdastr":false,"region":"Томская область","district":null,"populated_area":null,"street_type":"Улица","street_name":"Красноармейская","house_number":"148","apartment":"29"},{"id":1,"id_location":3,"kdastr_id":null,"use_kdastr":false,"region":"Томская область","district":null,"populated_area":null,"street_type":"Улица","street_name":"Красноармейская","house_number":"148","apartment":"27"}]'
```

## Пример ответа:
В случае успеха хотя бы одной локации в ответ будет высылаться следующая нагрузка (на url по смене статусов):
```
{
  "location": {
    "id": "5b04fd51839be764fecd2a0d",
    "loacation_id": "5b04fd51839be764fecd2a0e",
    "search_uid": "80-39866427",
    "status": "в обработке",
    "date": "27.05.2018 22:07"
  }
}

```
где:
* поле status:
‘в обработке’ - запрос отправлен успешно
‘ошибка’ - что то пошло не так, и данную локацию надо будет перезапросить
* поле  search_uid - по этому номеру в дальнейшем я смогу найти какой файл нужно скачать

В случае если все наебнулось и не дошло даже до запроса, ответ будет высылаться следующая нагрузка (на url "сам придумай какой"):
```
{
    "error_id": 500,
    "error_text": "suffer bitch" 
}
```

## Пожелания
В дальнейшем хотелось бы избавиться от поля "location":
[ 
  {
    "id": "5b04fd51839be764fecd2a0d",
    "loacation_id": "5b04fd51839be764fecd2a0e",
    "search_uid": "80-39866427",
    "status": "в обработке",
    "date": "27.05.2018 22:07"
  },
  {
    "id": "5b04fd51839be764fecd2a0d",
    "loacation_id": "5b04fd51839be764fecd2a0e",
    "search_uid": "80-39866427",
    "status": "в обработке",
    "date": "27.05.2018 22:07"
  }
]