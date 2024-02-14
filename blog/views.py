from django.shortcuts import render

# Create your views here.


# Represent landing page
def main(request):
    context = {}
    return render(request, "main.html", context)


# Represent about us page
def about_us(request):
    return render(request, "about_us.html")
