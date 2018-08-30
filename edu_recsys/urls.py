from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from rest_framework.documentation import include_docs_urls


apiurlpatterns = [
    path('activity/', include("apps.activity.urls")),
    path('docs/', include_docs_urls(title='API Documentaion')),

]
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v0/', include(apiurlpatterns)),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]