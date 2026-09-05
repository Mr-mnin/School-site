from django.db import models

# Create your models here.


#Our Tutors Tutors Domain

class Tutor(models.Model):
    name = models.CharField(max_length=150)
    slug = models.SlugField(unique=True)
    portrait = models.ImageField(
        upload_to='tutors/portraits/',
        blank=True,
        null=True
        )
    
    short_bio = models.CharField(max_length=250)
    full_bio = models.TextField()
    years_experience = models.IntegerField()
    is_founder = models.BooleanField(default=False)
    is_featured = models.BooleanField(default=False)
    display_order = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['display_order']
        verbose_name_plural = 'Tutors'

    def __str__(self):
        return self.name
    
class Subjects(models.Model):
    name = models.CharField( max_length=100)
    slug = models.SlugField(unique=True)
    tutors = models.ManyToManyField( 
        Tutor, 
        related_name='subjects', 
        blank=True 
        )
    created=models.DateTimeField(auto_now_add=True)
    modified=models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name']
        verbose_name_plural = 'Subjects'

    def __str__(self):
        return self.name

class Credentials(models.Model):
    tutor = models.ForeignKey( Tutor, on_delete=models.CASCADE )
    label = models.CharField(max_length=150)
    display_order = models.PositiveIntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['tutor', 'display_order']
        verbose_name_plural = 'Credentials'


    def __str__(self):
        return f"{self.label} – {self.tutor.name}"


#Services Domain

class Service(models.Model):
    title=models.CharField(max_length=150)
    slug=models.SlugField(unique=True)
    icon=models.CharField(max_length=50, blank=True)
    short_description=models.CharField(max_length=250)
    full_description= models.TextField()
    display_order=models.PositiveIntegerField(default=0)
    created=models.DateTimeField(auto_now_add=True)
    modified=models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['display_order']

    def __str__(self):
        return self.title

class ServiceInclusion(models.Model):
    service=models.ForeignKey(
        Service, 
        on_delete=models.CASCADE, 
        related_name='inclusions'
        )
    label=models.CharField(max_length=250)
    display_order=models.PositiveIntegerField(default=0)
    created=models.DateTimeField(auto_now_add=True)
    modified=models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['display_order']
        verbose_name_plural = 'Service inclusions'

    def __str__(self):
        return self.label[:50]


#About / Philosophy 
# .About Domain


class Value(models.Model):
    title= models.CharField(max_length=100)
    description=models.TextField()
    icon=models.CharField(max_length=50, blank=True)
    display_order=models.PositiveIntegerField(default=0)
    created=models.DateTimeField(auto_now_add=True)
    modified=models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['display_order']

    def __str__(self):
        return self.title

class Stat(models.Model):
    label=models.CharField(max_length=150)
    value=models.CharField(max_length=50)
    display_order=models.PositiveIntegerField(default=0)
    created=models.DateTimeField(auto_now_add=True)
    modified=models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['display_order']

    def __str__(self):
        return self.label

#Results / Testimonials
# Results Domain

class Testimonial(models.Model):
    name=models.CharField(max_length=150)
    slug=models.SlugField(unique=True)
    portrait=models.ImageField(
        upload_to='testimonials/portraits/',
        blank=True,
        null=True
        )
    quote=models.TextField()
    result=models.CharField(max_length=150, blank=True)
    rating=models.PositiveIntegerField(default=5)
    is_featured=models.BooleanField(default=False)
    display_order=models.PositiveIntegerField(default=0)
    created=models.DateTimeField(auto_now_add=True)
    modified=models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created']
        verbose_name_plural = 'Testimonials'

    def __str__(self):
        return f"{self.name} – {self.result}"
    
#Resources · Site Content
#Optional Domain

class Resources(models.Model):
    title=models.CharField(max_length=150)
    description=models.TextField()
    slug=models.SlugField(unique=True)
    resource_type=models.CharField(max_length=100)
    resource_file=models.FileField(upload_to='resources/files/')
    resource_external_link=models.URLField(blank=True)
    is_published=models.BooleanField(default=False)
    created=models.DateTimeField(auto_now_add=True)
    modified=models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.title

class Site_Content(models.Model):
    key=models.CharField(max_length=150)
    content=models.TextField()
    slug=models.SlugField(unique=True)
    page=models.CharField(max_length=150)
    section=models.CharField(max_length=150)
    is_published=models.BooleanField(default=False)
    created=models.DateTimeField(auto_now_add=True)
    modified=models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['page', 'section', 'key']
        verbose_name_plural = 'Site content'

    def __str__(self):
        return self.key

#Contact / Enquire
# Contact Domain

class Contact(models.Model):
    name=models.CharField(max_length=150)
    email=models.EmailField()
    student_year=models.CharField(max_length=50)
    subject_interest=models.CharField(max_length=250)
    message=models.TextField()
    status=models.BooleanField(default=False)
    created=models.DateTimeField(auto_now_add=True)
    modified=models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created']
        verbose_name_plural = 'Enquiries'

    def __str__(self):
        return f"{self.name} – {self.subject_interest} -({self.email})"
     