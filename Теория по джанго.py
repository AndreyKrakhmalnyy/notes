# _____________________________________________________________________________________________________________________________________
# Синтаксис использования циклов в django
# _____________________________________________________________________________________________________________________________________ 
    Для использования цикла в 'views.py' и в 'template.html' необходимо:
        1. Импортировать модуль 'render':
            # from django.shortcuts import render
        2. Использовать параметр 'context' в 'views.py' и конструкцию {% for _ из _ %} для обозначения
        начала цикла, затем {{% endfor %}} для закрытия цикла, например:
            
            
            /* views.py */
            # from django.shortcuts import render

            # TEAM = [
            #     {'name': 'Yoda', 'position': 'CEO'},
            #     {'name': 'Obi-Wan Kenobi', 'position': 'Senior Developer'},
            #     {'name': 'Anakin Skywalker', 'position': 'Junior Developer'},
            #     {'name': 'Jar Jar Binks', 'position': 'Trainee'},


            # def about(request):
            #     return render(request, 'шаблон.html', context={'TEAM': TEAM})
            
            /* template.py */
            # <h3>Список имён сотрудников и их грейдов</h3>
            #   {% for person in TEAM %}
            #   <li>{{ person.name }} - {{ person.position }}</li>
            #   {% endfor %}
        
        
        
        
# _____________________________________________________________________________________________________________________________________         
Декоратор '@require_http_methods'
# _____________________________________________________________________________________________________________________________________ 
        
    Для того, чтобы явно показать функции-обработчику в 'views.py' какие запросы нужно обрабатывать, а иначе возвращать
    ответ 'MethodNotAllowed (код 405)', используется декоратор '@require_http_methods' совместно с его импортом ниже:
        
            # from django.views.decorators.http import require_http_methods

            # @require_http_methods(['GET', 'POST'])
            # def login(request):
            #       <...> - здесь описание работы запросов 'GET' и 'POST'
            
    То есть если 'request' != 'GET' или 'request' != 'POST', то вернётся 'MethodNotAllowed (код 405)'.
            
# _____________________________________________________________________________________________________________________________________         
Создание django-проекта
# _____________________________________________________________________________________________________________________________________ 

    Создаём папку, в которой будет находиться проект (либо через 'Создать папку', либо mkdir <имя-папки>), 
    далее создаём окружение (virtualenv):
        # python3 -m virtualenv <имя-проекта>

    В окружении вводим команду для его активации:
        # source bin/activate
    
    Устанавливаем 'django':
        # pip install django
        
    Перейдя в папку с проектом в терминале создаём главный django-проект:
        # pip install startproject <имя-проекта>
        
    Далее находясь на одном уровне с главным django-проектом вводим команду:
        # pip install startapp <имя-проекта>
        
    
# _____________________________________________________________________________________________________________________________________         
Структура django-проекта
# _____________________________________________________________________________________________________________________________________     

       project/ - # Папка с проектом
        │
        ├── my_env/ # Виртуальное окружение
        │
        ├── manage.py
        │
        ├── core или main/  # Главное приложение проекта
        │   ├── __init__.py
        │   ├── settings.py
        │   ├── urls.py
        │   └── wsgi.py
        │   
        ├── first_app/  # Приложение 1 
        │    ├── templates/
        │    │    └── first_app/
        │    │          ├── base.html
        │    │          └── index.html
        │    ├── static/
        │    │    └── first_app/
        │    │          ├── css/
        │    │          └── img/
        │    └── migrations/
        │        ├── __init__.py
        │        └── __pycache__    
        │
        ├── second_app/  # Приложение 2 
        │    ├── templates/
        │    │    └── second_app/
        │    │          ├── base.html
        │    │          └── index.html
        │    ├── static/
        │    │    └── second_app/
        │    │          ├── css/
        │    │          └── img/
        │    └── migrations/
        │        ├── __init__.py
        │        └── __pycache__      
        │
        ├── requirements.txt # содержит список всех зависимостей Python, необходимых для запуска вашего веб-приложения (pip install -r requirements.txt)
        |
        ├── README.md
        |    
        └── ...
        
        
