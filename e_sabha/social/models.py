from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator,MaxValueValidator,RegexValidator
# Create your models here.

class MyProfile(models.Model):
    name = models.CharField(max_length = 100)
    user = models.OneToOneField(to = User, on_delete=models.CASCADE)
    age = models.IntegerField(default=18,validators = [MinValueValidator(18)])
    gender = models.CharField(max_length = 20,choices = (('male','male'),('female','female')))
    status = models.CharField(max_length = 20,choices = (('single','single'),('married','married')))
    pno = models.CharField(max_length = 10,null = 'True',blank = 'True')
    discription = models.TextField()
    profile_pic = models.ImageField(upload_to = 'images//' ,null = True,blank = False)
    def __str__(self):
        return self.name
    
       

class MyPost(models.Model):
    pic = models.ImageField(upload_to = 'images//' ,null = True)
    subject = models.CharField(max_length = 200)
    msg = models.TextField(null = True,blank = True)
    cr_date = models.DateTimeField(auto_now_add = True)
    uploaded_by = models.ForeignKey(to = MyProfile,on_delete = models.CASCADE,null = True,blank = True)
    def __str__(self):
        return self.uploaded_by

class PostComment(models.Model):
    post = models.ForeignKey(to = MyPost,on_delete = models.CASCADE)
    msg = models.TextField()
    commented_by = models.ForeignKey(to = MyProfile,on_delete = models.CASCADE)
    cr_date = models.DateTimeField(auto_now_add = True)
    flag = models.CharField(max_length = 20,null = True,blank = True,choices = (('racist','racist'),('abuse','abuse'))) 
    def __str__(self):
        return self.msg

class PostLike(models.Model):
    post = models.ForeignKey(to = MyPost,on_delete = models.CASCADE)
    liked_by = models.ForeignKey(to = MyProfile,on_delete = models.CASCADE) 
    cr_date = models.DateTimeField(auto_now_add = True)
    def __str__(self):
        return self.liked_by
class FollowUser(models.Model):
    profile = models.ForeignKey(to = MyProfile, on_delete = models.CASCADE,related_name = 'profile')
    followed_by = models.ForeignKey(to = MyProfile, on_delete = models.CASCADE,related_name = 'followed_by')     
    def __str__(self):
        return self.profile.name
class Contact(models.Model):
    name = models.CharField(max_length=200,null = True)
    email = models.EmailField(max_length=200,null = True)
    phone= models.CharField(max_length=12,null = True)
    msg= models.CharField(max_length=500,null = True)
    date= models.DateField(null = True,blank = True)
    def __str__(self):
        return self.name
    