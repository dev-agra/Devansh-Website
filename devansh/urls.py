from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
from . import views

app_name = 'devansh'

urlpatterns = [
    path('', views.Homepage, name="Home"),
    path('contact/', views.Contactpage, name="Contact"),
    path('feedback/', views.Feedbackpage, name="Feedback"),
    path('about/', views.Aboutpage, name="About")
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)