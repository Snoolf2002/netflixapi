from django.urls import path, include
from movie.views import ActorAPIView, MovieAPIView, ActorViewSet, MovieViewSet, CommentViewSet, CommentAPIView

from rest_framework.authtoken import views as auth
from rest_framework.routers import DefaultRouter
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.permissions import AllowAny

schema_view = get_schema_view(
    openapi.Info(
        title='Movie App Rest API',
        default_version='v1',
        description='Swagger docs for REST API',
        contact=openapi.Contact('Jaloliddin Abdurakhmonov <gmail@gmail.com>'),
    ),
    public=True,
    permission_classes=(AllowAny,),
)


router = DefaultRouter()
router.register('movies', MovieViewSet)
router.register('actors', ActorViewSet)
router.register('comments', CommentViewSet)


urlpatterns = [
    path('movie/', MovieAPIView.as_view(), name="movie"),
    path('actor/', ActorAPIView.as_view(), name="actor"),
    path('comment/', CommentAPIView.as_view(), name="comment"),
    path('auth/', auth.obtain_auth_token),
    path('', include(router.urls)),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='swagger-docs'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='redoc')
]

