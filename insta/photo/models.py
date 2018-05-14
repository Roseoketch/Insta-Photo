from django.db import models
from django.contrib.auth.models import User
from models import Profile
from . import models

# Create your models here.
class Image(models.Model):
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)
    caption = models.CharField(max_length = 60)
    upload_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile,on_delete=models.CASCADE)
    likes = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.caption
    class Meta:
        ordering = ['-upload_date']

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    @classmethod
    def update_caption(cls,id,caption):
        captioned = Image.objects.filter(id=id).update(caption = caption)
        return captioned

    @classmethod
    def get_images(cls):
        image = Image.objects.all()
        return image

    @classmethod
    def get_image_by_id(cls,id):
        image = Image.objects.filter(id=Image.id)
        return image
