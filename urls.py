from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.views.generic import TemplateView
from django.views.generic import RedirectView
from django.core.urlresolvers import reverse_lazy

from django.contrib import admin

import portal.views
import portal.core.fit
from portal.core.fit.views import logout

urlpatterns = [
    url(r'^$', RedirectView.as_view(url=reverse_lazy('fit:index'))),
    url(r"^home/", RedirectView.as_view(url=reverse_lazy('fit:index')), name='home'),
    #url(r"^account/logout", RedirectView.as_view(url=reverse_lazy('logout'))),
    url(r"^f2/", include("portal.core.fit.urls", namespace='fit')),
    url(r'^logout/$', logout, name='logout'),
    url(r"^admin/", include(admin.site.urls)),
    url(r"^account/signup/$", portal.views.SignupView.as_view(), name="account_signup"),
    url(r"^account/", include("account.urls")),
    url(r"^account/social/accounts/$", TemplateView.as_view(template_name="account/social.html"), name="account_social_accounts"),
    url(r"^account/social/", include("social.apps.django_app.urls", namespace="social")),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
