from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from django.conf.urls import include

from . import views

app_name = "library"
urlpatterns = [
    path("/comics", csrf_exempt(views.ComicsView.as_view()), name="comic"),
    path(
        "/comics/<int:pk>", csrf_exempt(views.ComicsDetailView.as_view()), name="comic"
    ),
    path(
        "/actions/action-single",
        csrf_exempt(views.BooksActionSingleView.as_view()),
        name="action-single",
    ),
    path(
        "/actions/smart-action-bulk",
        csrf_exempt(views.BooksActionBulkView.as_view()),
        name="smart-action-bulk",
    ),
    path(
        "/actions/smart-action-global",
        csrf_exempt(views.BooksActionGlobalView.as_view()),
        name="smart-action-global",
    ),
    path(
        "/actions/smart-action-download",
        csrf_exempt(views.BooksActionDownloadView.as_view()),
        name="smart-action-download",
    ),
    path(
        "/actions/add-comment",
        csrf_exempt(views.BooksAddCommentView.as_view()),
        name="add-comment",
    ),
    path('/books/<pk>/relationships/smart_bookstores', views.SmartBookStoreView.as_view(), name='smart_bookstores'),


    path("/products", csrf_exempt(views.ProductsView.as_view()), name="products"),
    path('/actions/smartactionhook', csrf_exempt(views.ProductSmartActionHook.as_view()), name='smartactionhook'),
    path('/actions/smartactionhookload', csrf_exempt(views.ProductSmartActionHookLoad.as_view()), name='smartactionhookload'),

    path("/charts", include("library.charts.urls")),
]
