from .models import Patient,Doctor
from rest_framework import serializers

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ['username', 'password']
    

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ['id', 'rating','numberOfVoters']

    def update(self, instance, newRating):
        instance.rating =  newRating
        instance.numberOfVoters = instance.numberOfVoters + 1
        instance.save()
        return instance
