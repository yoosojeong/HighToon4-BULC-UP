from django.contrib import admin
from django import forms
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from . import models

@admin.register(models.Profile)
class ProfileAdmin(admin.ModelAdmin):

    model = models.Profile
    can_delete = False
    verbose_name_plural = 'profile'

    list_display = (
        'user', 
        'profile_image', 
        'name', 
        'gender', 
        'bio', 
        'age',
    )

class UserAdmin(UserAdmin):
    inlines = [
        ProfileAdmin
    ]

# Re-register UserAdmin

@admin.register(models.PostingData)
class PostingAdmin(admin.ModelAdmin):

    list_display = (
        'created_at',
        'id',
        'subjsect',
        'title',
        'creator',
        'message',
        'qualification',
        'personnel',
        'location',
        'time',
        'term'
    )