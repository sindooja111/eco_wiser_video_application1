from django.shortcuts import render
from video_management.models import Video
from .tasks import extract_cc
from django.conf import settings
import os


def index(request):
    data = Video.objects.all()
    return render(request, 'index.html', {'data': data})


def play_video(request, video_id):
    try:
        data = Video.objects.get(id=video_id)
        path = data.file_path.split('\\')[-1]
    except Exception as e:
        return render(request, 'failed.html')
    if data:
        return render(request, 'video_player.html', {"data": path})


def upload_video(request):
    return render(request, template_name='upload_video.html')


def save_video(request):
    if request.method == 'POST':
        title = request.POST.get('title', '')
        video_file = request.FILES.get('video_file', None)
        if title and video_file:
            exists = Video.objects.filter(file_name=title)
            if len(exists) == 0:
                file_path = 'media\\uploads\\' + video_file.name
                video = Video(file_name=title, file_content=video_file, file_path=file_path)
                video.save()
                extract_cc.delay(video_file.name)
                return render(request, 'success.html')

    return render(request, 'failed.html')


