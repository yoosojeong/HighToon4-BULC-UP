from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _

class TimeStampedModel(models.Model):
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class UserBox(AbstractUser):

    GENDER_CHOICES = {
        ('male', 'Male'),
        ('female', 'Female'),
        ('not-specified', 'Not specified')
    }

    profile_image = models.ImageField(null=True)
    name = models.CharField(_('Name of User'), blank=True, max_length=255)
    gender = models.CharField(max_length=80, choices=GENDER_CHOICES, null=True)
    bio = models.TextField(null=True, max_length=150)
    age = models.IntegerField(null=True)

    def __str__(self):
        return self.name

class PostingData(TimeStampedModel):
    
    term_CHOICES = {
        ('long', '장기'),
        ('short', '단기'),
        ('not-specified', '미정')
    }

    subjsect = models.TextField() #주제 / 언어
    title = models.TextField(max_length=80) #제목
    creator = models.ForeignKey(UserBox, on_delete=models.CASCADE, null=True, related_name='creator') #주체자
    message = models.TextField(max_length=500) #내용
    qualification = models.TextField(max_length=500) #참가자격
    personnel = models.TextField(max_length=10) #모집 인원수
    location = models.CharField(max_length=140) #장소 / 좌표, 지도
    time =  models.TextField(max_length=80) #기간 / 매주 월요일 2시~4시
    term = models.TextField(max_length=80, choices=term_CHOICES, null=True) #장기, 단기

    class Meta:
        ordering = ['-created_at']