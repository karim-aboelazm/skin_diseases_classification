from django.contrib import admin
from django.urls import path,include
from django.conf import settings as st
from django.conf.urls.static import static as sc

urlpatterns = [
    path("admin/", admin.site.urls),
    path('',include('skin.urls',namespace='skin')),
]
if st.DEBUG:
    urlpatterns += sc(st.STATIC_URL,document_root=st.STATIC_ROOT)
    urlpatterns += sc(st.MEDIA_URL,document_root=st.MEDIA_ROOT)
