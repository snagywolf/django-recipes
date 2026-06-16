from django.urls import path, include
from django.contrib.auth import views as auth_views
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from . import views
from recipes.views import RecipeViewSet

# DRF Router (padrão profissional para API)
router = DefaultRouter()
router.register(r'recipes', RecipeViewSet, basename='recipe')

urlpatterns = [

    # =====================
    # HOME
    # =====================
    path('', views.home, name='home'),

    # =====================
    # AUTH
    # =====================
    path(
        'login/',
        auth_views.LoginView.as_view(
            template_name='recipes/page/login.html'
        ),
        name='login'
    ),

    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register, name='register'),

    # =====================
    # RECIPE (SITE NORMAL)
    # =====================
    path('recipes/<slug:slug>/', views.recipe_view, name='recipe'),
    path('create/', views.create_recipe, name='create_recipe'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('update/<int:id>/', views.update_recipe, name='update_recipe'),
    path('delete/<int:id>/', views.delete_recipe, name='delete_recipe'),

    # =====================
    # API (DRF ROUTER)
    # =====================
    path('api/', include(router.urls)),

    # (Opcional) Login da API via browsable API
    path('api-auth/', include('rest_framework.urls')),

 
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]