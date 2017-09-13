from django.conf.urls import url
from .views import Login, Logout
from .views import UserProfileData, UserList, UserNew, UserDelete
from .views import ActiveInactiveUser, ChangePassword

app_name = 'security'

urlpatterns = [
    url(r'^login/$', Login.as_view(), name="login"),
    url(r'^logout/$', Logout.as_view(), name="logout"),
    url(r'^userprofile/$', UserProfileData.as_view(), name="userprofile"),
    url(r'^userprofilechange-password/$', ChangePassword.as_view(), name="userprofile-change-password"),
    url(r'^user/list/$', UserList.as_view(), name="user-list"),
    url(r'^user/new/$', UserNew.as_view(), name="user-new"),
    url(r'^user/delete/(?P<pk>.*)/$', UserDelete.as_view(), name="user-delete"),
    url(r'^user/active-inactive/(?P<user_id>.*)/$', ActiveInactiveUser.as_view(), name="user-active-inactive"),
]

