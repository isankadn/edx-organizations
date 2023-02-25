"""
URLS for organizations
"""
from django.conf.urls import url, include
from organizations.views import OrganizationsViewSet, OrganizationDetailViewSet

app_name = 'organizations'  # pylint: disable=invalid-name
urlpatterns = [
    url(r'^$', OrganizationsViewSet.as_view(), name='partners_all'),
    url(r'^(?P<short_name>[\w-]+)/$', OrganizationDetailViewSet.as_view(), name='partner_details'),
    url(r'^v0/', include('organizations.v0.urls')),
]
