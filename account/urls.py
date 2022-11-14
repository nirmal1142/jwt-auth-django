from django.urls import path
from account.views import get_user_list, get_api_test, SendPasswordResetEmailView,  UserLoginView, UserPasswordChangeView, UserPasswordResetView, UserProfileView, UserRegistrationView


urlpatterns = [

    path('register/', UserRegistrationView.as_view(), name='user-registration'),
    path('login/', UserLoginView.as_view(), name='user-login'),
    path('profile/', UserProfileView.as_view(), name='profile'),
    path('changepassword/', UserPasswordChangeView.as_view(), name='changepassword'),
    path('send-reset-password-email/', SendPasswordResetEmailView.as_view(),
         name='send-reset-password-email'),
    path('reset-password/<uid>/<token>/',
         UserPasswordResetView.as_view(), name='reset-password'),
    path('get-user-list/', get_user_list, name='get-user-list'),
    path('api-test/', get_api_test, name='api-test'),


]
