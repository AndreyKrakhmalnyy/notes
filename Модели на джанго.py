Для отображения таблиц БД в админке необходимо выполнить следующие шаги:
   
   1. установить 'psql':
         # sudo apt install postgresql

   2. войти в psql:
         # sudo -u postgres psql
   3. создать пользователя с паролем:
         #  CREATE USER <имя пользователя> WITH PASSWORD <пароль>;
   4. создать БД:
         # CREATE DATEBASE <название БД>
   5. устанавливаем кодировку символов клиента
         # ALTER ROLE <имя пользователя> SET client encoding TO 'utf8';
         
      # Это означает, что пользователь будет использовать кодировку utf8 для связи с базой данных, что позволит 
      # обрабатывать символы на различных языках, включая не латинские символы.
   
   6. устанавливаем уровень изоляции транзакций (определяет уровень доступа и видимости данных в транзакциях):
         # ALTER ROLE <имя пользователя> SET default transaction isolation TO 'read committed';
   
   7. устанавливаем временную зону UTC для роли пользователя
         # ALTER ROLE <имя пользователя> SET timezone TO 'UTC';
   
      # пользователь будет использовать координированное всемирное время (UTC) в качестве своей временной зоны по умолчанию.
      
   8. предоставляем пользователю все привилегии (права доступа) к базе данных:
         # GRANT ALL PRIVILEGES ON DATABASE <название БД> TO <имя пользователя>;
   
   9. создаём таблицы в 'models.py' и регистрируем их в 'admin.py':
         9.1 Примеры для 'models.py'
      
            # from django.db import models

            # class Users(models.Model): 
            #    id = models.AutoField(primary_key=True)
            #    first_name = models.CharField(max_length=100)
            #    email = models.CharField(max_length=50)
            #    created_at = models.DateTimeField(auto_now=True)
         
         9.2 Пример для 'admin.py'

            # from django.contrib import admin
            # from .models import Users

            # admin.site.register(Users)
      
      10. в главной папке проекта в 'settings.py' в графе 'DATABASES' вставляем строки:

            #    DATABASES = {
            #    'default': {
            #       'ENGINE': 'django.db.backends.postgresql',
            #       'NAME': 'users_data',
            #       'USER': 'mainroleproject',
            #       'PASSWORD': 'abemuH44!',
            #       'HOST': 'localhost',   # Адрес вашего сервера по умолчанию 
            #       'PORT': '5432',        # Порт, на котором запущен PostgreSQL сервер
            #    }
            # }

      11. в виртуальном окружении установить модуль для подключения в БД:
            # pip install psycopg2

      12. создаём и проводим миграции, создаём админа:
            # python3 manage.py makemigrations
            # python3 manage.py migrate
            # pytho3 manage.py createsuperuser
      


Основные типы полей в Django ORM

   # 1. CharField:
      - max_length: Максимальная длина строки.

   # 2. TextField:
      - max_length: Максимальная длина текста.

   # 3. IntegerField:
      - default: Значение по умолчанию.
      - blank: Позволяет пустые значения.
      - null: Разрешает значения NULL.

   # 4. FloatField:
      - default: Значение по умолчанию.
      - blank: Позволяет пустые значения.
      - null: Разрешает значения NULL.

   # 5. BooleanField:
      - default: Значение по умолчанию.

   # 6. DateField:
      - auto_now: Используется для автоматического обновления даты при каждом сохранении модели.
      - auto_now_add: Устанавливает значение только при создании.

   # 7. DateTimeField:
      - auto_now: Автоматически обновляет значение при каждом сохранении модели.
      - auto_now_add: Устанавливает значение только при создании.
      - default: Значение по умолчанию.
      - verbose_name: Человекочитаемое имя поля.

   # 8. TimeField:
      - auto_now: Используется для автоматического обновления времени при каждом сохранении модели.
      - auto_now_add: Устанавливает значение только при создании.
      - blank: Позволяет пустые значения.
      - null: Разрешает значения NULL.

   9. EmailField:
      - max_length: Максимальная длина email-адреса.

   # 10. ImageField и FileField:
      - upload_to: Директория для загрузки файлов.
      - max_length: Максимальная длина имени файла.

   # 11. DecimalField:
      - max_digits: Максимальное количество цифр в числе.
      - decimal_places: Количество десятичных знаков.
      
   # 12. ForeignKey, ManyToManyField и OneToOneField:
      - to: Указывает на модель, с которой создается связь.
      
      #  12.1 ForeignKey (ManyToOne):
         Пример: Предположим, у вас есть модели Author (Автор) и Book (Книга). Один автор может написать несколько книг, 
         но каждая книга принадлежит только одному автору. В этом случае используется связь "многие к одному" (many-to-one). 
         Таким образом, каждая книга ссылается на одного автора.

      #  12.2 OneToOneField (OneToOne):
         Пример: Предположим, у вас есть модели Person (Человек) и Passport (Паспорт). У каждого человека есть только 
         один паспорт, и каждый паспорт относится только к одному человеку. Здесь используется связь "один к одному" (one-to-one).

      #  12.3 ManyToManyField (ManyToMany):
         Пример: Предположим, у вас есть модели Student (Студент) и Course (Курс). Каждый студент может изучать несколько курсов, 
         и каждый курс может быть изучен несколькими студентами. В этом случае используется связь "многие ко многим" (many-to-many).

      # ПРИМЕЧАНИЕ 
         Также важно указывать параметр 'on_delete=models.CASCADE', пример использования: есть таблица 'Users'
         и таблица 'BirthPlace', соответственно при удалении пользователя должна быть также удалена информация
         о его месте рождения, то есть в таблице 'Users' нужно указать связь 'OneToOne' с параметром 
         'on_delete=models.CASCADE'.