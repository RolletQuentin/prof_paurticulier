from django.contrib import admin

from authentication.models import User, School, SchoolSubject, Teacher, Student, Grade

admin.site.register(User)
admin.site.register(School)
admin.site.register(SchoolSubject)
admin.site.register(Teacher)
admin.site.register(Student)
admin.site.register(Grade)
