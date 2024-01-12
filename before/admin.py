from django.contrib import admin

# Register your models here.
from .models import Student,Rollno,Teacher,Skill,Employee
admin.site.register(Student)
admin.site.register(Rollno)
admin.site.register(Teacher)
admin.site.register(Skill)
admin.site.register(Employee)