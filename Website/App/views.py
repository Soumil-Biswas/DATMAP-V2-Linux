from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from . import main
# Create your views here.


def heading(request):
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        print(uploaded_file.name)
        print("{} Bytes" .format(uploaded_file.size))
        print(type(uploaded_file))
        fs = FileSystemStorage()
        fs.save(uploaded_file.name, uploaded_file)
        main.get_coordinates(uploaded_file)
    return render(request, 'App/DATMAP.html')
