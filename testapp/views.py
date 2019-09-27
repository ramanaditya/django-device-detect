from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings

# Create your views here.
def index(request):
    c = []
    c.append('Windows : '+ str(request.Windows))
    c.append('LINUX : ' + str(request.Linux))
    c.append('iMac : ' + str(request.iMac))
    c.append('iPhone : '+ str(request.iPhone))
    c.append('iPad : '+ str(request.iPad))
    c.append('iPod : '+ str(request.iPod))
    c.append('PC : '+ str(request.PC))
    c.append('iOS : ' + str(request.iOS))
    c.append('Android : ' + str(request.Android))
    c.append('Android Version : ' + str(request.Android.version))
    c.append('META : ' + str(request.META))
    return render(request, "index.html",{'c':c})
