from django.conf.urls import url
from .views import Dashboard, AccountList, AccountNew, AccountDelete, AccountEdit
from .views import TransactionList, TransactionNew, TransactionEdit, TransactionDelete
from .views import CategoryList, CategoryNew, CategoryEdit, CategoryDelete
from .views import TransactionCommentList, TransactionCommentNew

app_name = 'flow'

urlpatterns = [
    url(r'dashboard/$', Dashboard.as_view(), name="dashboard"),
    url(r'flow/account/list/$', AccountList.as_view(), name="account-list"),
    url(r'flow/account/new/$', AccountNew.as_view(), name="account-new"),
    url(r'flow/account/delete/(?P<pk>.*)/$', AccountDelete.as_view(), name="account-delete"),
    url(r'flow/account/edit/(?P<pk>.*)/$', AccountEdit.as_view(), name="account-edit"),
    url(r'flow/transaction/list/$', TransactionList.as_view(), name="transaction-list"),
    url(r'flow/transaction/new/$', TransactionNew.as_view(), name="transaction-new"),
    url(r'flow/transaction/edit/(?P<pk>.*)/$', TransactionEdit.as_view(), name="transaction-edit"),
    url(r'flow/transaction/delete/(?P<pk>.*)/$', TransactionDelete.as_view(), name="transaction-delete"),
    url(r'flow/category/list/$', CategoryList.as_view(), name="category-list"),
    url(r'flow/category/new/$', CategoryNew.as_view(), name="category-new"),
    url(r'flow/category/edit/(?P<pk>.*)/$', CategoryEdit.as_view(), name="category-edit"),
    url(r'flow/category/delete/(?P<pk>.*)/$', CategoryDelete.as_view(), name="category-delete"),
    url(r'flow/transaction/comment/list/$', TransactionCommentList.as_view(), name="transaction-comment-list"),
    url(r'flow/transaction/(?P<trans_id>.*)/comment/new/$', TransactionCommentNew.as_view(), name="transaction-comment-new"),
]
