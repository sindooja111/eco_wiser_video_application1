from django.shortcuts import render
from video_management.models import Video
from tasks import extract_cc


def index(request):
    return render(request, template_name='index.html')


def save_video(request):
    if request.method == 'POST':
        title = request.POST.get('title', '')
        video_file = request.FILES.get('video_file', None)
        if title and video_file:
            exists = Video.objects.filter(file_content__icontains=video_file)
            if len(exists) == 0:
                video = Video(file_name=title, file_content=video_file)
                video.save()
                cc_data = extract_cc.delay(video)
                return render(request, 'success.html')

    return render(request, 'failed.html')


