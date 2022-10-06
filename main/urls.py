from django.urls import path
from . import views
from django.conf.urls.static import static

urlpatterns = [
    path('', views.main, name="homepage"),
]

# urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
