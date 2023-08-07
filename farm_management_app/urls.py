from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('locations/', views.location_view, name='locations'),
    path('locations/bed/<slug:bed_name>/', views.bed_detail_view, name='bed'),
    path('cropplans/', views.cropplan_list, name='cropplans'),
    path('cropplans/<int:pk>/', views.cropplan_detail_view, name='cropplans-detail'),
    path('cropplans/new', views.cropplan_new, name='cropplans-new'),
    path('cropplans/<int:pk>/edit', views.cropplan_edit_view, name='cropplans-edit'),
    path('tasks/', views.TaskTableHtmx.as_view(), name='tasks'),
    path('tasks/<int:pk>/', views.task_detail_view, name='task-detail'),
    path('tasks/<int:pk>/edit', views.task_edit_view, name='task-edit'),
    path('tasks/<int:pk>/complete', views.task_complete, name='task-complete'),
    path('tasks/new', views.new_task, name='task-new'),
    path('cp_test/', views.CropPlanTableHtmx.as_view(), name='cp_test'),


]


