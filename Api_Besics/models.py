from django.db import models
# from my_app.models import Person
from django.contrib.auth.models import UserManager


# Create your models here.
class Article(models.Model):
    title=models.CharField(max_length=100)
    author=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    # objects = UserManager()
    #
    # class Meta:
    #     db_table = 'Article'
    # # class Meta:
    # #     model = person
    #     fields = '__all__'


    # class ArticleForm(ModelForm):
    #     class Meta:
    #         model = Article
    #         fields = '__all__'

