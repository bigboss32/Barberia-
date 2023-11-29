from django.shortcuts import render

def index(request):
    
    return render(request, 'index.html')

def crear_cita(request):
    print(request.user)
    return render(request, 'compradores/Crear_comprador.html')
