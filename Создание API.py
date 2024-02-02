Этапы создания API приложения

Рассматривается на примере данных о аптечных товарах

    1. Создаём приложение 'products' в проекте и добавляем его в 'INSTALLED_APPS' главной папки проекта:
        # bash
        # django-admin startapp products
        
        # settings.py
        # 'INSTALLED_APPS' = [
        #             ...
        #     'products.apps.ProductsConfig',
        #             ...      
        # ]
        
    2. В 'models.py' создаём таблицы:
        # 'Category' (категория товара - лекарства, БАДы и витамины, косметика и т.д.), 
        # 'SubCategory' (подкатегория товара - БАДы для мужчин, БАДы для улучшения памяти и т.д.), 
        # 'Product' (основные характеристики выбранного товара - цена, объём, страна производства и т.д.) 
        # 'Instruction' (инструкция к товару и описание - способ применения, описание, состав и т.д.)
        
    3. Регистрируем таблицы в 'products/admin.py':
        # from django.contrib import admin
        # from .models import Category, SubCategory, Product, Instruction

        # admin.site.register(Category)
        # admin.site.register(SubCategory)
        # admin.site.register(Product)
        # admin.site.register(Instruction)
        
    4. Создаём 'serializers.py' в 'products' и заполняем:
        # from rest_framework import serializers
        # from .models import Category, SubCategory, Product, Instruction
        
        
        # class CategorySerializer(serializers.ModelSerializer): - Создаём класс для преобразования данных модели в JSON и обратно для взаимодействия с данными через API.
        #     class Meta: - Создаём класс для предоставления метаданных сериализатора
        #         model = Category - Задаём модель, с которой будет связан сериализатор
        #         fields = '__all__' - Указываем все поля
                
        # На основе кода выше создаём аналогичные классы.
        
    5. Далее в 'products/views.py' пишем:
        # from django.shortcuts import render
        # from rest_framework import viewsets - также добавить к импорту
        # from products.models import Category, SubCategory, Instruction, Product - импорт таблиц из products/models.py
        # from products.serializers import CategorySerializer, SubCategorySerializer, ProductSerializer, InstructionsSerializer - импорт сериализаторов из products/serializators.py


        # class CategoryApiView(viewsets.ModelViewSet): - Здесь указываем имя контроллера, которое затем передаём в 'router' в 6 пункте, 
        #                                                 представляет собой обработчики для типичных операций CRUD (Create, Retrieve, Update, Destroy)
        #     queryset = Category.objects.all() - Устанавливаем доступ ко всем объектам модели Category
        #     serializer_class = CategorySerializer - Указываем используемый сериализатор
        #     http_method_names = ['get'] - Указываем метод обработки запросов
            
        # На основе кода выше создаём аналогичные классы.
        
    6. Далее указываем маршруты в 'urls.py' проекта:
        # from django.contrib import admin
        # from django.urls import path, include
        # from rest_framework import routers
        # from products.views import CategoryApiView, SubCategoryApiView, ProductApiView, InstructionsApiView - импорт из 'products/views.py'
        
        # router = routers.DefaultRouter() # Используется для упрощения процесса создания URL-маршрутов для представлений API
        # router.register(r'api/cat', CategoryApiView) - Регистрируем представления в URL-маршрутизаторе 
        # router.register(r'api/cat/subcat', SubCategoryApiView)
        # router.register(r'api/cat/subcat/products', ProductApiView)
        # router.register(r'api/cat/subcat/products/instructions', InstructionsApiView)
        
        # urlpatterns = [
        #     path('', include(router.urls)), # Подставляем автоматически созданные URL-маршрутов от router выше 
        #     path('pages/', include('pages.urls')),
        #     path('admin/', admin.site.urls),
        #             ]
        
