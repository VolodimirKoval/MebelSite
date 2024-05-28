from django.shortcuts import render


def main_page(request):
    context = {
        'title': 'Main page',
    }
    
    return render(request, 'home/main.html', context=context)


def about_us(request):
    context = {
        'title': 'About',
    }
    
    return render(request, 'home/about_us.html', context=context)
