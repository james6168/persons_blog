from django.urls import path
from . import views

urlpatterns = [
    path("blogs/", views.BlogListCreateAPIView.as_view()),
    path("blogs/<int:pk>/", views.BlogUpdateDeleteGetAPIView.as_view()),
    path("categories/", views.CategoriesListAPIView.as_view())
]