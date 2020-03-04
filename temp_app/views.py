from django.shortcuts import render
import os
from django.conf import settings
from django.http import HttpResponse, Http404


# Create your views here.
def home(request):
    return render(request, 'temp_app/index.html')


def download(request):
    file_path = os.path.join(settings.STATIC_ROOT, 'Alex_Jolly_Resume.pdf')
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/pdf")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            return response
    raise Http404
