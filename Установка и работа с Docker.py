Шаг 1 — Установка Docker

    Пакет установки Docker, доступный в официальном репозитории Ubuntu, может содержать не самую последнюю версию. 
    Чтобы точно использовать самую актуальную версию, мы будем устанавливать Docker из официального репозитория Docker. 
    Для этого мы добавим новый источник пакета, ключ GPG от Docker, чтобы гарантировать загрузку рабочих файлов, а затем установим пакет.

    Первым делом обновите существующий список пакетов:
        # sudo apt update
        
    Затем установите несколько необходимых пакетов, которые позволяют apt использовать пакеты через HTTPS:
        # sudo apt install apt-transport-https ca-certificates curl software-properties-common
    
    
    Добавьте ключ GPG для официального репозитория Docker в вашу систему:
        # curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
        
    Добавьте репозиторий Docker в источники APT:
        # sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu focal stable"
        
    Потом обновите базу данных пакетов и добавьте в нее пакеты Docker из недавно добавленного репозитория:
        # sudo apt update
        
    Убедитесь, что установка будет выполняться из репозитория Docker, а не из репозитория Ubuntu по умолчанию:
        # apt-cache policy docker-ce
        
    Вы должны получить следующий вывод, хотя номер версии Docker может отличаться:
        # Output of apt-cache policy docker-ce
        # docker-ce:
        # Installed: (none)
        # Candidate: 5:19.03.9~3-0~ubuntu-focal
        # Version table:
        #     5:19.03.9~3-0~ubuntu-focal 500
        #         500 https://download.docker.com/linux/ubuntu focal/stable amd64 Packages

    Установите Docker:
        # sudo apt install docker-ce
        
    Docker должен быть установлен, демон-процесс запущен, а для процесса активирован запуск при загрузке. Проверьте,
    что он запущен:
        # sudo systemctl status docker
        
    Вывод должен выглядеть примерно следующим образом, указывая, что служба активна и запущена:
        # Output
        # ● docker.service - Docker Application Container Engine
        #     Loaded: loaded (/lib/systemd/system/docker.service; enabled; vendor preset: enabled)
        #     Active: active (running) since Tue 2020-05-19 17:00:41 UTC; 17s ago
        # TriggeredBy: ● docker.socket
        #     Docs: https://docs.docker.com
        # Main PID: 24321 (dockerd)
        #     Tasks: 8
        #     Memory: 46.4M
        #     CGroup: /system.slice/docker.service
        #             └─24321 /usr/bin/dockerd -H fd:// --containerd=/run/containerd/containerd.so
        
        
    Также нужно авторизоваться на DockerHub.
    
