from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

from .views import *

urlpatterns = [
    path('', MangoHome.as_view(), name='home'),
    path('tags/', TagCloud.as_view(), name='tags'),
    path('tag/<slug:tag_slug>', get_tag, name='get_tag'),
    path('news/<slug:news_slug><int:news_id>', view_news, name='view_news'),
    path('singup/', RegisterUser.as_view(), name='singup'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('addnews/', add_news, name='add_news'),
    path('mynews/', user_news, name='user_news'),
]


