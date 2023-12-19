from video_management.models import ClosedCaptions


def generate_cc_from_file(data_file, video_file):
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
        subtitles_list.append(
            ClosedCaptions(from_timestamp=from_timestamp, to_timestamp=to_timestamp, cc_text=subtitle_text,
                           video_id=video_file))
    if subtitles_list:
        print(subtitles_list)
        ClosedCaptions.objects.bulk_create(subtitles_list)


