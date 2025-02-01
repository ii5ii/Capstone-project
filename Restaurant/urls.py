#define URL route for index() view
from django.urls import path
from . import views
app_name = "restaurant"
urlpatterns = [
    path('', views.home, name='home'),  # Maps to / (restaurant:home)
    #path('restaurant/', views.index, name='index'),  # Maps to /restaurant/ (restaurant:index)

    # Menu API endpoints
    path("menu/", views.MenuItemView.as_view(), name="menu"),  # restaurant:menu
    path("menu/<int:pk>/", views.MenuItemView.as_view(), name="menu-item"),  # restaurant:menu-item

    # Booking system (Fix: Use booking_view instead of booking)
    path("booking/", views.booking_view, name="booking"),  # restaurant:booking
    path("booking/confirmation/<int:booking_id>/", views.booking_confirmation_view, name="booking_confirmation"),
    # restaurant:booking_confirmation
]
