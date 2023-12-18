from eco_wiser_video_application.celery import app
from time import sleep
import os
import subprocess
from django.conf import settings

from video_management.ccextraction import generate_cc_from_file


@app.task(bind=True)
def extract_cc(video_file):
    process_soft = os.path.join(settings.BASE_DIR, 'video_management', 'CCExtractor_win_portable', 'ccextractorwinfull.exe')
    mode = '-o'
    output_file = os.path.join(settings.BASE_DIR, 'media', 'uploads', video_file.name + '_subtitles.srt')
    video_url = os.path.join(settings.BASE_DIR, 'media', 'uploads', video_file.name)

    try:
        p = subprocess.run([process_soft, video_url, mode, output_file], stdout=subprocess.PIPE)
        if p.stdout is not None:
            return generate_cc_from_file(output_file)
        else:
            print("No output captured.")

    except Exception as e:
        print('', e)
