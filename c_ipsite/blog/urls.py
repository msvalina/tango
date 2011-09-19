from django.conf.urls.defaults import *

urlpatterns = patterns('blog.views',
    (r'^$', 'index'),
    (r'^(?P<year>\d+)/$', 'year_view'),
    (r'^(?P<year>\d+)/(?P<month>\d+)$', 'year_month_view'),
    (r'^(?P<year>\d{4})/(?P<month>\d{2})$', 'year_month_view'),
)
