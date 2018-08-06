from django.contrib import admin
from django import forms
from django.contrib.auth.admin import UserAdmin as AuthUserAdmin
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from .models import UserBox
from . import models


class MyUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = UserBox


class MyUserCreationForm(UserCreationForm):

    error_message = UserCreationForm.error_messages.update({
        'duplicate_username': 'This username has already been taken.'
    })

    class Meta(UserCreationForm.Meta):
        model = UserBox

    def clean_username(self):
        username = self.cleaned_data["username"]
        try:
            UserBox.objects.get(username=username)
        except UserBox.DoesNotExist:
            return username
        raise forms.ValidationError(self.error_messages['duplicate_username'])


@admin.register(UserBox)
class MyUserAdmin(AuthUserAdmin):
    form = MyUserChangeForm
    add_form = MyUserCreationForm
    fieldsets = (
            ('User Profile', {'fields': ('profile_image', 'name', 'gender', 'age','bio')}),
    ) + AuthUserAdmin.fieldsets
    list_display = ('username', 'name', 'is_superuser')
    search_fields = ['name']

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