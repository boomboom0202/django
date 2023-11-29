"""
URL configuration for note_tracker project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


from django.urls import path
from note_app.views import *
from django.contrib import admin

urlpatterns = [
    path('search/', search_notes, name='search_notes'),  
    path('search-page/', search_notes_page, name='search_notes_page'), 
    path('generate_report/', generate_report,name = 'generate_report'),
    path('', note_list, name = 'note_list'),
    path('notes/add/', add_note, name = 'add_note'),
    path('notes/<int:note_id>/',note_detail, name = 'note_detail')
]