from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'demo.views.home', name='home'),
    url(r'^pretty_quote', 'demo.views.home_with_template', name='pretty_quote'),
    url(r'^quote/(?P<quote_index>\d+)$', 'demo.views.specific_quote', name='specific_quote'),
)
