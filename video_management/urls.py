from django.urls import path
from video_management.views import upload_video, save_video, index, play_video

urlpatterns = [
    path('', index),
    path('upload-video', upload_video, name='upload-video'),
    path('save-video', save_video, name='save-video'),
    path('play-video/<int:video_id>/', play_video, name='play-video')
]
