from django.db import models
from markdownx.models import MarkdownxField
from markdownx.utils import markdownify
from datetime import datetime, timedelta
# Create your models here.


def get_my_datetime():
    return datetime.now() + timedelta(hours=3)

class Entry(models.Model):
    timestamp = models.DateTimeField(default=get_my_datetime, blank=True)
    tags = models.CharField(max_length=100, help_text="tags for structurazing", blank=True, default = 'No tags')
    note = MarkdownxField(help_text="note body")
    class Meta:
        ordering = ["-timestamp"]

    @property
    def formatted_markdown(self):
        return markdownify(self.note)

    def __str__(self):
        """
        String for representing the Model object
        """
        return '%s, %s str' % (self.timestamp, self.tags)
