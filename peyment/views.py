from django.shortcuts import render

# Create your views here.


def peyment(request):
    context = {}
    return render(request, "peyment.html", context)
