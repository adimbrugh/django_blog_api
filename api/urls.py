

from blog.views import ( PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView )
from blog.views import post_detail_view, CommentUpdateView, CommentDeleteView
from drf_yasg.views import get_schema_view as swagger_get_schema_view
from blog.views import post_list_view, posts_by_tag
from django.contrib.auth import views as auth_views
from accounts.views import RegisterView, ProfileView
from django.urls import path
from drf_yasg import openapi


#API design, doucmentaion, and ensuring adherence to OpenAPI standerds
schema_view = swagger_get_schema_view(
    openapi.Info(
        title= "Django Blog API",
        default_version= "1.0.0",
        description="API Documentation Of APP"
    ),
    public=True,
)


urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('', PostListView.as_view(), name='post_list'),
    path('post/<slug:slug>/', PostDetailView.as_view(), name='post_detail'),
    path('post/new/', PostCreateView.as_view(), name='post_create'),
    path('post/<slug:slug>/edit/', PostUpdateView.as_view(), name='post_edit'),
    path('post/<slug:slug>/delete/', PostDeleteView.as_view(), name='post_delete'),
    path("post/<slug:slug>/", post_detail_view, name="post_detail"),
    path("comment/<int:pk>/edit/", CommentUpdateView.as_view(), name="comment_edit"),
    path("comment/<int:pk>/delete/", CommentDeleteView.as_view(), name="comment_delete"),
    path("", post_list_view, name="post_list"),
    path("tag/<slug:tag_slug>/", posts_by_tag, name="posts_by_tag"),
    path('swagger/schema/', schema_view.with_ui('swagger', cache_timeout=0), name='swagger_schema'),
]


from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns += [
    path('password-reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('swagger/schema/', schema_view.with_ui('swagger', cache_timeout=0), name='swagger_schema'),
]

