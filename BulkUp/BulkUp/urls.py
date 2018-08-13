from django.conf.urls import include
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views
from django.conf import settings
from app import forms

urlpatterns = [
    url(r'^home/login/$', views.LoginView.as_view(template_name="login_form.html", authentication_form=forms.LoginForm), name="login"),
    url(r'^home/logout/$', views.LogoutView.as_view(next_page=settings.LOGOUT_REDIRECT_URL), name="logout"),
    url(r'^admin/', admin.site.urls),
    url(r'^', include(('app.urls', 'app'), namespace='app')),
    url(r'^accounts/', include('django.contrib.auth.urls')),
]
