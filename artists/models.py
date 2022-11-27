from django.db import models
# Create your models here.
from django.urls import reverse
from accounts.models import CustomUser
country_choice=(
    ('1','Việt Nam'),
    ('2','US-UK'),
    ('3','K-POP'),
    ('4','Hoa Ngữ'),
    ('5','Nhật Bản'),
    ('6','Khác'),
)
class Artist(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(default="A Popular Artist!")
    image=models.ImageField()
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE,null=True,related_name='singer')
    followers=models.ManyToManyField(CustomUser,blank=True,related_name="followers")
    slug=models.SlugField(max_length=50)
    country=models.CharField(max_length=50,default='1',choices=country_choice)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
    	return self.name
    def get_image(self):
        if self.image:
            return self.image.url
    def get_absolute_url(self):
        return reverse("detail", kwargs={"slug": self.slug})
    