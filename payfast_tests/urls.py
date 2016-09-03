import django
import payfast.urls

from django.contrib import admin

if django.VERSION < (1, 3):
    # Work around https://code.djangoproject.com/ticket/15343
    from django.conf.urls.defaults import handler404, handler500  # noqa

if django.VERSION < (1, 4):
    from django.conf.urls.defaults import url, include
else:
    from django.conf.urls import url, include


if django.VERSION < (1, 7):
    admin.autodiscover()


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^payfast/', include(payfast.urls)),
]
