from django.urls import path
from .views import ComplianceListCreateView, ComplianceDetailViewiWithApplication, ApplicationListCreateView

# Defining the api urls here
urlpatterns = [
    path('compliances/', ComplianceListCreateView.as_view(), name='compliance-list'),
    path('compliances/with-application/', ComplianceDetailViewiWithApplication.as_view(), name='compliance-detail-with-application'),
    path('applications/', ApplicationListCreateView.as_view(), name='application-list'),
]
