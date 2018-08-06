from django.conf.urls import url
from . import views

urlpatterns = [
    url(
        regex=r'^home/$',
        view=views.Home.as_view(),
        name='home',
    ),
    url(
        regex=r'^home/login/$',
        view=views.Login.as_view(),
        name='login',
    ),
    url(
        regex=r'^home/register/$',
        view=views.Register.as_view(),
        name='register',
    ),
        url(
        regex=r'^home/login/register/$',
        view=views.Register.as_view(),
        name='register',
    ),
    url(
        regex=r'^home/posting/$',
        view=views.Posting.as_view(),
        name='posting',
    ),
        url(
        regex=r'^posting/$',
        view=views.Posting.as_view(),
        name='posting',
    ),
    url(
        regex=r'^home/list/$',
        view=views.List.as_view(),
        name='post_list',
    ),
    url(
        regex=r'^list/$',
        view=views.List.as_view(),
        name='post_list',
    ),
    url(
        regex=r'^home/list/(?P<post_id>[0-9]+)/$',
        view=views.PostDetail.as_view(),
        name='post_detail',
    ),
    url(
        regex=r'^(?P<username>\w+)/password/$',
        view=views.ChangePassword.as_view(),
        name='Change'
    ),
]