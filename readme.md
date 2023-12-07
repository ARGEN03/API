## Настройки

Прежде чем начать использовать API, убедитесь, что ваше окружение настроено правильно. Вы можете использовать виртуальное окружение для изоляции зависимостей

### Активируйте виртуальное окружение:

Для Windows:
 ```bash 
.\venv\Scripts\activate
```

Для Linux:
```bash
source venv/bin/activate
```

### Установите зависимости:
вы можете скачать библиотеки с файла requirements.txt

```bash  
pip install -r requirements.txt
```
## Создайте база данных library

# Функциональность
### GET - запрос, выводит все данные
```bash
http://localhost:8000/get_books/  
```

### PUT - запрос, выводит обновление
```bash
http://localhost:8000/update_book/booK_id/
```

### POST - запрос, создает запись
```bash
http://localhost:8000/create_book/
```

### DELETE - запрос, удаляет заппись
```bash
http://localhost:8000/delete_item/book_id/
```
