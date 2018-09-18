from django.shortcuts import render


def home_page(request):
    context ={
        "title": "Hello World!",
        "welcome": "Welcome to the homepage",
        "premium_content": "YEAHHH"
    }
    # print(request.session.get('first_name', 'Unknown'))
    return render(request, "home_page.html", context)


def about_page(request):
    context ={
        "title": "About Page",
        "content": "Welcome to the about page",

    }
    return render(request, "about_page.html", context)
