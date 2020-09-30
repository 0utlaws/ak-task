from django.contrib import admin
from .models import (
    Candidate,
    Recruiter,
    Task,
    Grade
)


@admin.register(Candidate)
class CandidateAdmin(admin.ModelAdmin):
    search_fields = ('first_name', 'last_name')


@admin.register(Recruiter)
class RecruiterAdmin(admin.ModelAdmin):
    search_fields = ('first_name', 'last_name')


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    search_fields = ('title',)


@admin.register(Grade)
class GradeAdmin(admin.ModelAdmin):
    list_display = ('task', 'value', 'recruiter', 'candidate')
    search_fields = ('value', 'task__title', 'candidate__first_name', 'candidate__last_name',
                     'recruiter__first_name', 'recruiter__last_name')
