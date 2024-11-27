from typing import Iterable
from django.db import models
from django.utils import timezone
from django.utils.text import slugify





JOB_TYPE = (
    ('Internship','Internship'),
    ('PartTime','PartTime'),
    ('FullTime','FullTime'),
    ('Contrect','Contrect'),
)

EDUCATION_TYPE = (    
    ('PHD','PHD'),
    ('Master','Master'),
    ('Bachelor','Bachelor'),
    )

EXPERIENCE_TYPE = (    
    ('NoExperience','NoExperience'),
    ('Junior','Junior'),
    ('MidLivil','MidLivil'),
    ('Senior','Senior'),
    )

class Job(models.Model):

    title = models.CharField(max_length=120)
    description = models.TextField(max_length=20000)
    job_type = models.CharField(choices=JOB_TYPE,max_length=20)
    education = models.CharField(choices=EDUCATION_TYPE,max_length=20)
    exprience = models.CharField(choices=EXPERIENCE_TYPE,max_length=20)
    salary = models.IntegerField(null=True,blank=True)
    position = models.CharField(max_length=100)
    due_date = models.DateField()
    created_at = models.DateTimeField(default=timezone.now)
    slug = models.SlugField(null=True,blank=True)
    user = models.IntegerField()
    company = models.CharField(max_length=40)


    def save(self,*args,**kwargs) :
        self.slug = slugify(self.title)
        return super(Job,self).save(*args,**kwargs)
    
    def __str__(self):
        return self.title
    

class JobApply(models.Model):
    user = models.IntegerField()
    job = models.ForeignKey(Job,related_name='applied_job',on_delete=models.CASCADE)
    resume = models.FileField(upload_to='resumes')
    cover_letter = models.TextField(max_length=1000)
    applied_at = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return str(self.job)