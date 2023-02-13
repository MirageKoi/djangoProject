from django.urls import path
from . import views


urlpatterns = [
    path("", views.homepage, name="homepage"),
    path('form/', views.form_view, name='form-view'),
    path("task/", views.task_list_view, name="task_list_view"),
    path("task/<int:number>/", views.task_detailed_view, name="task_detailed_view")
]