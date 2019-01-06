from django.urls import path
from .views import person_list
from .views import person_new
from .views import person_update
from .views import person_delete
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('list/', person_list, name='person_list'),
    path('new/', person_new, name='person_new'),
    path('update/<int:id>/', person_update, name='prs_update'),
    path('delete/<int:id>/', person_delete, name='prs_delete'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
