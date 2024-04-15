from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from . import views

# urlpatterns = [
#     path('categories', views.CategoriesView.as_view()),
#     path('menu-items', views.MenuItemsView.as_view()),
#     path('menu-items/<int:pk>', views.SingleMenuItemView.as_view()),
#     path('cart/menu-items', views.CartView.as_view()),
#     path('orders', views.OrderView.as_view()),
#     path('orders/<int:pk>', views.SingleOrderView.as_view()),
#     path('groups/manager/users', views.GroupViewSet.as_view(
#         {'get': 'list', 'post': 'create', 'delete': 'destroy'})),

#     path('groups/delivery-crew/users', views.DeliveryCrewViewSet.as_view(
#         {'get': 'list', 'post': 'create', 'delete': 'destroy'}))
# ]
urlpatterns = [
    path('api-token-auth/', obtain_auth_token, name='api-token-auth'), 
    # Categories endpoint
    path('categories/', views.CategoriesView.as_view(), name='categories-list'),

    # Menu items endpoints
    path('menu-items/', views.MenuItemView.as_view(), name='menu-items-list'),
    path('menu-items/<int:pk>/', views.SingleItemView.as_view(), name='single-menu-item'),

    # Cart management endpoints
    path('cart/', views.CustomerCart.as_view(), name='customer-cart'),
    path('cart/menu-items', views.CustomerCart.as_view(), name='cart-menu-items'),

    # Order management endpoints
    path('orders/', views.OrdersView.as_view(), name='orders-list'),
    path('orders/<int:pk>/', views.SingleOrderView.as_view(), name='single-order'),

    # User group management endpoints
    path('groups/manager/users/', views.ManagerUsersView.as_view(), name='manager-group-users'),
    path('groups/manager/users/<int:pk>/', views.ManagerSingleUserView.as_view(), name='assign-user-to-manager-group'),
    path('groups/delivery-crew/users/', views.DeliveryCrewManagement.as_view(), name='delivery-crew-group-users'),
    path('groups/delivery-crew/users/<int:pk>/', views.DeliveryCrewManagementSingleView.as_view(), name='assign-user-to-delivery-crew-group'),
]