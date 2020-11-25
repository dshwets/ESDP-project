```
git clone https://gitlab.com/ihinion/applehostel.git

git checkout development

virtualenv -p python3 venv

source venv/bin/activate

pip install -r requirments/local.txt

cp .env.example .env.development
```

Требуется создать базу PostgreSQL

.env.development не находится под версионным
контролем, его надо заполнить соответствующими
значениями для указанных в .env.example переменных

```cd source

./manage.py migrate
```

Если подключение к базе произошло, то все миграции пройдут успешно

Для запуска всех тестов команда:

```./manage.py test```

Команда для запуска приемочных тестов:

```./manage.py behave```
