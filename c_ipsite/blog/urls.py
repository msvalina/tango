from django.conf.urls.defaults import *

urlpatterns = patterns('blog.views',
    (r'^$', 'index'),
    (r'^(?P<year>\d+)/$', 'year_view'),
    (r'^(?P<year>\d{4})/(?P<month>\d{1,2})/$', 'year_month_view'),
    (r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{1,2})/$', 'year_month_day_view'),
)
