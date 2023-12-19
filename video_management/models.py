from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        abstract = True


class Video(BaseModel):
    file_name = models.CharField(max_length=80, null=False)
    file_content = models.FileField(upload_to='uploads/')
    file_path = models.CharField(max_length=150)

    def delete(self, *args, **kwargs):
        if self.file_content:
            storage, path = self.file_content.storage, self.file_content.path
            storage.delete(path)
        super().delete(*args, **kwargs)


class ClosedCaptions(BaseModel):
    video_id = models.ForeignKey(Video, on_delete=models.CASCADE)
    from_timestamp = models.TimeField(null=False)
    to_timestamp = models.TimeField(null=False)
    cc_text = models.TextField()

