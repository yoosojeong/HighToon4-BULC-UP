# from django.contrib.auth import get_user_model
from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from .models import Profile
from .models import PostingData

# User = get_user_model()

class SignupForm(UserCreationForm):

    GENDER_CHOICES = {
        ('male', 'male'),
        ('female', 'female'),
        ('not-specified', 'not-specified')
    }

    profile_image = forms.ImageField(required=True)
    name = forms.CharField(required=True)
    gender = forms.ChoiceField(choices=GENDER_CHOICES, required=True)
    bio = forms.CharField(required=True)
    age = forms.IntegerField(required=True)

    class Meta(UserCreationForm.Meta):

        fields = UserCreationForm.Meta.fields + (
            "profile_image",
        )

        def __init__(self, *args, **kwargs):
            super(UserCreationForm, self).__init__(*args, **kwargs)
            self.fields['profile_image'].required = False

    def save(self):
        
        user = super().save()

        profile = Profile.objects.create(
            user=user,
            profile_image = self.cleaned_data['profile_image'],
            name = self.cleaned_data['name'],
            gender = self.cleaned_data['gender'],
            bio = self.cleaned_data['bio'],
            age = self.cleaned_data['age'],
        )
        
        return user.save()

class LoginForm(AuthenticationForm):
    answer = forms.IntegerField(label='3+3=?')
    
    def clean_answer(self): # clean_'필드명' 을 통해 유효성 검사 가능
        if self.cleaned_data.get('answer', None) != 6:
            raise forms.ValidationError('땡~!!!')

class PostingDataForm(forms.ModelForm):
        
    term_CHOICES = {
        ('long', '장기'),
        ('short', '단기'),
        ('not-specified', '미정')
    }

    def __init__(self, user, *args, **kwargs):
        
        super(PostingDataForm, self).__init__(*args, **kwargs)

        self.fields['creator']=forms.ModelChoiceField(queryset=Profile.objects.filter(name = user))

    subjsect = forms.CharField(required=True) 
    title = forms.CharField(required=True)
    message = forms.CharField(required=True)
    qualification = forms.CharField(required=True)
    personnel = forms.CharField(required=True) 
    location = forms.CharField(required=True) 
    time = forms.CharField(required=True)
    term = forms.ChoiceField(choices=term_CHOICES, required=True) 

    class Meta:
        model = PostingData

        fields = ('subjsect', 'title', 'creator', 'message', 'qualification', 'personnel', 'location', 'time', 'term',)
