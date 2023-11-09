from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status, generics
from .models import CSVFile
from .serializers import CSVFileSerializer
from django.http import Http404
import csv



class CSVFileUploadView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, format=None):
        file = request.data.get("file")
        print(file.name)

        if file:
            # You can create an instance of the model and assign the file
            csv_file = CSVFile(file=file, name=file.name)
            csv_file.save()

            file_serializer = CSVFileSerializer(csv_file)
            return Response(file_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response({"error": "No file provided"}, status=status.HTTP_400_BAD_REQUEST)

class CSVFileListView(APIView):
    def get(self, request, format=None):
        days = ["Mon"]
        csv_files = CSVFile.objects.all()
        file_names = [csv_file.uploaded_at.strftime("%a, %d %b %Y %H:%M:%S GMT-") + str(csv_file.name) for csv_file in csv_files]

        response_data = {
            "fileNames": file_names
        }

        return Response(response_data)
   
class CSVFileDeleteView(generics.RetrieveDestroyAPIView):
    queryset = CSVFile.objects.all()
    serializer_class = CSVFileSerializer

    def get_object(self):
        fileName = self.kwargs.get('fileName')
        split = fileName.split("-")
        name = split[-1]
        datetime_str = split[0]
        try:
           for obj in CSVFile.objects.filter(name=name):
                if(obj.uploaded_at.strftime("%a, %d %b %Y %H:%M:%S GMT") == datetime_str):
                    return obj
        except CSVFile.DoesNotExist:
            return Http404
        
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance:
            with open(instance.file.path, 'r', encoding='utf-8') as csv_file:
                csv_reader = csv.DictReader(csv_file)
                csv_data = list(csv_reader)

            return Response(csv_data, status=status.HTTP_200_OK)
        else:
            return Response({'detail': 'CSVFile not found.'}, status=status.HTTP_404_NOT_FOUND)

        
    def perform_destroy(self, instance):
        instance.file.delete()  # Delete the associated CSV file
        instance.delete()
        return Response({"message" : "File deleted successfully"}, status=status.HTTP_200_OK)