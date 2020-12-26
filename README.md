Данная документация предполагает локальное разворачивание проекта в системе Ubuntu версии 18.04 и выше, 
а также основанных на ней (Linux Mint Cinnamon и т.д.)

#### Техническое задание
Необходимо реализовать CRM-приложение (система управления взаимоотношениями с клиентами) для компании Apple Hostel.

#### Бэкенд
Приложение написано на языке Python на основе фреймворка Django версии 2.2.13

#### Фронтенд
Для фронтенда использован Bootstrap 4.5

#### Системные библиотеки  
Зависимости виртуального окружения требуют наличия в системе библиотек libjpeg-dev и zlib1g-dev, 
при необходимости устанавливаются следующей командой

```sh 
$ sudo apt-get install libjpeg-dev zlib1g-dev
```

Из других особо заслуживающих упоминания библиотек и сервисов в приложении используется selenium для приемочных тестов. 
Для его корректной работы должен быть установлен ChromeDriver необходимой версии:  
https://sites.google.com/a/chromium.org/chromedriver/downloads

#### Создание базы данных

Проект использует базу данных PostgreSQL версии 10-11

Документация PostgreSQL, раздел установка https://www.postgresql.org/docs/10/installation.html

Вход в систему управления базами данных
```sh
$ sudo -u postgres psql
```

Создание нового пользователя (выбрать желаемые значения вместо user_name и 'password')
```
create user user_name with password 'password';
alter role user_name set client_encoding to 'utf8';
alter role user_name set default_transaction_isolation to 'read committed';
alter role user_name set timezone to 'UTC';
```

Создание новой бд под названием apple_db
```
create database apple_db owner user_name;
```

Выход из СУБД
```
\q
```

#### Установка redis
В проекте также используется высокопроизводительная БД redis.

Документация по установке и настройке, включая демонизацию и запуск redis-сервера https://redis.io/topics/quickstart

Запуск сервера в фоновом режиме
```sh
$ redis-server --daemonize yes
```

Закрытие сервера
```sh
$ redis-cli shutdown
```

#### Разворачивание проекта
Клонирование проекта, создание и активация виртуального окружения, установка зависимостей в виртуальное окружение
```sh
$ git clone https://gitlab.com/ihinion/applehostel.git
$ cd applehostel
$ git checkout development
$ virtualenv -p python3.7 venv
$ source venv/bin/activate
$ pip install -r requirements/local.txt
$ cp .env.example .env.development
```

Файл с переменными для настроек проекта .env.development не находится под версионным контролем. 
Его надо заполнить соответствующими значениями для указанных в .env.example переменных

```sh 
$ nano .env.development
```

- APP_ENV=your_envoirment (dev для девелопмента)
- DB_NAME=your_database_name (название базы данных, например apple_db)
- DB_HOST=your_database_host (хост бд, например localhost)
- DB_PORT=your_database_port (порт бд, например 5432)
- DB_USER=your_database_user (имя пользователя бд)
- DB_PASSWORD=your_database_password (пароль пользователя бд)
- POSTGRES_DB=your_database_name_for_postgress_container
- POSTGRES_USER=your_username_for_postgress_container
- POSTGRES_PASSWORD=your_password_for_postgress_container
- SECRET_KEY=your_django_secretkey (секретный ключ Django)
- DEBUG=your_debug_mode (дебаг-режим, True/False)
- ALLOWED_HOSTS=*
- REDIS_HOST=your_redis_host (хост редиса, по умолчанию 127.0.0.1)
- REDIS_PORT=your_redis_port (порт редиса, по умолчанию 679)
- REDIS_DB=your_redis_database (название базы данных редиса, от 0 до 15, по умолчанию 0)

Проведение миграций
```sh
$ cd source
$ python manage.py migrate
```

Если подключение к базе произошло, то все миграции пройдут успешно

#### Права доступа
Ни одна часть приложения не видна незалогиненному пользователю. При попытке неаутентифированного пользователя получить доступ происходит редирект на страницу логина. При попытке доступа неавторизованного пользователя происходит редирект на страницу 403 ошибки (доступ запрещен)

#### Тесты
Большая часть приложения покрыта модульными и приемочными тестами. Следующие команды следует выполнять в директории `source` при активированном виртуальном окружении

Команда для запуска модульных тестов
```sh
$ python manage.py test
```

Команда для запуска приемочных тестов
```sh
$ python manage.py behave
```