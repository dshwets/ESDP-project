```
git clone https://gitlab.com/ihinion/applehostel.git apple_hostel

cd apple_hostel

git checkout development

virtualenv -p python3.7 venv

source venv/bin/activate

 pip install -r requirments/local.txt

cp .env.example .env.development
```

Требуется создать базу PostgreSQL

.env.development не находится под версионным
контролем, его надо заполнить соответствующими
значениями для указанных в .env.example переменных

cd source

./manage.py migrate
```
Если подключение к базе произошло, то все миграции пройдут успешно
