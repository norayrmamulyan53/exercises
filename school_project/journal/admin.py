from django.contrib import admin
from .models import Teacher, Student, Subject


class PersonAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'age', 'join_date', 'last_updated')
    list_display_links = ('id', 'full_name')
    search_fields = 'full_name',


class SubjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'teacher')
    list_display_links = 'name',
    search_fields = 'name',


roles = [Teacher, Student]
admin.site.register(roles, PersonAdmin)
admin.site.register(Subject, SubjectAdmin)
