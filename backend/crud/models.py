from django.db import models

# Create your models here.


class Subjects(models.Model):
    name = models.CharField( max_length=100)
    slug = models.SlugField(unique=True)


    def __str__(self):
        return self.name

class Tutor(models.Model):
    name = models.CharField( max_length=100)
    slug = models.SlugField(unique=True)
    portrait = models.ImageField(upload_to='tutors/portraits/', blank=True, null=True)
    short_bio= models.TextField( max_length=50000 )
    short_bio= models.TextField()
    years_experience = models.IntegerField(max_length=2)
    is_founder=models.BooleanField()
    is_featured=models.BooleanField()
    display_order= models.IntegerField(max_length=2)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name