Для Django REST Framework мы рассмотрим две замечательные библиотеки:

# drf-yasg - которая очень популярна, но в ней используется спецификация OpenAPI 2.0. 
# drf-spectacular - относительно новая библиотека, которая набирает популярность и которая поддерживает спецификацию OpenAPI 3.0.



Подключение 'drf-yasg'.

Устанавливаем библиотеки и локально, и глобально:
    # pip install -U drf-yasg

В файле settings.py подключаем drf_yasg.
    # INSTALLED_APPS = [
    # ...
    # 'django.contrib.staticfiles',  #Необходим для  swagger ui's css/js файлов (По умолчанию включен)
    # 'drf_yasg',
    # ...
    # ]

Затем в файле urls.py.


    # from rest_framework import permissions
    # from django.urls import path, include, re_path
    # from drf_yasg.views import get_schema_view
    # from drf_yasg import openapi

    # schema_view = get_schema_view(
    # openapi.Info(
    #     title="Snippets API",
    #     default_version='v1',
    #     description="Test description",
    #     terms_of_service="https://www.google.com/policies/terms/",
    #     contact=openapi.Contact(email="contact@snippets.local"),
    #     license=openapi.License(name="BSD License"),
    # ),
    # public=True,
    # permission_classes=(permissions.AllowAny,),
    # )

    # urlpatterns = [
    #     ...
    #     re_path(
    #         r'^swagger(?P\.json|\.yaml)$',
    #         schema_view.without_ui(cache_timeout=0),
    #         name='schema-json'
    #     ),
    #     path(
    #         'swagger/',
    #         schema_view.with_ui('swagger', cache_timeout=0),
    #         name='schema-swagger-ui'
    #     ),
    #     path(
    #         'redoc/',
    #         schema_view.with_ui('redoc', cache_timeout=0),
    #         name='schema-redoc'
    #     ),
    # ...
    # ]

В комплекте последняя версия Swagger Ui и Redoc.
Переходя по адресу http://127.0.0.1:8000/swagger/ мы увидим сгенерированную документацию.




Подключение drf-spectacular.
Тут мы можем смело использовать последную версию Django. На сегодняшний день это Django 5. 
Устанавливаем библиотеки и локально, и глобально:
    # pip install drf-spectacular==0.27.0

В файл settings.py добавляем:
    # INSTALLED_APPS = [
    #     .....
    #     'drf_spectacular',
    # ]

    # REST_FRAMEWORK = {
    #     ....
    #     'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
    # }

    # SPECTACULAR_SETTINGS = {
    #     'TITLE': 'Django5 Test Swagger API',
    #     'DESCRIPTION': 'Django5 Test Swagger API description',
    #     'VERSION': '1.0.0',
    #     'SERVE_INCLUDE_SCHEMA': False,
    #     # OTHER SETTINGS
    # }

В файл urls.py добавляем:
    # from drf_spectacular.views import (
    #     SpectacularAPIView,
    #     SpectacularSwaggerView,
    #     SpectacularRedocView
    # )

    # urlpatterns = [
    #     path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    #     # Optional UI:
    #     path(
    #         'api/schema/swagger-ui/',
    #         SpectacularSwaggerView.as_view(url_name='schema'),
    #         name='swagger-ui'
    #     ),
    #     path(
    #         'api/schema/redoc/',
    #         SpectacularRedocView.as_view(url_name='schema'),
    #         name='redoc'
    #     ),
    # ]
    
По маршруту 'api/schema/swagger-ui/' заходим в 'swagger'.

Ссылка: https://gadjimuradov.ru/post/swagger-dlya-django-rest-framework/