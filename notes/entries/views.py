from django.shortcuts import render
from .models import Entry
from .forms import AddNoteForm
from django.http import HttpResponseRedirect

# Create your views here.
def index(request):
    # Если данный запрос типа POST, тогда
    if request.method == 'POST':
        form = AddNoteForm(request.POST)

        # Проверка валидности данных формы:
        if form.is_valid():
            Entry.objects.create(tags = form.clean_data()[0], note = form.clean_data()[1])
            return HttpResponseRedirect('/entries/')

    # Если это GET (или какой-либо еще), создать форму по умолчанию.
    else:
        form = AddNoteForm(initial={'tags': 'no tags', 'note' : 'what\'s new?' })

    return render(
        request,
        'index.html',
        context={'entry_list': Entry.objects.all(), 'form' : form},
    )


def del_entry(request,del_id):
    Entry.objects.get(id = del_id).delete()
    return HttpResponseRedirect('/entries/')
