from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, include

from .settings import MEDIA_ROOT, MEDIA_URL

urlpatterns = [
    path("admin/", admin.site.urls),
    path("i18n/", include("django.conf.urls.i18n")),
]

urlpatterns += i18n_patterns(
    path("", include("pages.urls")),
    path("accounts/", include("accounts.urls")),
    path("contacts/", include("contacts.urls")),
    path("listings/", include("listings.urls")),
)

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)
