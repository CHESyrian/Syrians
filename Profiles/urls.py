from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('<str:profile>/', Profile, name='Profile'),
    path('<str:profile>/get_social_media_accounts/', GetSocialMediaAccounts),
    path('<str:profile>/get_gallery/', Profile_Gallery, name='GetGallery'),
    path('posts/<str:reaction>/<int:id>/', Reaction_Post, name='Reaction_Post'),
] \
    + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
