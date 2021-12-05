from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
from django.urls import reverse


User = get_user_model()

# Create your models here.

class Todo(models.Model):
    title = models.CharField(_('Todo'), max_length=120)
    description = models.TextField(_('Todo Description'), blank=True)
    done = models.BooleanField(_("Todo status"), default=False)
    user = models.ForeignKey(User, verbose_name=_("Creator"), on_delete=models.CASCADE)


    date_created = models.DateTimeField(_("Date Created"), auto_now_add=True)
    date_updated = models.DateTimeField(_("Date Updated"), auto_now=True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("todo-detail", kwargs={"pk": self.pk})
    