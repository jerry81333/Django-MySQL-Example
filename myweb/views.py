from django.shortcuts import render

# Create your views here.

from myweb.models import IMG
from myweb.models import ART
from myweb.models import VID
from myweb.models import MUS
from myweb.models import VIDEO

def uploadImg(request):

    if request.method == 'POST':
        new_img = IMG(
            img=request.FILES.get('img'), 
            title=request.POST['imgtitle'], 
        )
        #new_img.title=request.GET['imgtitle']
        new_img.save()

    return render(request, 'uploadimg.html')

def uploadArt(request):

    if request.method == 'POST':
        new_art = ART(
            content=request.POST['content'], 
            title=request.POST['arttitle'], 
        )
        new_art.save()

    return render(request, 'articleupload.html')

def uploadMus(request):
    if(request.method=='POST'):
        new_mus = MUS(
            title = request.POST['mustitle'],
            mus = request.FILES.get('mus'),
            )
        new_mus.save()
    return render(request, 'musicupload.html')

def uploadVideo(request):
    if(request.method=='POST'):
        new_video = VIDEO(
            title = request.POST['videotitle'],
            vid = request.FILES.get('video'),
            )
        new_video.save()
    return render(request, 'videoupload.html')

def showImg(request):
    imgs = IMG.objects.all()
    articles = ART.objects.values('title')
    videos = VID.objects.values('title')
    musics = MUS.objects.values('title')
    videos2 = VIDEO.objects.values('title')
    content = {
    'imgs':imgs,
    'articles':articles,
    'videos':videos,
    'musics':musics,
    'videos2':videos2,
    }
    return render(request, 'showimg.html', content)

def exshow(request,typle,tit):
    if(typle=='img'):
        imgs = IMG.objects.filter(title=tit)
        content = {
        'imgs':imgs,
        }
        return render(request, 'img.html', content)
    if(typle=='article'):
        articles = ART.objects.filter(title=tit)
        content = {
        'articles':articles,
        } 
        return render(request,'article.html',content)
    if(typle == 'video'):
        videos = VID.objects.filter(title=tit)
        content = {
        'videos':videos,
        }
        return render(request,'video.html',content)
    if(typle == 'music'):
        musics = MUS.objects.filter(title=tit)
        content = {
        'musics':musics,
        }
        return render(request,'music.html',content)
    if(typle == 'video2'):
        videos2 = VIDEO.objects.filter(title=tit)
        content = {
        'videos2':videos2,
        }
        return render(request,'video2.html',content)
