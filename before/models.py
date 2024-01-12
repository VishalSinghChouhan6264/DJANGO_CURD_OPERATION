from django.db import models

# Create your models here.
class demo(models.Model):
    first_name=models.CharField(max_length=250)
    last_name=models.CharField(max_length=250)
    contact_num=models.IntegerField(null=True)


class Post(models.Model):
    title=models.CharField(max_length=200)
    content=models.TextField()


class Skill(models.Model):
    s_name=models.CharField(max_length=100)

    def __str__(self):
        return self.s_name

class Teacher(models.Model):
    t_name=models.CharField(max_length=50)

    def __str__(self):
        return self.t_name

class Rollno(models.Model):
    rollno=models.IntegerField()
    def __str__(self):
        return str(self.rollno)

class Student(models.Model):
    name=models.CharField(max_length=50)
    phone_no=models.CharField(max_length=50)
    rollno=models.OneToOneField(Rollno,on_delete=models.CASCADE)
    teacher=models.ForeignKey(Teacher,on_delete=models.CASCADE)
    skills=models.ManyToManyField(Skill)

    def __str__(self):
        return self.name
    
class Employee(models.Model):
    eid=models.CharField(max_length=20)
    ename=models.CharField(max_length=50)
    eemail=models.EmailField()
    econtact=models.CharField(max_length=15)

    

    