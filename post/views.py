from django.shortcuts import render
from .models import *
from comment.modesl import *
# Create your views here.
class Uploadpost(APIView):
    def post(self,request):
        user=request.user
        caption=request.POST.get('caption')
        file=request.POST.get('file')
        file_preview=request.POST.get('file_preview')
        post=Post.obhects.create(caption=captin,user=user)
        file=Fileuploadpost.objects.create(user=user,file=file,file_preview=file_preview,post=post)
        return Response({'success':True})

class Postdetail(APIView):
    def get(self,request,id):

    def post(self,request,id):
        post=Post.obhects.get(id=id)
        action=request.POST.get('action')
        if action=='update':
            caption=request.POST.get('caption')
            file=request.POST.get('file')
            file_id=request.POST.get('file_id')
            file_preview=request.POST.get('file_preview')
            post.caption=caption
            post.save()
            filepost=Fileuploadpost.objects.get(id=file_id)
            if file:
                filepost.file=file
            if file_preview:
                filepost.file_preview=file_preview
            filepost.save()
        elif action=='like':
            if user in post.likers.all():
                post.likers.remove(user)
            else:
                post.likers.add(user)
        elif action=='comment':
            body=request.POST.get('body')
            comment=Comment.objects.create(user=user,body=body,post=post)
        return Response({'success':True})