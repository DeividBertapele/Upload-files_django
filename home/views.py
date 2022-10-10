from django.shortcuts import render
from django.http import HttpResponse
from PIL import Image
from .models import MyFile

# Create your views here.
def home(request):
    if request.method == "GET":
        return render(request, 'home.html')
    elif request.method == "POST":
        title = request.POST.get('title')
        file = request.FILES.get('my_file')

        if file.size > 2000000:
             return HttpResponse('Arquivo muito grande')

        mf = MyFile(title="minha_imagem", arq=file)
        mf.save()
        
        return HttpResponse('Enviado com sucesso')
        

 