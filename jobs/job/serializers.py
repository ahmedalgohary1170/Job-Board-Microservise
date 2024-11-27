from rest_framework import serializers
from .models import Job , JobApply






class JobSerializers(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = '__all__'




class JobApplySerializers(serializers.ModelSerializer):
    class Meta:
        model = JobApply
        fields = '__all__'



