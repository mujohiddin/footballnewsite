from django.urls import path
from .views import SignUpView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    # path('reset_password/', auth_views.PasswordResetViewView.as_view(), name="password_reset"),
    # path('reset_password_sent/', auth_views.PasswordResetDoneViewViewView.as_view(), name="password_reset_done"),
    # path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmViewView.as_view(), name="password_reset_confirim"),
    # path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(), name="password_reset_complete"),
]
