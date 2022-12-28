from __future__ import absolute_import
from django.views.generic import ListView, DetailView, TemplateView

from organizations.models import Organization, OrganizationCourse
from xmodule.modulestore.django import modulestore
from opaque_keys.edx.keys import CourseKey
from openedx.core.djangoapps.content.course_overviews.models import CourseOverview
from django.conf import settings
from django.shortcuts import get_object_or_404


class OrganizationsViewSet(ListView):
    model = Organization
    context_object_name = 'organizations_list'
    queryset = Organization.objects.filter(active=True)
    template_name = "partners.html"


class OrganizationDetailViewSet(TemplateView):
    model = OrganizationCourse

    template_name = "partner_details.html"

    def get_context_data(self, **kwargs):
        course_overviews = []
        courses = OrganizationCourse.objects.filter(organization_id=self.kwargs['pk'], active=1)

        for course in courses:
            course_key = CourseKey.from_string(course.course_id)
            # overview = CourseOverview.get_from_id(course_key)
            course_overviews.append(CourseOverview.get_from_id(course_key))


        context = super(OrganizationDetailViewSet, self).get_context_data(**kwargs)

        context['courses'] = course_overviews
        context['lms_url'] = settings.SITE_NAME
        context['organization'] = get_object_or_404(Organization, id=self.kwargs['pk'])

        return context
