
from django.contrib import admin
from django.urls import path, include

import visits
from .views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_page_view),
    path('visits/', include("visits.urls")),
]
