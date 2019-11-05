from django import forms
from markdownx.fields import MarkdownxFormField
from markdownx.widgets import MarkdownxWidget

class AddNoteForm(forms.Form):
    tags = forms.CharField(widget=forms.Textarea(attrs={"rows":1, "cols":120}))
    note = MarkdownxFormField(widget=MarkdownxWidget(attrs={"rows":6, "cols":120}))
    def clean_data(self):
        tags = self.cleaned_data['tags']
        note = self.cleaned_data['note']
        return tags, note

