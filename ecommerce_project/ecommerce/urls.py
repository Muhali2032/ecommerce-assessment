
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),

    path(
        'login/',
        auth_views.LoginView.as_view(
            template_name='ecommerce/login.html'
        ),
        name='login'
    ),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
        path(
        'password-reset/',
        auth_views.PasswordResetView.as_view(
            template_name='ecommerce/password_reset.html',
            email_template_name='ecommerce/password_reset_email.html',
            subject_template_name='ecommerce/password_reset_subject.txt',
            success_url='/password-reset/done/'
        ),
        name='password_reset'
    ),
    path(
        'password-reset/done/',
        auth_views.PasswordResetDoneView.as_view(
            template_name='ecommerce/password_reset_done.html'
        ),
        name='password_reset_done'
    ),
    path(
        'reset/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(
            template_name='ecommerce/password_reset_confirm.html',
            success_url='/reset/done/'
        ),
        name='password_reset_confirm'
    ),
    path(
        'reset/done/',
        auth_views.PasswordResetCompleteView.as_view(
            template_name='ecommerce/password_reset_complete.html'
        ),
        name='password_reset_complete'
    ),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('stores/', views.store_list, name='store_list'),
    path('stores/create/', views.store_create, name='store_create'),
    path('stores/<int:pk>/edit/', views.store_update, name='store_update'),
    path('stores/<int:pk>/delete/', views.store_delete, name='store_delete'),

    path(
        'stores/<int:store_pk>/products/',
        views.product_list,
        name='product_list'
    ),
    path(
        'stores/<int:store_pk>/products/create/',
        views.product_create,
        name='product_create'
    ),
    path(
        'products/<int:pk>/edit/',
        views.product_update,
        name='product_update'
    ),
    path(
        'products/<int:pk>/delete/',
        views.product_delete,
        name='product_delete'
    ),
    path(
        'catalogue/',
        views.product_catalogue,
        name='product_catalogue'
    ),
    path('cart/', views.cart_view, name='cart_view'),
    path('cart/add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/remove/<int:product_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('checkout/', views.checkout, name='checkout'),

    path(
        'order-success/<int:order_id>/',
        views.order_success,
        name='order_success'
    ),
    path(
        'products/<int:product_id>/review/',
        views.submit_review,
        name='submit_review'
    ),
]

