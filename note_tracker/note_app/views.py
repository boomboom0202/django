
from django.shortcuts import get_object_or_404, redirect, render

from django.http import HttpResponse
from django.template.loader import render_to_string
from django.core.files.temp import NamedTemporaryFile
from django.http import FileResponse
from note_app.forms import NoteForm
from .models import Note

def note_list(request):
    notes = Note.objects.all()
    return render(request, 'app/index.html', {'notes': notes})

def note_detail(request, note_id):
    note = Note.objects.get(pk=note_id) 
    return render(request, 'app/note_detail.html', {'note': note})

def add_note(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('note_list')
    else:
        form = NoteForm()
    return render(request, 'app/add_note.html', {'form': form})

from django.conf import settings

def generate_report(request):
    if 'title' in request.GET:
        title_to_search = request.GET['title']
        notes = Note.objects.filter(title__icontains=title_to_search)

        report_content = "Результат поиска'{}':\n\n".format(title_to_search) 
        for note in notes:
            report_content += f"Заголовок: {note.title}\nОписание: {note.text}\n\n"

        response = HttpResponse(report_content, content_type='text/plain')
        response['Content-Disposition'] = 'attachment; filename="search_results.txt"'
        return response
    else:
        return HttpResponse("Поисковый запрос не указан.")
    
def search_notes_page(request):
    return render(request, 'app/search.html') 

def search_notes(request):
    if 'title' in request.GET: 
        title_to_search = request.GET['title']  
        notes = Note.objects.filter(title__icontains=title_to_search)
        return render(request, 'app/search_results.html', {'notes': notes, 'search_term': title_to_search})
    else:
        return render(request, 'app/search_results.html', {'notes': None, 'search_term': None})