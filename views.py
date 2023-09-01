from django.shortcuts import render

def index(request):
    return render(request, "portfolio/index.html")

def about(request):
    return render(request, "portfolio/about.html")

def project(request):
    return render(request, "portfolio/project.html")

def project1(request):
    return render(request, "portfolio/project1.html")
def project2(request):
    return render(request, "portfolio/project2.html")
def project3(request):
    return render(request, "portfolio/project3.html")



def experience(request):
    return render(request, "portfolio/experience.html")