Шаг 2 - Подготовка проекта 
    Создаём в корневой диретории проекта файл 'Dockerfile' и прописываем команды ниже:
        
        # FROM python:3.10


        # SHELL ["/bin/bash", "-c"]

        # # Запрещаем создание файлов с кэшем внутри контейнера (1), иначе Python будет создавать .pyc файлы 
        # # для ускорения повторной компиляции и выполнения программ (0)
        # ENV PYTHONDONTWRITEBYTECODE 1 

        # # Указываем полный вывод ошибок приложения в stdout (1), а иначе вывод Python будет буферизированным (0)
        # ENV PYTHONUNBUFFERED 1 

        # # Обновляем пакет pip внутри контейнера
        # RUN pip install --upgrade pip


        # # Обновление списка пакетов из репозиториев APT в контейнере и установка доп пакетов и зависимостей
        # RUN apt update && apt -qy install gcc libjpeg-dev libxslt-dev libpq-dev gettext cron openssh-client \
        #     flake8 locales neovim

        # # gcc (GNU Compiler Collection) — набор компиляторов для различных языков программирования, таких как C, C++ и др.
        # # libjpeg-dev: Библиотека для работы с изображениями в формате JPEG.
        # # libxslt-dev: Библиотека для работы с XSLT (eXtensible Stylesheet Language Transformations).
        # # libpq-dev: Настройка для разработки приложений, использующих PostgreSQL.
        # # gettext: Утилиты для работы с локализацией и интернационализацией.
        # # cron: Планировщик задач.
        # # openssh-client: Клиент OpenSSH для подключения к другим удаленным хостам по SSH.
        # # flake8: Инструмент для проверки стиля кода Python.
        # # locales: Набор файлов локализации системы.




        # # Создаём нового пользователя с именем "andrey" в контейнере
        # # -m: Создает домашнюю директорию для пользователя, если она еще не существует.
        # # -s /bin/bash: Устанавливает исполняемый файл для оболочки по умолчанию для нового пользователя на /bin/bash.
        # # chmod 777 /opt /run: Эта команда устанавливает права доступа для директорий /opt и /run
        # RUN useradd -rms /bin/bash andrey && chmod 777 /opt /run

        # # Указываем рабочую директории внутри контейнера
        # WORKDIR /pharm_app

        # # Копируем файл с зависимостями
        # COPY requirements.txt .

        # # Устанавливаем зависимости проекта
        # RUN pip install -r requirements.txt

        # # Копируем модержимое проекта в директорию выше, то есть в pharm_app
        # COPY --chown=andrey:andrey . .

        # # Выбираем нового пользователя и от его имени выполняем команду ниже
        # USER andrey

        # CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
        
        
    Далее необходимо добавить текущего пользователя в группу docker, которая имеет правильные разрешения для доступа к сокету 
    Docker:
        
        # sudo usermod -aG docker <имя пользователя>

    Далее в корневой папке проекта, где находится 'Dockerfile' создаём образ нашшего проекта:
        
        # docker build -t <название образа> .
        
    Создаём файл '.env' в корневой папке проекта, добавляем его в '.gitignore' и пишем следующее:
        
        # PostgreSQL configuration
        # POSTGRES_HOST=localhost
        # POSTGRES_PORT=5432
        # POSTGRES_USER=mainrole
        # POSTGRES_PASSWORD=abemuH77!
        # POSTGRES_DB=pharmapp_db
        # Django configuration:
        # DJANGO_SETTINGS_MODULE=core.settings
        # DJANGO_SECRET_KEY=django-insecure-craodd_%_m$dl2ns9o#!hmvno56v_k=o9cl_93@(fczt+ut_o@
        # JWT configuration
        # SIMPLE_JWT_ALGORITHM=HS256
        # SIMPLE_JWT_SIGNING_KEY=G4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKx
        # SIMPLE_JWT_VERIFYING_KEY=wRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c
    
        В этот файл нужно добавлять переменные, значения которых необходимо скрыть, для этого в 'settings.py' оборачиваем такие 
            данные в "os.getenv", например:
                # '<переменная в settings.py>' = os.getenv('<кастомное имя переменной для .env>')
            
            Далее добавляем их в '.env' без кавычек в виде <кастомное имя переменной для .env>=значение
        
        Причание: 
            Для удаления образа используется команда - # docker rmi <IMAGE ID>
            
            Посмотреть 'IMAGE ID' можно по команде - # docker images
        
    В 'settings.py' исправляем значение переменной:
            # ALLOWED_HOSTS = ['*']

Шаг 3 - Запуск контейнера

    Для запуска сервисов на основе описания в файле docker-compose.yml используется команда:
        # docker compose up

    Для удаления неактивных контейнеров (которые не запущены в данный момент), неиспользуемых образов (образы, которые не связаны ни с одним контейнером),
    неиспользуемых сетей (сети, которые не используются ни при одном контейнере), неиспользуемых томов (тома, которые не связаны ни с одним контейнером)
    используется команда:
        # docker system prune

    Для остановки всех сервисов, связанных с вашим проектом, и удаления связанных с ним контейнеров, сетнй, томов и образов:
        # docker compose down
        
    Для удаления конкретного образа используется команда:
        # docker rmi <имя образа>:<версия> - эти данные прописываются в 'docker-compose.yml'
        
    Если после запуска контейнера нужно пересоздать образ, то сначала нужно остановить все сервисы через "docker compose down",
    а затем удалять.


Пример содержимого файла 'docker-compose.yml':
        # version: '3.10' # указываем версию python

        # services:
        # db: # значение POSTGRES_HOST из .env
        #     image: postgres:latest # Версия psql, в данном случае последняя
        #     container_name: pharmapp_postgres # кастомное имя контейнера БД
        #     volumes: 
        #     - ~/.pg/pg_data/pharmapp_db:/var/lib/postgresql/data # папка,которой будет храниться в контейнере созданная БД
        #     env_file: 
        #     - .env # имя файла с зависимостями

        # project:
        #     image: pharmapp_image:latest # имя созданного образа по Dockerfile
        #     container_name: pharmapp_container # кастомное имя контейнера проекта
        #     depends_on: 
        #     - db # Установление зависимости образа от сервиса БД
        #     env_file: 
        #     - .env # имя файла с зависимостями
        #     ports:
        #     - "8000:8000"
        #     command: > # Описание всего, что нужно сделать контейнеру для запуска приложения
        #     bash -c "./manage.py migrate && ./manage.py runserver 0.0.0.0:8000" 


Пример содержимого файла 'Dockerfile':
        # FROM python:3.10

        # # Указание конкретной оболочки, которая будет использоваться для выполнения команд в контейнере
        # SHELL ["/bin/bash", "-c"] 

        # # Запрещаем создание файлов с кэшем внутри контейнера (1), иначе Python будет создавать .pyc файлы 
        # # для ускорения повторной компиляции и выполнения программ (0)
        # ENV PYTHONDONTWRITEBYTECODE 1 

        # # Указываем полный вывод ошибок приложения в stdout (1), а иначе вывод Python будет буферизированным (0)
        # ENV PYTHONUNBUFFERED 1 

        # # Обновляем пакет pip внутри контейнера
        # RUN pip install --upgrade pip


        # # Обновление списка пакетов из репозиториев APT в контейнере и установка доп пакетов и зависимостей
        # RUN apt update && apt -qy install gcc libjpeg-dev libxslt-dev libpq-dev gettext cron openssh-client \
        #     flake8 locales neovim

        # # gcc (GNU Compiler Collection) — набор компиляторов для различных языков программирования, таких как C, C++ и др.
        # # libjpeg-dev: Библиотека для работы с изображениями в формате JPEG.
        # # libxslt-dev: Библиотека для работы с XSLT (eXtensible Stylesheet Language Transformations).
        # # libpq-dev: Настройка для разработки приложений, использующих PostgreSQL.
        # # gettext: Утилиты для работы с локализацией и интернационализацией.
        # # cron: Планировщик задач.
        # # openssh-client: Клиент OpenSSH для подключения к другим удаленным хостам по SSH.
        # # flake8: Инструмент для проверки стиля кода Python.
        # # locales: Набор файлов локализации системы.


        # # Создаём нового пользователя с именем "andrey" в контейнере
        # # -m: Создает домашнюю директорию для пользователя, если она еще не существует.
        # # -s /bin/bash: Устанавливает исполняемый файл для оболочки по умолчанию для нового пользователя на /bin/bash.
        # # chmod 777 /opt /run: Эта команда устанавливает права доступа для директорий /opt и /run
        # RUN useradd -rms /bin/bash andrey && chmod 777 /opt /run

        # # Указываем рабочую директории внутри контейнера
        # WORKDIR /pharm_app

        # # Копируем файл с зависимостями
        # COPY requirements.txt .

        # # Устанавливаем зависимости проекта
        # RUN pip install -r requirements.txt

        # # Копируем модержимое проекта в директорию выше, то есть в pharm_app
        # COPY --chown=andrey:andrey . .

        # # Выбираем нового пользователя и от его имени выполняем команду ниже
        # USER andrey

        # # Перечень команд, который выполнит командная оболочка контейнера
        # CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]


Пример содержимого файла '.env':
        # # PostgreSQL configuration
        # POSTGRES_HOST=db - хост, который мы указываем в 'docker-compose.yml' в 'services'
        # POSTGRES_PORT=5432 - данные из 'settings.py' проекта
        # POSTGRES_USER=mainrole - данные из 'settings.py' проекта
        # POSTGRES_PASSWORD=abemuH77! - данные из 'settings.py' проекта
        # POSTGRES_DB=pharmapp_db - данные из 'settings.py' проекта
        # # Django configuration:
        # DJANGO_SETTINGS_MODULE=core.settings - ссылка на 'settings.py'
        # # JWT configuration
        # SIMPLE_JWT_ALGORITHM=HS256 - данные из 'settings.py' проекта
        # SIMPLE_JWT_SIGNING_KEY=G4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKx - данные из 'settings.py' проекта
        # SIMPLE_JWT_VERIFYING_KEY=wRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c - данные из 'settings.py' проекта


Хорошие гайды:
    https://www.youtube.com/watch?v=YgNFEeiqGyw
    https://www.youtube.com/watch?v=u9JExSCA9eE