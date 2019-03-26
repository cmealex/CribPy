from django.conf.urls import url
from .views import index, display_rooms, add_item, edit_item, delete_item

urlpatterns = [

    url(r'^$', index, name='index'),

    url(r'^display_rooms$', display_rooms, name='display_rooms'),

    url(r'^add_item$', add_item, name='add_item'),

    url(r'^edit_item/(?P<pk>\d+)$', edit_item, name='edit_item'),

    url(r'^delete_item/(?P<pk>\d+)$', delete_item, name='delete_item')
]