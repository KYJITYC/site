
python manage.py runserver - запускает сервер

INSTALLED_APPS = 'app.apps.AppConfig' - для миграции внести строку в файл settings.app -название приложения
	apps-папка, AppConfig-app назване + добавляем слово Config

python manage.py makemigrations app - миграция (синхронизация) приложения. app-название
python manage.py startapp app - запускает приложение. app-название
python manage.py migrate - запуск миграции


"работа с БД"
python manage.py shell:
>>> from app.models import Article, Comment # наши классы
>>> Article.objects.all()- выводит все объекты из БД
>>> Article.objects.get(id= 1) - получить 1 объект id например 1
>>> from django.utils import timezone # для даты публикации
>>> a = Article(article_title = 'какая-то статья', article_text = 'some text', pub_date = timezone.now()) 
>>> a.save() # теперь статья в базе данных
>>> a.id # выдаст id в базе
>>> a.pub_date # выдаст дату
>>> quit() # выход
>>> a=Article.objects.get(id= 1)
>>> a.was_published_recently() #True
>>> Article.objects.filter(article_title__startswith = 'какая' )  #2 нижних подчеркивания
>>> a.arteice_title = 'новый заголовок' # + .save()!
>>> a.save()
>>> current_year = timezone.now().year
>>> Article.objects.filter(pub_date__year = current_year) # скатьиопубликованные в 2020
>>> a.comment_set.create(author_name='джон', comment_text = 'первый' )
>>> a.comment_set.all() # все комменты к статье (при условии article = models.ForeignKey(Article, on_delete = models.CASCADE))
>>> a.comment_set.count()
>>> a.comment_set.filter(author_name__startswith = "не") 
>>> cs = a.comment_set.filter(author_name__startswith = "не")
>>> cs.delete() # удаляет все записи от "не джон"