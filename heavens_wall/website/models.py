from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class comment(models.Model):
    pid=models.IntegerField()
    user=models.CharField(max_length=200,null=False)
    comment=models.TextField(max_length=False)

    def __unicode__(self):
        return str(self.user)

    class Meta:
        verbose_name_plural='comment'

class  comments(models.Model):
    int_id=models.CharField(max_length=10)
    comment_user=models.CharField(max_length=100,null=False)
    user_comments=models.TextField(null=False)
    comment_date=models.DateTimeField()
    comment_likes=models.CharField(max_length=100)
    def __unicode__(self):
        return str(self.comment_user)

    class Meta:
        verbose_name_plural='comments'

class editpages(models.Model):
    page_name=models.CharField(max_length=250,null=False)
    page_content=models.TextField(null=False)
    mtitle=models.TextField(null=False)
    mkeywords=models.TextField(null=False)
    mdescription=models.TextField(null=False)

    def __unicode__(self):
        return str(self.page_name)

    class Meta:
        verbose_name_plural='joinus'

class photos(models.Model):
    user_id=models.IntegerField()
    profile_id=models.IntegerField()
    name=models.CharField(max_length=200,null=False)
    description=models.TextField(null=False)

    def __unicode__(self):
        return str(self.profile_id)

    class Meta:
        verbose_name_plural='photos'

class profile(models.Model):
    user_id=models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=100,null=False,unique=True)
    gb=models.ImageField(blank=True,null=True)
    quotation=models.TextField(null=False)
    arrival_date=models.CharField(max_length=100,null=False)
    departure_date=models.CharField(max_length=100,null=False)
    cause_death=models.TextField(null=False)
    place_death=models.CharField(max_length=250,null=False)
    other=models.TextField(null=False)
    rest_place=models.CharField(max_length=200,null=False)
    other_names=models.TextField(null=False)
    ethnicity=models.CharField(max_length=200,null=False)
    alma=models.TextField(null=False)
    political=models.TextField(null=False)
    religion=models.CharField(max_length=200,null=False)
    spouse=models.CharField(max_length=200,null=False)
    children=models.TextField(null=False)
    parents=models.TextField(null=False)
    known=models.TextField(null=False)
    status=models.CharField(max_length=50,null=False)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return str(self.name)

    class Meta:
        verbose_name_plural='profile'

class register(models.Model):
    Fname=models.CharField(max_length=60,null=False)
    Lname=models.CharField(max_length=60,null=False)
    Email=models.CharField(max_length=60,null=False)
    phone=models.CharField(max_length=60,null=False)
    Fax=models.CharField(max_length=60,null=False)
    password=models.CharField(max_length=60,null=False)
    Status=models.SmallIntegerField(null=False,default=0)
    created_date=models.DateTimeField()
    last_login=models.DateTimeField()

    def __unicode__(self):
        return str(self.Fname)

    class Meta:
        verbose_name_plural='register'

class testimonials(models.Model):
    uid=models.IntegerField()
    title=models.CharField(max_length=60)
    description=models.TextField(null=False)
    status=models.IntegerField()
    placed=models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return str(self.title)

    class Meta:
        verbose_name_plural='testimonials'

class users(models.Model):
    user_name=models.CharField(max_length=200,null=False)
    user_surname=models.CharField(max_length=200,null=False)
    user_email=models.CharField(max_length=200,null=False)
    user_password=models.CharField(max_length=200,null=False)
    user_status=models.IntegerField()
    user_created=models.DateTimeField(auto_now_add=True)
    last_login=models.DateTimeField(null=False)

    def __unicode__(self):
        return str(self.user_name)

    class Meta:
        verbose_name_plural='users'

class video(models.Model):
    user_id=models.IntegerField()
    pid=models.IntegerField()
    visit=models.DateTimeField()
    ip=models.CharField(max_length=20)

    def __unicode__(self):
        return str(self.ip)

    class Meta:
        verbose_name_plural='views'
