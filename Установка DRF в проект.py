Устанавливаем как локально в окружение, так и глобально:
    # pip install djangorestframework
    # pip install markdown       
    # pip install django-filter  

Или клонируйте проект с github:
    # git clone https://github.com/encode/django-rest-framework
    
Добавьте 'rest_framework'в свою 'INSTALLED_APPS' настройку:
    # INSTALLED_APPS = [
    #     ...
    #     'rest_framework',
    # ]
    
Если вы собираетесь использовать API с возможностью просмотра, вам, вероятно, также захочется добавить представления входа 
и выхода из системы REST framework. Добавьте следующее в свой корневой urls.py файл:
    # urlpatterns = [
    #     ...
    #     path('api-auth/', include('rest_framework.urls'))
    # ]

Пример.
Давайте рассмотрим краткий пример использования платформы REST для создания простого API на основе модели.

Мы создадим API для чтения и записи для доступа к информации о пользователях нашего проекта.

Любые глобальные настройки API платформы REST хранятся в одном словаре конфигурации с именем REST_FRAMEWORK. 
Начните с добавления следующего в ваш settings.py модуль:
    # REST_FRAMEWORK = {
    #     # Use Django's standard `django.contrib.auth` permissions,
    #     # or allow read-only access for unauthenticated users.
    #     'DEFAULT_PERMISSION_CLASSES': [
    #         'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    #     ]
    # }
    
Теперь мы готовы создать наш API, проект 'project', приложение 'api', модель 'User' уже создана в 'project/api/models.py':
    #________ project/api/serializers.py ________#
    # from rest_framework import serializers
    # from .models import User
    
    # class UserSerializer(serializers.ModelSerializer):
    #     class Meta:
    #         model = User
    #         fields = ['url', 'username', 'email', 'is_staff']

    
    #________ project/api/views.py ________#
    # from rest_framework import viewsets
    # from api.models import User
    # from api.serializers import UserSerializer
    
    # class UserViewSet(viewsets.ModelViewSet):
    #     queryset = User.objects.all()
    #     serializer_class = UserSerializer


    #________ project/urls.py ________#   
    # from django.contrib import admin
    # from django.urls import path, include
    # from rest_framework import routers
    # from api.views import UserViewSet

    # router = routers.DefaultRouter()
    # router.register(r'users', UserViewSet, basename='users')

    # urlpatterns = [
    #     path('', include(router.urls)),
    #     path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
    # ]

Теперь вы можете открыть API в своем браузере по адресу http://127.0.0.1:8000/ и просмотреть свой новый «пользовательский» API. 
Если вы используете элемент управления входом в правом верхнем углу, вы также сможете добавлять, создавать и удалять пользователей из системы.

Ссылка на документацию: https://www.django-rest-framework.org/#installation