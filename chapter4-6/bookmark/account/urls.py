from django.conf.urls import url
from . import views as account_views
from django.contrib.auth import views as build_in_views
from django.contrib.auth import urls as auth_urls


urlpatterns = [
        # url(r'^login/$', account_views.user_login, name='user_login'),

        url(r'^$', account_views.dashboard, name='dashboard'),
        url(r'^login/$', build_in_views.login, name='login'),
        url(r'^logout/$', build_in_views.logout, name='logout'),
        url(r'^logout-then-login/$', build_in_views.logout_then_login, name='logout_then_login'),
        url(r'^password-change/$', build_in_views.password_change, name='password_change'),
        url(r'^password-change/done/$', build_in_views.password_change_done, name='password_change_done'),
        url(r'^password-reset/$', build_in_views.password_reset, name='password_reset'), url(r'^password-reset/done/$', build_in_views.password_reset_done, name='password_reset_done'),
        url(r'^password-reset/confirm/$', build_in_views.password_reset_confirm, name='password_reset_confirm'),
        url(r'^password-reset/complete/$', build_in_views.password_reset_complete, name='password_reset_complete'),
        url(r'^register/$', account_views.register, name='register'),
        url(r'^edit/$', account_views.edit, name='edit'),
        url(r'users/$', account_views.user_list, name='user_list'),
        url(r'^users/(?P<username>[-\w]+)/$', account_views.user_detail, name='user_detail'),
        url(r'^users/follow/$', account_views.user_follow, name='user_follow'),

        # url(r'^password'),
        ]

urlpatterns += auth_urls.urlpatterns
