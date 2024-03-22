from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author' : 'Ebube Joshua',
        'title' : 'Blog Post 1',
        'content' : 'First Post content',
        'date_posted' : 'March 16, 2024'
    },
    
    {
        'author' : 'Ebube Joshua',
        'title' : 'Blog Post 2',
        'content' : 'Second Post content',
        'date_posted' : 'March 16, 2024'
    }
]


context = {
    'posts': posts
}

# Create your views here.
def home(request):
    return render(request, 'main/index.html', context)

def about(request):
    return render(request, 'main/about.html', { 'title': 'About' })