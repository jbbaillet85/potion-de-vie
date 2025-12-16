from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("allauth.urls")),
    # path("user/", include("apps.user.urls")),
    path("", TemplateView.as_view(template_name="home/homepage.html"), name="homepage"),
    path(
        "credits",
        TemplateView.as_view(template_name="home/credits.html"),
        name="credits",
    ),
    path(
        "contribution",
        TemplateView.as_view(template_name="home/contribution.html"),
        name="contribution",
    ),
]
