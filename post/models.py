from django.db import models
from accounts.models import *
from artists.models import *
# Create your models here.
viewer_choice=(
    ('1','Public'),
    ('2','Friend'),
    ('3','Excepttion people'),
    ('4','Private'),
    ('5','Specific friends'),
    ('6','Custom'),
    ('7','Best friend'),
    ('8','Unnamed list'),
    ('9','Acquaintance'),
)

class Post(models.Model):
    caption = models.TextField(max_length=1500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    viewer=models.CharField(max_length=100,choices=viewer_choice,default="1")
    likers=models.ManyToManyField(CustomUser,blank=True,related_name='likers_post')
    
    def __str__(self):
    	return self.user.username
    def count_file(self):
        return Fileuploadpost.objects.filter(post=self).count()
    def count_comment(self):
        return Comment.objects.filter(post=self).count()
    def count_comment_parent(self):
        return Comment.objects.filter(post=self,parent=None).count()
    
class Fileuploadpost(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    post=models.ForeignKey(Post, on_delete=models.CASCADE,related_name='file_post')
    file= models.FileField(upload_to='post/')
    file_preview=models.ImageField(upload_to='post/',null=True)
    duration=models.FloatField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    def get_file_preview(self):
        if self.file_preview and hasattr(self.file_preview,'url'):
            return self.file_preview.url

class Sharepost(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    post=models.ForeignKey(Post,on_delete=models.CASCADE)
    provider=models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    