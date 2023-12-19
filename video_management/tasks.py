from eco_wiser_video_application.celery import app
from time import sleep
import os
import subprocess
from django.conf import settings


@app.task(bind=True)
def extract_cc(self, video_file_name):
    from video_management.ccextraction import generate_cc_from_file
    from video_management.models import Video

    process_soft = os.path.join(settings.BASE_DIR, 'video_management', 'CCExtractor_win_portable', 'ccextractorwinfull.exe')
    mode = '-o'
    output_file = os.path.join(settings.BASE_DIR, 'media', 'uploads', video_file_name + '_subtitles.srt')
    video_file = Video.objects.filter(file_path='media\\uploads\\' + video_file_name)
    video_url = None
    if len(video_file) > 0:
        video_url = video_file[0].file_path
    try:
        if video_url is not None:
            p = subprocess.run([process_soft, video_url, mode, output_file], stdout=subprocess.PIPE)
            if p.stdout is not None:
                return generate_cc_from_file(output_file, video_file[0])
            else:
                print("No output captured.")

    except Exception as e:
        print('', e)
