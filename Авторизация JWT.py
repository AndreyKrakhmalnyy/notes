Этапы:

1. Войти в окружение и установить следующие пакеты:
    # djangorestframework           
    # djangorestframework-jwt       
    # djangorestframework-simplejwt
    
2. в 'settings.py' вставляем следующие строки:
    
    #     REST_FRAMEWORK = {
    # 'DEFAULT_AUTHENTICATION_CLASSES': (
    #     'rest_framework_simplejwt.authentication.JWTAuthentication',
    # ),
    # }

    # SIMPLE_JWT = {
    #     "ACCESS_TOKEN_LIFETIME": timedelta(minutes=5),
    #     "REFRESH_TOKEN_LIFETIME": timedelta(days=1),
    #     "ROTATE_REFRESH_TOKENS": False,
    #     "BLACKLIST_AFTER_ROTATION": False,
    #     "UPDATE_LAST_LOGIN": False,

    #     "ALGORITHM": "HS256",
    #     "SIGNING_KEY": SECRET_KEY,
    #     "VERIFYING_KEY": "",
    #     "AUDIENCE": None,
    #     "ISSUER": None,
    #     "JSON_ENCODER": None,
    #     "JWK_URL": None,
    #     "LEEWAY": 0,

    #     "AUTH_HEADER_TYPES": ("Bearer",),
    #     "AUTH_HEADER_NAME": "HTTP_AUTHORIZATION",
    #     "USER_ID_FIELD": "id",
    #     "USER_ID_CLAIM": "user_id",
    #     "USER_AUTHENTICATION_RULE": "rest_framework_simplejwt.authentication.default_user_authentication_rule",

    #     "AUTH_TOKEN_CLASSES": ("rest_framework_simplejwt.tokens.AccessToken",),
    #     "TOKEN_TYPE_CLAIM": "token_type",
    #     "TOKEN_USER_CLASS": "rest_framework_simplejwt.models.TokenUser",

    #     "JTI_CLAIM": "jti",

    #     "SLIDING_TOKEN_REFRESH_EXP_CLAIM": "refresh_exp",
    #     "SLIDING_TOKEN_LIFETIME": timedelta(minutes=5),
    #     "SLIDING_TOKEN_REFRESH_LIFETIME": timedelta(days=1),

    #     "TOKEN_OBTAIN_SERIALIZER": "rest_framework_simplejwt.serializers.TokenObtainPairSerializer",
    #     "TOKEN_REFRESH_SERIALIZER": "rest_framework_simplejwt.serializers.TokenRefreshSerializer",
    #     "TOKEN_VERIFY_SERIALIZER": "rest_framework_simplejwt.serializers.TokenVerifySerializer",
    #     "TOKEN_BLACKLIST_SERIALIZER": "rest_framework_simplejwt.serializers.TokenBlacklistSerializer",
    #     "SLIDING_TOKEN_OBTAIN_SERIALIZER": "rest_framework_simplejwt.serializers.TokenObtainSlidingSerializer",
    #     "SLIDING_TOKEN_REFRESH_SERIALIZER": "rest_framework_simplejwt.serializers.TokenRefreshSlidingSerializer",
    # }
    
3. в 'INSTALLED_APPS' добавляем:
    
    #     INSTALLED_APPS = [
    #     'django.contrib.admin',
    #     'django.contrib.auth',
    #     'django.contrib.contenttypes',
    #     'django.contrib.sessions',
    #     'django.contrib.messages',
    #     'django.contrib.staticfiles',
    #     'rest_framework_simplejwt',
    # ]

4. в 'urls.py' добавляем:
    
    # path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    
5. установить 'psql' глобально, завести БД, пользователя с паролем, присвоить ему созданную БД, так же установить 
    'psycopg2' в окружение проекта, создать таблицы в проекте с помощью Django ORM (инструкции в файле 'Модели на Джанго.py').
    
6. при возникновении ошибок на фоне миграций можно воспользоваться командой в статье 
    https://vivazzi.pro/ru/it/programming-error-relation-already-exists/.

7. для создания кастомных таблиц используются классы "AbstractBaseUser, PermissionsMixin", для 
    менеджера пользователей используется класс "BaseUserManager", для этого делаем 
    импорт как указано ниже:
        # from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
    
   
   
Ссылка на документацию: https://django-rest-framework-simplejwt.readthedocs.io/en/latest/getting_started.html
   