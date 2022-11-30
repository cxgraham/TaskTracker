from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('register', views.register, name = 'register'),
    path('login', views.login, name = 'login'),
    path('logout', views.logout, name = 'logout'),
    path('homepage', views.homepage, name = 'homepage'),
    path('new_task', views.new_task, name = 'new_task'),
    path('tasks/edit/<int:id>', views.edit_task, name = 'edit_task'),
    path('tasks/delete/<int:id>', views.delete_task),
    path('homepage/filter/by_priority',  views.filter_tasks_by_priority, name = 'filtered_tasks')
]