from django.urls import path
from .views import FetchCitationsView

urlpatterns = [
    path('fetch-citations/', FetchCitationsView.as_view(), name='fetch_citations'),
]
