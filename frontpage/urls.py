from django.urls import path
from .views import index_view
from  frontpage import views


urlpatterns = [
    path('index.html', index_view),
    path('', index_view),
]
