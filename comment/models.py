from django.db import models
from accounts.models import *
class Comment(models.Model):
    song = models.ForeignKey(to="songs.Song", on_delete=models.CASCADE, related_name='song_comments',null=True)
    post = models.ForeignKey(to="post.Post", on_delete=models.CASCADE, related_name='post_comments',null=True)
    playlist = models.ForeignKey(to="songs.Playlist", on_delete=models.CASCADE, related_name='playlist_comments',null=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, related_name='+')
    likers=models.ManyToManyField(CustomUser, related_name='likers_comment',blank=True)
    dislikers=models.ManyToManyField(CustomUser, related_name='dislikers_comment',blank=True)
    def count_reply(self):	
	    return Comment.objects.filter(parent=self).count()
    def count_like(self):
    	return self.likers.all().count()
    def count_dislike(self):
        	return self.dislikers.all().count()

