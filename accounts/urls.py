from django.urls import path,include
from .import views

urlpatterns = [
    path('reg',views.reg,name="reg"),
    path('login',views.login,name="login"),
    path('logout',views.login,name="logout"),
    path('viewforms',views.viewforms,name="viewforms"),
    path('panel',views.panel,name="panel"),
]

