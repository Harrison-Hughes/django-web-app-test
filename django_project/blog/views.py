from django.shortcuts import render

posts = [
    {
        'author': 'Harrison Hughes',
        'title': 'on a plane',
        'content': 'soaring, flying',
        'date_posted': 'September 25'
    },
    {
        'author': 'Cam Thom',
        'title': 'on a boat',
        'content': 'blub blub',
        'date_posted': 'September 23'
    }
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', {'posts': posts})


def about(request):
    return render(request, 'blog/about.html')
