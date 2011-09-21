from django.conf.urls.defaults import *

urlpatterns = patterns('blog.views',
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{1,2})/(?P<slug>[-\w]+)/$',
        view='post_detail',
        name='blog_detail'
    ),
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{1,2})/$',
        view='day_archive',
        name='blog_day_archive'
    ),
    url(r'^(?P<year>\d{4})/(?P<month>\d{1,2})/$',
        view='year_month_archive',
        name='blog_month_archive'
    ),
    url(r'^(?P<year>\d+)/$',
        view='year_archive',
        name='blog_year_view'
    ),
    url(r'^$', 
        view='index',
        name='blog_index'
    ),
)
