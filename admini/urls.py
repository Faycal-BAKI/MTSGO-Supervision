from django.conf.urls import  url
from . import views

urlpatterns = [
    url(r'^stats/$', views.afficher_stats),  # Accès aux statistiques
    url(r'^questions/$', views.afficher_questions), #Affiche toutes les questions disponibles
    url(r'^ajout_question/$', views.ajout_question, name='ajout'),
    #url(r'^nouvellequestion$', views.creerquestion), #
    url(r'^ajout_spot/$', views.ajout_spot, name='ajout'),
    url(r'^carte/$', views.afficher_carte)
]
