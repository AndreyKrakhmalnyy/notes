Этапы

1. Войти в окружение и установить следующие пакеты:
    # djangorestframework           
    # djangorestframework-jwt       
    # djangorestframework-simplejwt
    
2. Добавить в 'settings.py' следующие параметры:
    #     REST_FRAMEWORK = {
    # 'DEFAULT_AUTHENTICATION_CLASSES': (
    #     'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
    # ),
    # } 
    
3. Установить 'psql' глобально, завести БД, пользователя с паролем, присвоить ему созданную БД, так же установить 
   'psycopg2' в окружение проекта, создать таблицы в проекте с помощью Django ORM (инструкции в файле 'Модели на Джанго.py')
   