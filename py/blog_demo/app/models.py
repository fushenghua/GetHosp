#coding:utf-8
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class job(models.Model):
    jobId=models.IntegerField(u'jobId',db_column='jobId',primary_key=True);
    jobImg = models.CharField(u'jobImg' ,max_length=300,db_column='jobImg')
    jobName = models.CharField(u'jobName', max_length=50,db_column='jobName')
    token = models.CharField(u'token', max_length=15,blank=True,db_column='token')

    class Meta:
        db_table = 'job'
        verbose_name = '工作'
        verbose_name_plural = '工作'

    #def __unicode__(self):
    #    return  '%s %s %s' % (self.full_name,self.address,self.tel)
def __str__(self):
    return  '%s %s %s' % (self.jobName,self.jobImg,self.token)
