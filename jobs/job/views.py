from rest_framework import generics

from .models import Job , JobApply
from .serializers import JobApplySerializers,JobSerializers

class JobListCreateAPI(generics.ListCreateAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializers


class JobDetailUpdateDeleteAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializers