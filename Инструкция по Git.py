Первоначальные настройки

1. Установить git:
    # sudo apt update && sudo apt install git

2. В VsCode в расширениях вводим "GitHub Pull Requests and Issues", устанавливаем и перезагружаем.

3. Далее необходимо глобально авторизовать на своей ОС аккаунт на GitHub:
    # git config --global user.email "электронная почта учётной записи"
    # git config --global user.name "имя учётной записи (логин)"
    
4. В нижнем левом углу нажимаем на значок "GitHub" и находим пункт связанный с авторизацией, кликаем и входим 
   в учётную запись.


#__________________________________________________________________________________________________________________________________________
# Создание репозитория.
#__________________________________________________________________________________________________________________________________________

1. Создаём на "GitHub" репозиторий ("знак плюса в верхнем правом углу экрана")

2. Клонируем репозиторий с "GitHub" нажимаем "f1" и вводим команду "Git" и выпадающем меню выбираем "clone",
   и вставляем url ссылку на репозиторий, которая генерируется при создании репозитория, выбираем папку в которой
   он будет храниться и добавляем в рабочую область редактора.
   
3. При работе с проектом все изменения будут отображаться в меню редактора слева в графе "Система контроля версий".
   Чтобы добавлять файлы в облачный репозиторий изменения в проекте необходимо сначала в графе "Система контроля версий"
   проименовать внесённые изменения и иксировать ("Фиксация", либо значок галочки в графе "Репозитории Системы управления версиями"), 
   далее слева от галочки фиксации кливаем на значок синхронизации и таким образом добавляем изменения в репозиторий.

       
    
#__________________________________________________________________________________________________________________________________________
# Загрузка проекта в репозиторий на GitHub.
#__________________________________________________________________________________________________________________________________________  

1. Создаём новый репозиторий на "GitHub"

2. В папке проекта вводим поочерёдно команды:
    # git init  - инициализация git в проекте 
    # git add . - используем точку обозначения текущей директории
    
   Теперь в меню "Система контроля версий" отобразятся файлы, включённые в коммит.
   
3. Далее в меню "Система контроля версий" в графе "Репозитории Системы управления версиями" кликаем на три точки, 
   Удалённый --> Добавить удалённый репозиторий, в строку добавляем url-ссылку на облачный репозиторий, вводим имя
   под который был создан репозиторий, то есть имя аккаунта. 

4. Далее фиксируем файлы, проводим синхронизацию и файлы будут добавлены в хранилище.




#__________________________________________________________________________________________________________________________________________
# Заметки
#__________________________________________________________________________________________________________________________________________

   Для того чтобы игнорировать какие-либо папки в папке проекта используется файл ".gitignore",
   например, в папке проекта "project" находятся папки "app" и "venv", для этого в области этих папок, то есть
   в "project" создаём файл ".gitignore" и вводим:
       # /venv/
       
   Также важно учитывать то,что изменения в '.gitignore' не применяются к уже проиндексированным файлам, поэтому
   чтобы файлы из '.gitignore' были невидимы в облачном репозитории необходимо удалить нужный файл из отслеживания Git:
      # git rm --cached <Имя файла> - вводим находясь на одном уровне с файлом
       
   Для удаления входим по пути в терминал папки,из которой необходимо удалить файл и вводим:
      # git rm <имя файла>
      
   