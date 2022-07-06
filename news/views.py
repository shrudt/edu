from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView
from datetime import date

from .models import *
from .forms import *


class MangoHome(ListView):
    model = News
    template_name = "news/news_list.html"
    context_object_name = "news"
    extra_context = {"title": "Mango", }


class TagCloud(ListView):
    model = Tags
    template_name = "news/tag_cloud.html"
    context_object_name = "tags"
    extra_context = {"title": "Tag cloud", }


def get_tag(request, tag_slug):
    news = News.objects.filter(tag__slug=tag_slug)
    tag = Tags.objects.get(slug=tag_slug)
    data = {
        'news': news,
        'tag': tag,
        'title': tag.tag_name,
    }
    return render(request, template_name='news/tag_list.html', context=data)


def view_news(request, news_slug, news_id):
    if request.method == 'POST':
        com = Comments(news=News.objects.get(id=news_id), user=User.objects.get(username=request.user), date=date.today())
        comment = CommentForm(request.POST, instance=com)
        comment.save()
        return HttpResponseRedirect(reverse('view_news', args=(news_slug, news_id, )))

    else:
        news = News.objects.get(slug=news_slug)
        tags = news.tag.all()
        comments = Comments.objects.filter(news_id=news_id).select_related('user')
        comment_form = CommentForm
        data = {
            'news': news,
            'tags': tags,
            'comments': comments,
            'title': news.title,
            'form': comment_form,
        }
        return render(request, template_name='news/view_news.html', context=data)


class RegisterUser(CreateView):
    form_class = UserCreationForm
    template_name = 'news/singup.html'
    success_url = reverse_lazy('home')


class LoginUser(LoginView):
    form_class = AuthenticationForm
    template_name = 'news/login.html'

    def get_success_url(self):
        return reverse_lazy('home')


def logout_user(request):
    logout(request)
    return redirect('login')


def add_news(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            instance = News(user=User.objects.get(username=request.user))
            news = AddNewsForm(request.POST, instance=instance)
            news.save()
            return redirect('user_news')
        else:
            form = AddNewsForm
            data = {
                "form": form,
                "title": "Add news",
            }
            return render(request, template_name='news/add_news.html', context=data)
    else:
        return redirect('login')


def user_news(request):
    if request.user.is_authenticated:
        news = News.objects.filter(user=request.user)
        data = {
            "news": news,
            "title": "My news",
        }
        return render(request, template_name='news/user_news.html', context=data)
    else:
        return redirect('login')




