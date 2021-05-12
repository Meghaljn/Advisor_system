from django.conf.urls import url
from django.urls import path
from . import views
from .views import RegisterAPI,LoginAPI
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    url(r'^admin/advisors', views.post_advisors),
    # path(r'^user/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'), # new
    # path(r'^user/refresh/', TokenRefreshView.as_view(), name='token_refresh'),      # new
    path('user/register/', RegisterAPI.as_view(), name='register'),
    path('user/login/', LoginAPI.as_view(), name='login'),
    url(r'^user/(?P<id>\d+)/advisor/$',views.get_list, name='get_list'),
    url(r'^user/(?P<user_id>\d+)/advisor/(?P<advisor_id>\d+)/$',views.book_time,name ='book_time'),
    url(r'^user/(?P<user_id>\d+)/advisor/booking/$',views.get_booked_list, name = 'get_booked_list'),

]