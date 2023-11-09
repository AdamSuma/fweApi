from django.urls import path
from .views import CSVFileUploadView, CSVFileListView, CSVFileDeleteView

urlpatterns = [
    path('upload/', CSVFileUploadView.as_view(), name='file-upload'),
    path('files/', CSVFileListView.as_view(), name="files-read"),
    path('files/<str:fileName>/', CSVFileDeleteView.as_view(), name='csvfile-delete'),
]