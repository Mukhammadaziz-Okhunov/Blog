from django.shortcuts import render
from blog1.models import Maqola, Rasm


def home(request):
    return render(request, "home.html")

def about(request):
    return render(request, "about.html")

def blog(request):
    maqolalar = Maqola.objects.all().order_by('-time')
    return render(request, "blog.html", {'maqolalar': maqolalar})

def maqola(request, son):
    son = Maqola.objects.get(id=son)
    rasmlar = Rasm.objects.filter(maqola=son)
    return render(request, "maqola.html", {'son': son, 'rasmlar': rasmlar})