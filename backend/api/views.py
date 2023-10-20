from rest_framework import generics
from .models import Compliance, Application
from .serializers import ComplianceSerializer, ApplicationCreateSerializer,ComplianceCreateSerializer

# Create Compliance 
class ComplianceListCreateView(generics.ListCreateAPIView):
    queryset = Compliance.objects.all()
    serializer_class = ComplianceCreateSerializer

# Get Compliance Details with Application Details
class ComplianceDetailViewiWithApplication(generics.ListCreateAPIView):
    queryset = Compliance.objects.all()
    serializer_class = ComplianceSerializer

# Create Apllication Details
class ApplicationListCreateView(generics.ListCreateAPIView):
    queryset = Application.objects.all()
    serializer_class = ApplicationCreateSerializer

