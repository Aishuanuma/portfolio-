# urls.py
from django.urls import path
from . import views
from .views import portfolio_setup, create_project, edit_project, delete_project
urlpatterns = [
    path('profile/', views.profile, name='profile'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('create_profile/', views.create_profile, name='create_profile'),
    path('portfolio_setup/', portfolio_setup, name='portfolio_setup'),
    path('create_project/', create_project, name='create_project'),
    
    path('edit_project/<int:project_id>/', edit_project, name='edit_project'),
    path('delete_project/<int:project_id>/', delete_project, name='delete_project'),
    path('project_list/', views.project_list, name='project_list'),
    path('project/create/',create_project,name='create_project'),
    path('index/',views.index,name='index'),
    path('projects/<int:project_id>/', views.project_detail, name='project_detail'),



    path('work_experience/', views.work_experience_list, name='work_experience_list'),
    path('work_experience/create/', views.create_work_experience, name='create_work_experience'),
    path('work_experience/edit/<int:pk>/', views.edit_work_experience, name='edit_work_experience'),
    path('work_experience/delete/<int:pk>/', views.delete_work_experience, name='delete_work_experience'),
    

    path('certifications/', views.certification_list, name='certification_list'),
    path('certifications/add/', views.add_certification, name='add_certification'),
    path('certifications/delete/<int:pk>/', views.delete_certification, name='delete_certification'),


    path('education/', views.education_list, name='education_list'),
    path('education/add/', views.add_education, name='add_education'),
    path('education/edit/<int:pk>/', views.edit_education, name='edit_education'),
    path('education/delete/<int:pk>/', views.delete_education, name='delete_education'),
]
