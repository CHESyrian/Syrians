"""Syrians URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('<str:usrnm>/', MyProfile, name='MyProfile'),
    path('<str:usrnm>/add_social_media_account/', AddSocialMediaAccount, name='AddSocialMediaAccount'),
    re_path(r'(?P<usrnm>[a-zA-Z0-9._]{,})/.*get_social_media_accounts/$', GetSocialMediaAccounts, name='GetSocialMediaAccounts'),
    path('<str:usrnm>/papyrus/', Profile_Papyrus, name='Papyrus'),
    path('<str:usrnm>/gallery/', Profile_Gallery, name='Gallery'),
    path('<str:usrnm>/gallery/delete/<int:img_id>/', Delete_Image, name='Delete_Image'),
    path('<str:usrnm>/changing_bio/', Change_Bio, name='Changing_Bio'),
    path('<str:usrnm>/sharing_post/', Share_Post, name='Sharing_Post'),
    path('<str:usrnm>/edit_post/<int:id>/', Edit_Post, name='Edit_Post'),
    path('<str:usrnm>/do_editpost/<int:id>/', Do_EditPost, name='Do_EditPost'),
    path('<str:usrnm>/delete_post/<int:id>/', Delete_Post, name='Delete_Post'),
    path('<str:usrnm>/sharing_image/', Share_Image, name='Sharing_Image'),
    path('<str:usrnm>/messages/', Messages, name='Messages'),
    path('<str:usrnm>/notifications/', Notifications, name='Notifications'),
    path('<str:usrnm>/settings/', Account_Settings, name='Account_Settings'),
    path('<str:usrnm>/settings/edit_profile/', Edit_Profile, name='Edit_Profile'),
    path('<str:usrnm>/settings/edit_profile/change_profile_pictures/', Change_Profile_Pictures, name='Change_Profile_Pictures'),
    path('<str:usrnm>/settings/edit_profile/change_profile_pictures/change_cover/', Do_ChangeCover, name='Changing_Cover'),
    path('<str:usrnm>/settings/edit_profile/change_profile_pictures/change_profpic/', Do_ChangeProfPic, name='Changing_ProfPic'),
    path('<str:usrnm>/settings/edit_profile/edit_profile_informations/', Edit_ProfInfos, name='Edit_ProfInfos'),
    path('<str:usrnm>/settings/edit_profile/edit_profile_informations/do_edit/', Do_EditProfInfos, name='Do_EditProfInfo'),
    path('<str:usrnm>/settings/edit_profile/edit_profile_informations/do_change_name/', Do_ChangeName, name='Do_ChangeName'),
    path('<str:usrnm>/settings/edit_profile/edit_others_accounts/', EditSocialMediaAccount, name='Edit_Social_Media_Account'),
    path('<str:usrnm>/settings/edit_profile/edit_others_accounts/get_social_media_accounts/', GetSocialMediaAccounts),
    path('<str:usrnm>/settings/edit_profile/edit_others_accounts/do_edit/', AddSocialMediaAccount, name='Do_EditSocialMediaAccount'),
    path('<str:usrnm>/settings/edit_profile/edit_others_accounts/do_remove/', Do_RemoveSocialMediaAccount, name='Do_RemoveSocialMediaAccount'),
    path('<str:usrnm>/settings/change_email/', Change_Email, name='Change_Email'),
    path('<str:usrnm>/settings/change_email/do_change_email/', Do_ChangeEmail, name='Do_ChangeEmail'),
    path('<str:usrnm>/settings/reset_password_sendcode/', Reset_Password_SendCode, name='SendCode'),
    path('<str:usrnm>/settings/reset_password_verify/', Reset_Password_Verify, name='Verify'),
    path('<str:usrnm>/settings/reset_password/', Reset_Password, name='Reset_Password'),
    path('<str:usrnm>/settings/delete_profile/', Delete_Profile, name='Deleting'),
    path('<str:usrnm>/logging_out/', Logging_Out, name='Log_Out'),
    path('<str:usrnm>/settings/edit_profile/change_profile_pictures/change_cover/', Do_ChangeCover, name='Changing_Cover'),
    path('<str:usrnm>/settings/edit_profile/change_profile_pictures/change_profpic/', Do_ChangeProfPic, name='Changing_ProfPic'),
]\
    +  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
