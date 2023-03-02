# Пульт охраны банка

Данный репозитарий представляет собой веб интерфейс для контроля посещаемости хранилища банка. Сайт работает с удаленной базой данных, для которой необходимо выполнить подключение.

### Как установить

Перед установкой отредактируйте файл `project/.env` в соответсвии с описанием ниже:
```
DB_ENGINE=<DJANGO ENGINE в соответсвии с типом подключаемой БД>
DB_NAME=<Имя подключаемой БД>
DB_USER=<Пользователь БД>
DB_PASSWORD=<Пароль пользователя>
DB_HOST=<Имя или IP сервера с БД>
DB_PORT=<Порт подключения>
SERVER_DEBUG=<TRUE|FALSE по умолчанию False>
AMS_ALLOWED_HOSTS=.localhost,127.0.0.1,[::1]
```
Более подробно о подключение к БД можно узнать по ссылке https://docs.djangoproject.com/en/3.2/ref/databases/ 

Python3 должен быть уже установлен. 
Затем используйте `pip` (или `pip3`, есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```

### Пример запуска

Ниже представлен пример запуска скрипта.

```
django-orm-watching-storage> python manage.py runserver 0.0.0.0:8000
```
### Пример работы
```
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
February 23, 2023 - 17:01:55
Django version 3.2.12, using settings 'project.settings'
Starting development server at http://0.0.0.0:8000/
Quit the server with CONTROL-C.
```
После чего, вы сможете подключится к веб-интерфейсу http://127.0.0.1:8000/

### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).