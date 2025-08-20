from django.contrib import admin
from unfold.admin import ModelAdmin

from tracker.codetracker.models import problem, solution, streak, streak_registered

# Register your models here.

admin.site.register(problem)
admin.site.register(solution)
admin.site.register(streak_registered)

@admin.register(streak)
class streakAdmin(ModelAdmin):
    list_display = ("name", "code")