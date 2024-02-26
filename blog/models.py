from django.db import models
from ckeditor.fields import RichTextField

# from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.


class MyBaseModel(models.Model):
    is_active = models.BooleanField(verbose_name="Is active", default=False)
    created_at = models.DateTimeField(
        verbose_name="date created", auto_now_add=True)
    updated_at = models.DateTimeField(
        verbose_name="date updated", auto_now=True)

    class Meta:
        abstract = True
        ordering = ("pk",)

    def __str__(self):
        raise NotImplementedError("Implement __str__ method!")


class Category(MyBaseModel):
    title = models.CharField(
        max_length=250, null=False, blank=False, verbose_name="title"
    )
    description = RichTextField(
        null=False, blank=False, verbose_name="description")

    def __str__(self):
        return self.title


class Post(MyBaseModel):
    categories = models.ManyToManyField("Category", related_name="posts")
    title = models.CharField(max_length=250, null=False, blank=False)
    body = RichTextField()

    def __str__(self):
        return self.title


class Comment(MyBaseModel):
    author = models.CharField(max_length=60)
    body = models.TextField()
    post = models.ForeignKey("Post", on_delete=models.CASCADE, related_name='comments')

    def __str__(self):
        return self.author


class Video(MyBaseModel):
    post = models.ForeignKey(
        "Post", on_delete=models.CASCADE, related_name="videos")
    title = models.CharField(max_length=255)
    video_file = models.FileField(upload_to="blog_videos/")
    description = RichTextField(blank=True)

    def __str__(self):
        return self.title


class Image(MyBaseModel):
    post = models.ForeignKey(
        "Post", on_delete=models.CASCADE, related_name="images")
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to="blog_images/")
    description = RichTextField(blank=True)

    def __str__(self):
        return self.title


class Audio(MyBaseModel):
    post = models.ForeignKey(
        "Post", on_delete=models.CASCADE, related_name="audios")
    title = models.CharField(max_length=255)
    audio_file = models.FileField(upload_to="blog_audios/")
    description = RichTextField(blank=True)

    def __str__(self):
        return self.title
