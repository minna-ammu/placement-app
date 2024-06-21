from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    name=models.CharField(max_length=200,unique=True)

    def __str__(self):
        return self.name
    
class Jobs(models.Model):
    title=models.CharField(max_length=200)
    description=models.CharField(max_length=200)
    salary=models.PositiveIntegerField()
    experience=models.PositiveIntegerField(default=0)
    last_date=models.DateField()
    vaccancies=models.PositiveIntegerField(default=1)
    poster=models.ImageField(upload_to="poster images",null=True,blank=True)
    contact=models.CharField(max_length=200)
    qualification=models.CharField(max_length=200)
    category=models.ForeignKey(Category,on_delete=models.DO_NOTHING)
    status=models.BooleanField(default=True)

    def __str__(self):
        return self.title

class Student_profile(models.Model):
    qualification=models.CharField(max_length=200)
    resume=models.FileField(upload_to="resumes",null=True,blank=True)
    skills=models.CharField(max_length=200)
    options=(
        ("male","male"),("female","female")
    )
    gender=models.CharField(max_length=200,choices=options,default="female")
    experience=models.PositiveIntegerField()
    address=models.CharField(max_length=200)
    phone_number=models.CharField(max_length=200)
    profile_pic=models.ImageField(upload_to="profile pics",null=True,blank=True)
    user=models.OneToOneField(User,on_delete=models.CASCADE)

class Applications(models.Model):
    job=models.ForeignKey(Jobs,on_delete=models.DO_NOTHING)
    student=models.ForeignKey(User,on_delete=models.CASCADE)
    applied_date=models.DateTimeField(auto_now_add=True)
    options=(
        ("pending","pending"),("rejected","rejected"),("processing","processing")
    )
    status=models.CharField(max_length=200,choices=options,default="pending")

class Projects(models.Model):
    name=models.CharField(max_length=200)
    description=models.CharField(max_length=200)
    git_link=models.CharField(max_length=200)
    user=models.ForeignKey(Student_profile,on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name
