from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('nosotros/', views.nosotros, name='nosotros'),
    path('servicios/', views.servicios, name='servicios'),
    path('servicios/NivelacionEstudios.html', views.NivelacionEstudios, name='NivelacionEstudios'),
    path('servicios/ContinuidadEstudios.html', views.ContinuidadEstudios, name='ContinuidadEstudios'),
    path('servicios/Capacitacion.html', views.Capacitacion, name='Capacitacion'),
    path('servicios/ReclutamientoEnLinea.html', views.ReclutamientoEnLinea, name='ReclutamientoEnLinea'),
    path('servicios/ValidacionDeEstudios.html', views.ValidacionDeEstudios, name='ValidacionDeEstudios'),
    path('servicios/ArriendoDeMaquinaria.html', views.ArriendoDeMaquinaria, name='ArriendoDeMaquinaria'),
    path('noticias/', views.CardListView.as_view(), name='noticias'),
    path('add_card/', views.AddCardView.as_view(), name='add_card'),
    path('delete_card/<int:id>/', views.DeleteCardView.as_view(), name='delete_card'),
    path('contactanos/', views.contactanos, name='contactanos'),
    
]