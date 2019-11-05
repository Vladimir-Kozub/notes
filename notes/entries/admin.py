from django.contrib import admin
from .models import Entry
from .forms import AddNoteForm

# Register your models here.
admin.site.register(Entry)


class EntryForm(admin.TabularInline):
    model = Entry # from models.py
    form = AddNoteForm