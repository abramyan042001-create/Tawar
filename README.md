# Tawar

Учебный Django-проект со списком товаров на основе `ListView`.

Модель `Product` содержит три поля: артикул, наименование и цена.

## Запуск в Git Bash

```bash
python -m venv .venv
source .venv/Scripts/activate
python -m pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Список товаров: <http://127.0.0.1:8000/>

Добавление товаров через админку: <http://127.0.0.1:8000/admin/>