# _____________________________________________________________________________________________________________________________________         
Именование приложений в django-проекте
# _____________________________________________________________________________________________________________________________________     

    К примеру помимо 'main' или 'core' на сайте должны отображаться основные страницы сайта (pages), возможность регистрации (authentication),
    возможность бронирования заказа (orders) с оплатой (payment), то рекомендуется сделать так:
        
    project/ - # Папка с проектом
        │
        ├── my_env/ # Виртуальное окружение
        │
        ├── manage.py
        │
        ├── core/  # Главное приложение проекта с настройками
        │   ├── __init__.py
        │   ├── settings.py
        │   ├── urls.py
        │   └── wsgi.py
        │   
        ├── pages/  # Приложение со страницами сайта 
        │    ├── templates/
        │    │    └── first_app/
        │    │          ├── base.html
        │    │          └── index.html
        │    └── static/
        │        └── first_app/
        │              ├── css/
        │              └── img/
        |
        ├── authorization/  # Авторизация
        │    ├── templates/
        │    │    └── second_app/
        │    │          ├── base.html
        │    │          └── index.html
        │    ├── static/
        │    │    └── second_app/
        │    │          ├── css/
        │    │          └── img/   
        │    │
        │    ├── migrations/
        │    │    ├── __init__.py
        │    │    └── __pycache__  
        │    │
        │    └── другие файлы.py  
        │    
        ├── orders/  # Заказы
        │    ├── templates/
        │    │    └── second_app/
        │    │          ├── base.html
        │    │          └── index.html
        │    ├── static/
        │    │    └── second_app/
        │    │          ├── css/
        │    │          └── img/   
        │    │
        │    ├── migrations/
        │    │    ├── __init__.py
        │    │    └── __pycache__
        │    │
        │    └── другие файлы.py 
        |
        ├── payment/  # Оплата
        │    ├── templates/
        │    │    └── second_app/
        │    │          ├── base.html
        │    │          └── index.html
        │    ├── static/
        │    │    └── second_app/
        │    │          ├── css/
        │    │          └── img/   
        │    │
        │    ├── migrations/
        │    │    ├── __init__.py
        │    │    └── __pycache__   
        │    │
        │    └── и другие основные файлы (views, models и тд).py 
        |
        ├── requirements.txt 
        |
        ├── README.md
        |    
        └── ...
        
        
        
        
# _____________________________________________________________________________________________________________________________________         
Создание 'requirements.txt
# _____________________________________________________________________________________________________________________________________     

    Для создания файла зависимостей "requirements.txt" в корневой папке проекта в терминале прописываем:

        # pip freeze > requirements.txt
        
    Если установки зависимостей проекта из файла "requirements.txt" необходимо ввести команду:
    
        # pip install -r requirements.txt

    При удалении какой-либо зависимости необходимо его также убрать из списка в "requirements.txt".
    

Отображение шаблонов и статических файлов
    Для этого необходимо прежде всего доп. приложение (например, 'pages') связать с основным приложением (например, 'core'). 
    К примеру, в приложении 'pages' есть папка с шаблонами (полный путь pages/templates/pages/base.html), а также папка 'static' 
    со стилями (полный путь pages/static/pages/css/main.css), для отображения делаем следующее:
    
        1. в 'base.html' в 'head' указываем ссылку на файл стилей 'main.css':
            # {% load static %} <link href="{% static 'pages/css/main.css' %}" rel="stylesheet">
        2. в 'views.py' указываем ссылку на 'base.html':
            # from django.shortcuts import render

            # def home(request):
            #     return render(request, 'pages/base.html')
        3. создаём в 'pages' файл 'urls.py' и добавляем 
            # from django.urls import path - копируем из 'core/urls.py'
            # from . import views - из текущей директории импортируем 'views.py'

            # urlpatterns = [
            #     path('', views.home) - указываем ссылку на имя метода, который возвращает шаблон 'base.html'
            # ]
        4. в 'core/urls.py' добавляем путь к 'pages/urls.py'
            # from django.contrib import admin
            # from django.urls import path, include 

            #         urlpatterns = [
            # path('pages/', include('pages.urls')), - ссылаемся на 'pages/urls.py' в котором прописаны все пути приложения
            # path('admin/', admin.site.urls),
            #         ]
        5. также добавляем в 'core/settings.py' само приложение в список:
            INSTALLED_APPS = [
                'django.contrib.admin',
                'django.contrib.auth',
                'django.contrib.contenttypes',
                'django.contrib.sessions',
                'django.contrib.messages',
                'django.contrib.staticfiles',
                'pages.apps.PagesConfig', - параметр '.apps.PagesConfig' это ссылка на конфиг в 'pages/apps.py'
            ]