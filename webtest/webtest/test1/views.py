from django.shortcuts import render, HttpResponse
from test1 import models
# Create your views here.


def lgzp(request, id1):

    info = models.lgzp1.objects.get(pk = id1)
    info = info.info
    return HttpResponse(info)
