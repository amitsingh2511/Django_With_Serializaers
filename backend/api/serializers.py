from rest_framework import serializers
from .models import Compliance, Application

# Serializer For Create Application with compliance id
 
class ApplicationCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = ['id', 'name', 'product_name', 'compliance']

# Serializer For Get Application Deatils
class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = ['id', 'name', 'product_name']

# Serializer For Create Compliance Deatils
class ComplianceCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Compliance
        fields = ['id', 'name']

# Serializer For Get Compliance Deatils With application details
class ComplianceSerializer(serializers.ModelSerializer):
    applications = ApplicationSerializer(many=True, read_only=True)

    class Meta:
        model = Compliance
        fields = ['id', 'name', 'applications']
