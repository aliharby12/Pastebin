from django.db import models
from django.contrib.auth import get_user_model
from django.utils.crypto import get_random_string
from django.db.models.signals import post_save
from django.dispatch import receiver

from project.pastebin.models.abstracts import TimeStampedModel
from project.pastebin.utils import PathAndRename
from .validator import validate_file_extension

user = get_user_model()


class Paste(TimeStampedModel):
    """database table for pastes"""
    user = models.ForeignKey(user, on_delete=models.CASCADE, related_name='pastes')
    text = models.TextField(null=True, blank=True)
    text_file = models.FileField(
        upload_to=PathAndRename('pastes/files/'), null=True, blank=True,
        validators=[validate_file_extension]
    )
    name = models.CharField(max_length=5, null=True, blank=True)
    slug = models.CharField(max_length=8, null=True, blank=True)
    accessed = models.PositiveIntegerField(default=0)
    destroyable = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.text

    def save(self, *args, **kwargs):
        if not self.name:
            self.name=get_random_string(5)
        if not self.slug:
            self.slug=get_random_string(8)
        super(Paste, self).save(*args, **kwargs)


@receiver(post_save, sender=Paste)
def retrieve_text(sender, **kwargs):
    paste = kwargs['instance']
    if paste.text_file:
        text_in_file = open(paste.text_file.path).read()
        if paste.text == text_in_file:
            return
        else:
            paste.text = text_in_file
        paste.save()
    else:
        return