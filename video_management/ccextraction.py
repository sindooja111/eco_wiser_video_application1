import subprocess
import os
from django.conf import settings


def generate_cc_from_file(data_file):
    file_path = data_file
    with open(file_path, 'r') as file:
        file_content = file.read()
    subtitle_blocks = file_content.strip().split('\n\n')
    subtitles_list = []
    for block in subtitle_blocks:
        lines = block.split('\n')
        timestamp_range = lines[1]
        subtitle_text = ' '.join(lines[2:]).strip()
        from_timestamp, to_timestamp = timestamp_range.split(' --> ')
        subtitle_entry = {
            'from_timestamp': from_timestamp,
            'to_timestamp': to_timestamp,
            'text': subtitle_text
        }
        subtitles_list.append(subtitle_entry)
    for subtitle in subtitles_list:
        print(subtitle)
    return subtitles_list


def extract_cc(video_file):
    process_soft = os.path.join(settings.BASE_DIR,'video_management', 'CCExtractor_win_portable\\ccextractorwinfull.exe')
    mode = '-o'
    output_file = video_file.name + '_subtitles.srt'
    video_url = os.path.join(settings.BASE_DIR, 'media', 'uploads', video_file.name)
    try:
        p = subprocess.run([process_soft,
                            video_url, mode, output_file],
                           stdout=subprocess.PIPE)
        if p.stdout is not None:
            return generate_cc_from_file(output_file)
        else:
            print("No output captured.")

    except Exception as e:
        print('', e)
