# app/views.py
from rest_framework import generics, mixins
from .models import Product
from .serializers import ProductSerializer
from .tasks import import_excel_data
from rest_framework.response import Response

class ProductListCreateView(mixins.ListModelMixin, 
                            mixins.CreateModelMixin, 
                            generics.GenericAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

import os

class ProductImportExcelView(generics.GenericAPIView):
    def post(self, request, *args, **kwargs):
        file = request.FILES['file']
        
        # Construct the file path using os.path.join
        file_path = os.path.join(r"C:\Users\Rahul\Downloads", file.name)

        # Save the uploaded file to the specified path
        with open(file_path, 'wb') as f:
            for chunk in file.chunks():
                f.write(chunk)

        # Trigger the Celery task to process the uploaded file
        import_excel_data.delay(file_path)

        return Response({'message': 'File uploaded and processing started.'})
