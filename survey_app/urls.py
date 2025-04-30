# survey_app/urls.py
from django.urls import path
from survey_app.views import survey_form, login_view, logout_view, dashboard_view
from . import views
from django.contrib import admin
from survey_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),  # Home page
    path('survey/', survey_form, name='survey_form'), # use '' to make survey be home page
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('dashboard/', dashboard_view, name='dashboard'),
    path('download_csv/', views.download_csv, name='download_csv'),
    path('thank-you/', views.thank_you_view, name='thank_you'),
]

