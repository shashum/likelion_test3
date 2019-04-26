
from django.contrib import admin
from django.urls import path, include
import portfolio.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('portfolio/', include('portfolio.urls')),
    

]
