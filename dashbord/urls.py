
import django
from django.contrib import admin
from django.urls import path,include
from dashbord import views

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('',views.about,name='about'),
    # path('',views.index,name='about'),
    # path('',views.index,name='index'),
    path('',include('servies.urls'))
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)