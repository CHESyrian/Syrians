from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import *

urlpatterns = [
    path('<str:profile>/', Profile, name='Profile'),
    path('<str:prodile>/get_social_media_accounts/', GetSocialMediaAccounts),
    path('<str:profile>/get_gallery/', Profile_Gallery, name='GetGallery'),
    re_path(r'(?P<profile>[a-zA-Z0-9._]{,})/.*check_contacts/$', ),
    path('posts/<str:reaction>/<int:id>/', Reaction_Post, name='Reaction_Post'),
] \
    + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
