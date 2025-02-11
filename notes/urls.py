from django.urls import path
from . import views

urlpatterns = [
    path('newnote/',views.newnote,name="newnote"),
    path('getnotes/',views.getnotes,name="getnotes"),
    path('deletenote/<int:note_id>/',views.deletenote,name="deletenote"),
    path('share/<int:note_id>/', views.share_note, name='share_note'),
]
