from django.contrib import admin
from .models import Student
# Register your models here.


class Studentadmin(admin.ModelAdmin):
    list_display = ['student_id','student_name','student_address','student_marks']
admin.site.register(Student, Studentadmin)