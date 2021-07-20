"""easyjob1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib import admin
from django.urls import path,include
from .import views
from django.conf import settings
from django.conf.urls.static import static
from .import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/',views.signup,name ='signup'),
    path('department/',include('department.urls')),
    path('reg',views.register,name ='register'),
    path('register/department',views.department_register,name ='department_register'),
    path('signin/',views.signin,name = 'signin'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('public/',include('public.urls')),
    path('who/',views.who,name='who'),
    path('logout/', views.signout, name='signout'),
    path('', views.home, name='home'),
    path('jobseekerdash/',views.jobseekerdash,name='jobseekerdash'),
    path('measure', include('measurements.urls', namespace='measurements')),
    path('geoip/', include('django_geoip.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
