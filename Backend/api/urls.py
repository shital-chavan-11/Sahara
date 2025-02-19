from django.urls import path
from .views import register_user
from .views import donate
from .views import login_view
from .views import create_fund_post
from .views import ngo_stats
from .views import NotificationView
from .views import FundPostDetailView


urlpatterns = [
    path('register/', register_user, name='register'),
    path('donate/', donate, name='donate'),
    path('login/', login_view, name='login'),
    path('fund-posts/create/', create_fund_post, name='create_fund_post'),
    path('api/ngo-stats/<int:ngo_id>/', ngo_stats, name="ngo-stats"),
    path("api/notifications/", NotificationView.as_view(), name="notifications"),
    path("api/fund-posts/<int:post_id>/", FundPostDetailView.as_view(), name="fund_post_detail"),

]
