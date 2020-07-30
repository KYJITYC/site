!# os.path.dirname слэши / (неправильные для винды) os.path.abspath слэши \. Для правильного отборажения пути папки : os.path.dirname(os.path.abspath(__file__))


>>> django-admin startproject myfirst # созадет папки проекта 'myfirst' название

# так можно указать где хранить приложения
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_ROOT=os.path.dirname(__file__)
sys.path.insert(0,os.path.join(PROJECT_ROOT,'apps'))

>>> python manage.py runserver # запускает сервер. cd в папку с файлом manage.py

>>> python manage.py startapp app # создает приложение. app-название. создает папки приложения
# миграция-информация джанге когда и какие изменения ему заносить в БД
# для подкючения приложения его нужно мигрировать. Непосредственно мигрируют классы из файла models.py (Article, Comment)
INSTALLED_APPS = 'app.apps.AppConfig' # для миграции внести строку в файл settings.py. 'app' - название приложения
	#'apps'- папка, AppConfig -'App' назване пнриложения + добавляем слово 'Config' !или просто app??
    >>> python manage.py makemigrations app # миграция (синхронизация) приложения. app - название 
    # создается файл initial.py
>>> python manage.py migrate # запуск (примененеие) миграции

"работа с БД"
>>> python manage.py shell
>>> quit() # выход
>>> from app.models import Article, Comment # наши классы
>>> from django.utils import timezone # для даты публикации
>>> a = Article(article_title = 'какая-то статья', article_text = 'some text', pub_date = timezone.now()) # создает статью 
>>> a.save() # теперь статья в базе данных
>>> Article.objects.all() # выводит все объекты из БД
>>> Article.objects.get(id = 1) # получить 1 объект id например 1
>>> a.id # выдаст id в базе
>>> a.pub_date # выдаст дату
>>> quit() # выход
>>> a=Article.objects.get(id = 1)
>>> a.was_published_recently() #True
>>> Article.objects.filter(article_title__startswith = 'какая')  #2 нижних подчеркивания
>>> a.arteice_title = 'новый заголовок' # + .save()!
>>> a.save()
>>> current_year = timezone.now().year
>>> Article.objects.filter(pub_date__year = current_year) # скатьиопубликованные в 2020
>>> a.comment_set.create(author_name='джон', comment_text = 'первый')
>>> a.comment_set.all() # все комменты к статье (при условии article = models.ForeignKey(Article, on_delete = models.CASCADE))
>>> a.comment_set.count()
>>> a.comment_set.filter(author_name__startswith = "не") 
>>> cs = a.comment_set.filter(author_name__startswith = "не")
>>> cs.delete() # удаляет все записи от "не джон"

# Администрирование

>>>python manage.py createsuperuser #создает админа с лог\паролем
# в файле apps.py verbose_name = 'Blog' меняет название на Blog
# в файле models.py меняет название
class Meta: 
    verbose_name = 'Статья'
    verbose_name_plural = 'Статьи'
    
#HTML

# Для русификации в файле settings.py LANGUAGE_CODE = 'ru-RU'
# Дополнительно создаем папку templates в ней articles, а туда все html шаблоны для приложения и base.html
# os.path.join(PROJECT_DIR, 'templates') в settings.py в TEMPLATES чтобы искал файлы в новой папке
# в articles создаем list.html
http://127.0.0.1:8000/app/ # даст отображение base.html и list.html
# base.html - шаблон. list.html - расширение шаблона. block 'title' из base отсылает на block 'title' в list. Так же и с 'content'
#"Мой сайт" в base это значение по умолчанию, если в list этого блока не будет






Для ручного изменения переменной PATH нужно поправить один из конфигурационных файлов Bash. Эти файлы лежат в домашней директории пользователя:

.bashrc
.bash_profile
.profile
В зависимости от настроек терминала, Bash прогружает либо одни файлы, либо другие. Если в вашей домашней директории есть файл .bashrc, то пробуйте использовать его, если нет, то остальные файлы в том порядке, в котором они приведены выше. Добавьте в этот файл следующую строку:

export PATH=$PATH:/path/to/directory
Где /path/to/directory путь до директории с исполняемыми файлами.