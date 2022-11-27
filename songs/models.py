from django.db import models
# Create your models here.
from artists.models import Artist
from accounts.models import CustomUser
from django.urls import reverse
# Create your models here.
country_choice=(
    ('1',"Việt Nam"),
    ('2',"Âu Mỹ"),
    ('3',"Hàn Quốc"),
    ('4',"Nhật Bản"),
    ('5',"Hoa Ngữ"),
    ('6',"Hòa tấu"),
    ('7',"Khác"),
)

viewer_choice=(
    ('1','Cá nhân'),
    ('2','Công khai'),
)
class Album(models.Model):
    name=models.CharField(max_length=400)
    slug=models.SlugField(max_length=200,null=True)
    def get_absolute_url(self):
        return reverse("detail", kwargs={"slug": self.slug})
    def __str__(self):
        return self.name
class Genre(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
    	return self.name
    def get_absolute_url(self):
        return reverse("detail", kwargs={"slug": self.slug})

class Video(models.Model):
    file_preview=models.ImageField()
    file = models.FileField()
    created_at = models.DateTimeField(auto_now_add=True)
    user=models.ForeignKey(CustomUser,on_delete=models.CASCADE,related_name='video_uploader')
    duration=models.FloatField(default=0)
    likers=models.ManyToManyField(CustomUser,blank=True,related_name="mv_likers")
    def __str__(self):
        return self.file.url
class ShareMv(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    mv=models.ForeignKey(Video,on_delete=models.CASCADE)
    provider=models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
class Song(models.Model):
    name = models.CharField(max_length=100)
    image_cover=models.ImageField(null=True,default="/music.jpg")
    duration = models.FloatField()
    file = models.FileField()
    user=models.ForeignKey(CustomUser,on_delete=models.CASCADE,related_name='uploader')
    album=models.ForeignKey(Album,on_delete=models.SET_NULL,null=True,blank=True)
    video=models.ForeignKey(Video,on_delete=models.SET_NULL,null=True,blank=True)
    genre=models.ForeignKey(Genre,on_delete=models.SET_NULL,null=True,blank=True)
    artist_name=models.CharField(max_length=200)
    artists = models.ManyToManyField(Artist,blank=True,related_name='artists')
    hasLyric=models.BooleanField(default=False)
    lyrics=models.JSONField(null=True,blank=True)
    hasKaraoke=models.BooleanField(default=False)
    sentences=models.JSONField(null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    likers=models.ManyToManyField(CustomUser,blank=True,related_name="likers")
    viewer=models.CharField(max_length=50,choices=viewer_choice)
    country=models.CharField(max_length=50,choices=country_choice,default="7")
    def __str__(self):
    	return self.name

class View(models.Model):
    user=models.ForeignKey(CustomUser,on_delete=models.CASCADE,null=True)
    song=models.ForeignKey(Song,on_delete=models.CASCADE,related_name='song')
    created_at = models.DateTimeField(auto_now_add=True)
class Sharesong(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    song=models.ForeignKey(Song,on_delete=models.CASCADE)
    provider=models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
class Playlist(models.Model):
    user=models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    songs=models.ManyToManyField(Song,blank=True,related_name='songs')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name= models.CharField(max_length=100)
    slug = models.SlugField(max_length=150,null=True)
    public=models.BooleanField(default=True)
    ramdom_play=models.BooleanField(default=True)

class Shareplaylist(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    playlist=models.ForeignKey(Playlist,on_delete=models.CASCADE)
    provider=models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)