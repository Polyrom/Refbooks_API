from django.urls import path

from .views import ReferenceBookView, ReferenceBookItemsView, CheckElementView

urlpatterns = [
    path(
        '', ReferenceBookView.as_view(),
        name='refbooks'
    ),
    path(
        '<int:pk>/elements',
        ReferenceBookItemsView.as_view(),
        name='elements'
    ),
    path(
        '<int:pk>/check_element',
        CheckElementView.as_view(),
        name='check'
    )
]
