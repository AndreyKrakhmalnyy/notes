Для полноценной и удобной проверки работы JWT авторизации перед подключением её в проект рекомендуется подключить
    'DRF' и 'OpenAPI/Swagger-UI'.

Этапы:

1. Установить пакеты ниже и локально в проект и глобально:
    # djangorestframework              
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
    #     'rest_framework_simplejwt',
    # ]

4. в 'urls.py' добавляем:
    
    # path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'), - получение токена, вводятся данные суперпользователя
    # path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'), - обновление refresh токена
    # path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'), 
    

Теперь для получения какой-либо информации будет необходимо сначала перейти на 'api/token/', ввести данные зарегистрированного
    пользователя в админке, после чего будут получены 'refresh' и 'access' токены, далее перейти в 'OpenAPI/Swagger-UI'
    и ввести токен (значок замочка) после чего можно будет выполнять соответствующие GET, POST и тд запросы.
    
   
   
Ссылка на документацию: https://proproprogs.ru/django/drf-delaem-avtorizaciyu-po-jwt-tokenam
   