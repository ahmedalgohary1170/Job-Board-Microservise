from rest_framework import generics
from .models import Job , JobApply
from .serializers import JobApplySerializers,JobSerializers

# pagination
from .pagination import Jobspagination

# filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from .filters import JobFilter



class JobListCreateAPI(generics.ListCreateAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializers
    filter_backends = [DjangoFilterBackend,filters.SearchFilter]
    filterset_class = JobFilter
    pagination_class = Jobspagination

class JobDetailUpdateDeleteAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializers