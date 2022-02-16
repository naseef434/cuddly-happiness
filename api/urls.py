from unicodedata import name
from django import views
from django.urls import path
from . import views
urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.apiOverView, name="api over view"),
    path('task-list/',views.Tasklist, name="Task-list"),
    path('task-details/<str:pk>',views.TaskView, name="Task-View"),
    path('task-create/', views.TaskCreate, name="Task Create"),
    path('task-update/<str:pk>',views.TaskUpdate, name="TaskUpdate"),
    path('task-delete/<str:pk>',views.TaskDelete, name="TaskDelete"),
]
