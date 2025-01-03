from django.shortcuts import render

def main_page(request):
    return render(request, 'main.html')

def game_page(request):
    return render(request, 'games.html')

def basket_page(request):
    return render(request, 'basket.html')
