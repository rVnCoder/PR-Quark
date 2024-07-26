# views.py
import os
from django.shortcuts import render
from django.http import HttpResponse
from .models import FilesUpload
import subprocess
global name 
def naming( file) :
    name = file
def home(request):
    if(request.method == 'POST'):
        file2 = request.FILES["file"]
        print(file2)
        naming(file2)
        document= FilesUpload.objects.create(file=file2)
        document.save()
        # command1 = ["cd","media","&","quark","-a",str(file2),"-s","-w","test.html"]
        media_path = os.path.join("C:", "Users", "rajav", "OneDrive", "Desktop", "Pr-qurak", "media")
        file_path = os.path.join(media_path, str(file2))
        print(file_path)
        command1 = ["cd","media","&","quark","-a",str(file2),"-o","test.json","&","quark","-a",str(file2),"-s","-w","test.html","&","cd","AndroBugs_Framework-v1.0.0-windows","&","androbugs.exe","-f",file_path]
        try:
            result1 = subprocess.run(command1,shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            output1 = result1.stdout if result1.stdout else result1.stderr
            return render(request,'output.html')
        except subprocess.CalledProcessError as e:
            return HttpResponse(f"Command failed: {e}", status=500)
    return render(request, 'template.html')
def run_command(request):
    if 'run_command' in request.GET:
        command1 = ["cd","media","&","quark","-a","Ahmyth.apk","-s","-w","test.html"]
        try:
            result1 = subprocess.run(command1,shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            output1 = result1.stdout if result1.stdout else result1.stderr
            return render(request,'output.html')
        except subprocess.CalledProcessError as e:
            return HttpResponse(f"Command failed: {e}", status=500)
    return render(request, 'template.html')


