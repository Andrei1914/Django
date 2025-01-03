from django.shortcuts import render

def main_page(request):
    return render(request, 'class_template.html')
