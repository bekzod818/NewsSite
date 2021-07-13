from re import template
from django.urls import path
from .views import SignUpView, MyPasswordChangeView, MyPasswordResetDoneView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    # path('password-change/', MyPasswordChangeView.as_view(), name='password-change'),
    # path('password-change/done/', MyPasswordResetDoneView.as_view(), name='password-change-done'),
]