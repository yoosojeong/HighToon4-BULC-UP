from django.conf.urls import url
from django.contrib.auth import views
from django.conf.urls.static import static
from django.conf import settings
from . import views

app_name = 'app'

urlpatterns = [
    url(
        regex=r'^home/$',
        view=views.Home.as_view(),
        name='home',
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
        regex=r'^home/profile/$',
        view=views.Profile.as_view(),
        name='profile',
    ),
    url(
        regex=r'^home/signup/$',
        view=views.Signup.as_view(),
        name='signup',
    ),
    url(
        regex=r'^home/list/$',
        view=views.List.as_view(),
        name='post_list',
    ),
    url(
        regex=r'^home/list/delete/(?P<post_id>[0-9]+)/$',
        view=views.PostDetail.as_view(),
        name='post_detail',
    ),
    url(
        regex=r'^home/list/(?P<post_id>[0-9]+)/$',
        view=views.PostDetail.as_view(),
        name='post_detail',
    ),
    url(
        regex=r'^home/list/search/$',
        view=views.PostSearch.as_view(),
        name='post_search',
    ),
    # url(
    #     regex=r'^accounts/login/done$',
    #     view=views.ChangePassword.as_view(),
    #     name='create_user_done'
    # ),
] 

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)