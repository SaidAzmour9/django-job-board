from django.contrib.auth.models import User
from django.db import models
from django.utils.text import slugify

# Create your models here.

JOB_TYPE = (
    ('full time', 'full time'),
    ('part time', 'part time'),
)

def image_upload(instance, filename):
    imagename , extention = filename.split(".")
    return "jobs/%s.%s"%(instance.id,extention)

class Job(models.Model):
    owner = models.ForeignKey(User, verbose_name=("job_owner"), on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    job_type = models.CharField(max_length=15, choices=JOB_TYPE)
    description = models.TextField(max_length=1000)
    published_at = models.DateTimeField(auto_now=True)
    vacancy = models.IntegerField(default=0)
    salary = models.IntegerField(default=1)
    experience = models.IntegerField(default=1)
    category = models.ForeignKey('Category',on_delete=models.CASCADE)
    image = models.ImageField(upload_to=image_upload)
    slug = models.SlugField(blank=True,null=True)


   
    def save(self, *args, **kwargs):
       self.slug = slugify(self.title)
       super(Job, self).save(*args, **kwargs) # Call the real save() method

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Apply(models.Model):
    job = models.ForeignKey("Job", verbose_name=("apply_job"), on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    website = models.URLField( max_length=200)
    applyed_at = models.DateTimeField(auto_now=True)
    cv = models.FileField(upload_to=('apply/'))
    cover_letter = models.TextField(max_length=500)

    def __str__(self):
        return self.name