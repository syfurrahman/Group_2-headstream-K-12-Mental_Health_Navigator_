# survey_app/urls.py
from django.urls import path
from survey_app.views import survey_form, login_view, logout_view, dashboard_view
from . import views
from django.contrib import admin
from survey_app import views
from .views import chatbot_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('survey/', survey_form, name='survey_form'),  # Survey page
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('dashboard/', dashboard_view, name='dashboard'),
    path('download_csv/', views.download_csv, name='download_csv'),
    path('thank-you/', views.thank_you_view, name='thank_you'),
    path('modal-survey-submit/', views.modal_survey_submit, name='modal_survey_submit'),
    path('', views.index, name='index'),  # Main page
    path('aboutus/', views.aboutus, name='aboutus'),  # About Us page
    path('assess/', views.assess, name='assess'),  # Assessment page
    path('case2/', views.case2, name='case2'),  # Case 2 page
    path('case3/', views.case3, name='case3'),  # Case 3 page
    path('case4/', views.case4, name='case4'),  # Case 4 page
    path('case5/', views.case5, name='case5'),  # Case 5 page
    path('casestudies/', views.casestudies, name='casestudies'),  # Case Studies page
    path('explore/', views.explore, name='explore'),  # Explore page
    path('fundingStrategy/', views.fundingStrategy, name='fundingStrategy'),  # Funding Strategy page
    path('implementSolution/', views.implementSolution, name='implementSolution'),  # Implement Solution page
    path('methuen/', views.methuen, name='methuen'),  # Methuen page
    path('selectSolution/', views.selectSolution, name='selectSolution'),  # Select Solution page
    path('stakeholder/', views.stakeholder, name='stakeholder'),  # Stakeholder page
    path("chat/", views.chatbot_view, name="chat"), # Chatbot endpoint
]

