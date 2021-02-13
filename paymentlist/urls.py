from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
from paymentlist import views

urlpatterns = [
    #homepage
    path('', views.all_payments, name='all_payments'),
    path('create', views.create_payments, name='create_payments'),
    path('edit/<int:trn_pk>', views.edit_payments, name='edit_payments'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)