from django.urls import path
from video_management.views import index, save_video

urlpatterns = [
    path('upload-video', index),
    path('save-video', save_video, name='save-video'),
]
