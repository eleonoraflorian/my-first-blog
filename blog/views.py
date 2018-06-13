from django.shortcuts import render
from django.core.urlresolvers import reverse

def post_list(request):
    return render(request, 'blog/post_list.html', {})
