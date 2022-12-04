from config import settings
from django.conf.urls.static import static
from django.urls import path
from .views import YoutubeConverter
from .logic import file_download

urlpatterns = [
    path('', YoutubeConverter.as_view(), name='converter'),
    path('download/<str:file_name>/', file_download, name='download')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
