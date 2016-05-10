#coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse
from django.db import connection
from models import job
# Create your views here.
def index(request):
        # for j in job.objects.all():

        # return HttpResponse(u"hello tetst!"+str(j.jobId))
        return render(request, 'index.html', {'jobs': job.objects.all()})
