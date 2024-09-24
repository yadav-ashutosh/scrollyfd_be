from django.urls import path
from . import views  # Import your app's views

urlpatterns = [
    path('', views.wwe_view, name='wwe_page'),  # The root of 'wwe/' goes to the view
]