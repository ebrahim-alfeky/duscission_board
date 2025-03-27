from django.db import models
from datetime import datetime
current_date = datetime.now().date()
current_time = datetime.now().time()
# Create your models here.

#* django provide user class 
from django.contrib.auth.models import User
#! board topic post user

class Board(models.Model):#todo   موضوع   
    #todo Board is table in database and fileds is columens
    #todo django provide id(primary key for each object)==add new columen
    
    name=models.CharField(max_length=25,unique=True,blank=True)
    #todo max_length for security
    #todo unique=True name don't repeat
    
    description=models.CharField(max_length=500,null=True)
    
    created_by=models.ForeignKey(User,related_name='boards',on_delete=models.CASCADE,null=True)

    def __str__(self):
        return str(self.name)


class Topic(models.Model):
    subject=models.CharField(max_length=250)
    #todo relation between Board & Topic == foreign key == one to many
    #todo one Board can take many Topic
    
    board=models.ForeignKey(Board,related_name='topics',on_delete=models.CASCADE)
    
    created_by=models.ForeignKey(User,related_name='topics',on_delete=models.CASCADE,null=True)
    
    created_date=models.DateField(auto_now_add=True)

    def __str__(self):
        return self.subject

class Post(models.Model):
    message=models.TextField(max_length=1000)
    #todo relation between Post & Topic == foreign key == one to many
    #todo one Topic can take many Post
    
    topic=models.ForeignKey(Topic,related_name="posts",on_delete=models.CASCADE)
    
    created_by=models.ForeignKey(User,related_name='posts',on_delete=models.CASCADE,null=True)

    created_date=models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.message
