from django.shortcuts import render

# Create your views here.
def indexView(request):
    return render(request, "index.html", {})

# Create render of publicaciobnes.
def publicaciones(request):
    return render(request, "publicaciones.html", {})

#Create render of nosotros
def nosotros(request):
    return render(request, "nosotros.html", {})