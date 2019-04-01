from django.http import HttpResponse
from django.shortcuts import render
from .models import Post
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from django.views.generic.detail import DetailView

from django.template.defaultfilters import slugify
import datetime




def homePageView(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/index.html', {'posts': posts})
   


def get_redirected(queryset_or_class, lookups, validators):
    """
    Calls get_object_or_404 and conditionally builds redirect URL
    """
    obj = get_object_or_404(queryset_or_class, **lookups)
    for key, value in validators.items():
        if value != getattr(obj, key):
            return obj, obj.get_absolute_url()
    return obj, None

def my_view(request, slug, id):
    article, article_url = get_redirected(Article, {'pk': id}, {'slug': slug})
    if article_url:
        return redirect(article_url)