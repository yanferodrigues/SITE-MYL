from django.contrib import admin
from gym.models import Workout, MuscleGroup,Exercise

class ListWorkout(admin.ModelAdmin):
    list_display = ("user","day")
    list_display_links = ("user","day")
    search_fields = ("user",)
    ordering = ("user",)

class ListMuscleGroup(admin.ModelAdmin):
    list_display = ("workout__user","workout","name")
    list_display_links = ("workout__user","workout","name")
    search_fields = ("workout__user",)
    ordering = ("workout__user",)
    
class ListExercise(admin.ModelAdmin):
    list_display = ("muscle_group__workout__user","muscle_group","name")
    list_display_links = ("muscle_group__workout__user","muscle_group","name")
    search_fields = ("muscle_group__workout__user",)
    ordering = ("muscle_group__workout__user",)

admin.site.register(Workout, ListWorkout)
admin.site.register(MuscleGroup,ListMuscleGroup)
admin.site.register(Exercise,ListExercise)
