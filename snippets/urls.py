from rest_framework import renderers
from .rest.v1.views import SnippetViewSet, UserViewSet, api_root
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns


from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from .rest.v1 import views
# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'snippets', views.SnippetViewSet)
router.register(r'users', views.UserViewSet)
# The API URLs are now determined automatically by the router.
urlpatterns = [
    url(r'^', include(router.urls))
]


#  snippet_list = SnippetViewSet.as_view({
#      'get': 'list',
#      'post': 'create'
#  })
#  snippet_detail = SnippetViewSet.as_view({
#      'get': 'retrieve',
#      'put': 'update',
#      'patch': 'partial_update',
#      'delete': 'destroy'
#  })
#  snippet_highlight = SnippetViewSet.as_view({
#      'get': 'highlight'
#  }, renderer_classes=[renderers.StaticHTMLRenderer])
#  user_list = UserViewSet.as_view({
#      'get': 'list'
#  })
#  user_detail = UserViewSet.as_view({
#      'get': 'retrieve'
#  })
#
#
#  urlpatterns = format_suffix_patterns([
#      url(r'^$', api_root),
#      url(r'^snippets/$', snippet_list, name='snippet-list'),
#      url(r'^snippets/(?P<pk>[0-9]+)/$', snippet_detail, name='snippet-detail'),
#      url(r'^snippets/(?P<pk>[0-9]+)/highlight/$', snippet_highlight, name='snippet-highlight'),
#      url(r'^users/$', user_list, name='user-list'),
#      url(r'^users/(?P<pk>[0-9]+)/$', user_detail, name='user-detail')
#  ])