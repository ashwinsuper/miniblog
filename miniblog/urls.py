from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static


admin.site.site_header = "MiniBlog Header"
admin.site.site_title = "MiniBlog Title"
admin.site.index_title = "MiniBlog Index Title"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('blog.urls')),
    path('home',include('blog.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)