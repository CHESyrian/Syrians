from django.shortcuts import render, HttpResponseRedirect, HttpResponse, reverse
from django.http import JsonResponse
from django.contrib.auth import logout, authenticate
from django.contrib.auth.models import User
from .models import Profile_Model, Sharing_Post, Sharing_Image, User_Accounts
import datetime as dt


def MyProfile(request, usrnm):
    if usrnm == request.user.username:
        user_id = User.objects.get(username=usrnm).id
        user_profile = Profile_Model.objects.get(username=user_id)
        context = {'user_profile':user_profile}
        return render(request, 'my_account/my_profile.html', context)
    else:
        return render(request, 'errors_pages/not_permission.html')


def AddSocialMediaAccount(request, usrnm):
    if request.user.username == usrnm:
        account_type = request.POST['Type']
        account_link = request.POST['Link']
        user_id      = User.objects.get(username=usrnm).id
        links        = User_Accounts.objects.get(username=user_id)
        if account_type == "Facebook":
            links.Facebook_Link = account_link
        elif account_type == "Twitter":
            links.Twitter_Link = account_link
        elif account_type == "LinkedIn":
            links.LinkedIn_Link = account_link
        elif account_type == "Youtube":
            links.Youtube_Link = account_link
        elif account_type == "Instagram":
            links.Instagram_Link = account_link
        elif account_type == "Github":
            links.Github_Link = account_link
        elif account_type == "Kaggle":
            links.Kaggle_Link = account_link
        elif account_type == "Codepen":
            links.Codepen_Link = account_link
        else:
            return HttpResponse(f'{account_type} in not available')
        links.save()
        return JsonResponse({'result': 'Saved'})
    else:
        return render(request, 'errors_pages/not_permission.html')


def GetSocialMediaAccounts(request, usrnm):
    if request.user.username == usrnm:
        user_id = User.objects.get(username=usrnm).id
        links   = User_Accounts.objects.get(username=user_id)
        data    = {
            'facebook'  : links.Facebook_Link,
            'twitter'   : links.Twitter_Link,
            'youtube'   : links.Youtube_Link,
            'linkedin'  : links.LinkedIn_Link,
            'instagram' : links.Instagram_Link,
            'github'    : links.Github_Link,
            'kaggle'    : links.Kaggle_Link,
            'codepen'   : links.Codepen_Link
        }
        return JsonResponse(data)
    else:
        return render(request, 'errors_pages/not_permission.html')


def Profile_Papyrus(request, usrnm):
    if usrnm == request.user.username:
        user_instance = User.objects.get(username=usrnm)
        posts         = Sharing_Post.objects.filter(username=user_instance).order_by('-Post_Date')
        user_id       = user_instance.id
        user_profile  = Profile_Model.objects.get(username=user_id)
        context       = {'posts':posts,
                         'user_profile': user_profile}
        return render(request, 'my_account/profile_papyrus_section.html', context)
    else:
        return render(request, 'errors_pages/not_permission.html')


def Profile_Gallery(request, usrnm):
    if usrnm == request.user.username:
        user_instance  = User.objects.get(username=usrnm)
        images         = Sharing_Image.objects.filter(username=user_instance).order_by('-Image_Date')
        images_gallery = enumerate(images, 1)
        user_id        = user_instance.id
        user_profile   = Profile_Model.objects.get(username=user_id)
        context        = {'Images_Gallery':images_gallery,
                          'user_profile': user_profile}
        return render(request, 'my_account/profile_gallery_section.html', context)
    else:
        return render(request, 'errors_pages/not_permission.html')


def Delete_Image(request, usrnm, img_id):
    if usrnm == request.user.username:
        try:
            image = Sharing_Image.objects.get(id=img_id)
            image.delete()
            data = {'isDeleted': True, 'note':'Deleted'}
            return JsonResponse(data)
        except:
            data = {'isDeleted': False, 'note': f'Sorry, but image with id {img_id} not found:('}
            return JsonResponse(data)
    else:
        data = {'isDeleted': False, 'note':'You have not permissions:('}
        return JsonResponse(data)


def Change_Bio(request, usrnm):
    if usrnm == request.user.username:
        user_id          = User.objects.get(username=usrnm).id
        user_profile     = Profile_Model.objects.get(username=user_id)
        user_profile.Bio = request.POST['ShareBio_txt']
        user_profile.save()
        return HttpResponseRedirect(reverse('MyProfile', args=[usrnm]))
    else:
        return render(request, 'errors_pages/not_permission.html')


def Share_Post(request, usrnm):
    if usrnm == request.user.username:
        user_instance   = User.objects.get(username=usrnm)
        user_post       = Sharing_Post(username=user_instance,
                                       Post=request.POST['SharePost_txt'])
        user_post.BG_Color   = request.POST['PostBackground']
        user_post.Font_Size  = request.POST['PostFontSize']
        user_post.Font_Color = request.POST['PostFontColor']
        user_post.save()
        return HttpResponseRedirect(reverse('Papyrus', args=[usrnm]))
    else:
        return render(request, 'errors_pages/not_permission.html')


def Edit_Post(request, usrnm, id):
    if usrnm == request.user.username:
        try:
            post      = Sharing_Post.objects.get(id=id)
            context   = {'Old_Post' : post}
            return render(request, 'my_account/edit_post.html', context)
        except Exception as err:
            return HttpResponse(err)
    else:
        return render(request, 'errors_pages/not_permission.html')

def Do_EditPost(request, usrnm, id):
    if usrnm == request.user.username:
        old_post            = Sharing_Post.objects.get(id=id)
        old_post.Post       = request.POST['EditPost_txt']
        old_post.BG_Color   = request.POST['PostBackground']
        old_post.Font_Size  = request.POST['PostFontSize']
        old_post.Font_Color = request.POST['PostFontColor']
        old_post.save()
        return HttpResponseRedirect(reverse('Papyrus', args=[usrnm,]))
    else:
        return render(request, 'errors_pages/not_permission.html')

def Delete_Post(request, usrnm, id):
    if usrnm == request.user.username:
        Post = Sharing_Post.objects.get(id=id)
        Post.delete()
        return HttpResponseRedirect(reverse('Papyrus', args=[usrnm,]))
    else:
        return render(request, 'errors_pages/not_permission.html')


def Share_Image(request, usrnm):
    if usrnm == request.user.username:
        user_instance = User.objects.get(username=usrnm)
        user_image    = Sharing_Image(username=user_instance,
                                      Image=request.FILES['ShareImage_browse'],
                                      Image_Text=request.POST['ShareImage_txt'])
        date                  = str(dt.datetime.today())
        extension             = user_image.Image.name.split('.')[-1]
        new_name              = f'Image_{usrnm}_{date}.{extension}'
        user_image.Image.name = new_name
        user_image.save()
        return HttpResponseRedirect(reverse('Gallery', args=[usrnm]))
    else:
        return render(request, 'errors_pages/not_permission.html')


def Messages(request, usrnm):
    return render(request, 'my_account/messages.html')


def Notifications(request, usrnm):
    return render(request, 'my_account/notifications.html')


def Account_Settings(request, usrnm):
    if usrnm == request.user.username:
        return render(request, 'my_account/account_settings.html')
    else:
        return render(request, 'errors_pages/not_permission.html')


def Edit_Profile(request, usrnm):
    if usrnm == request.user.username:
        return render(request, 'my_account/edit_profile.html')
    else:
        return render(request, 'errors_pages/not_permission.html')


def Change_Profile_Pictures(request, usrnm):
    if usrnm == request.user.username:
        user_id     = User.objects.get(username=usrnm).id
        user_infos  = Profile_Model.objects.get(username=user_id)
        profile_img = user_infos.Profile_Image
        cover_img   = user_infos.Cover_Image
        context     = {'Profile_Image': profile_img,
                       'Cover_Image'  : cover_img}
        return render(request, 'my_account/change_profile_pictures.html', context)
    else:
        return render(request, 'errors_pages/not_permission.html')


def Do_ChangeCover(request, usrnm):
    if usrnm == request.user.username:
        user_id = User.objects.get(username=usrnm).id
        profile = Profile_Model.objects.get(username=user_id)
        profile.Cover_Image = request.FILES.get('ChangeCover_input')
        #profile.Cover_Image.name = usrnm + "cover" + profile.Cover_Image.name
        profile.save()
        return HttpResponseRedirect(reverse('Change_Profile_Pictures', args=[usrnm]))
    else:
        return render(request, 'errors_pages/not_permission.html')


def Do_ChangeProfPic(request, usrnm):
    if usrnm == request.user.username:
        user_id = User.objects.get(username=usrnm).id
        profile = Profile_Model.objects.get(username=user_id)
        profile.Profile_Image = request.FILES.get('ChangeProfPic_input')
        profile.save()
        return HttpResponseRedirect(reverse('Change_Profile_Pictures', args=[usrnm]))
    else:
        return render(request, 'errors_pages/not_permission.html')


def Edit_ProfInfos(request, usrnm):
    if usrnm == request.user.username:
        user_infos = Profile_Model.objects.get(User_Name=usrnm)
        context    = {'User': user_infos}
        return render(request, 'my_account/edit_profile_infos.html', context)
    else:
        return render(request, 'errors_pages/not_permission.html')


def Do_EditProfInfos(request, usrnm):
    if usrnm == request.user.username:
        user_id                     = User.objects.get(username=usrnm).id
        user_profile                = Profile_Model.objects.get(username=user_id)
        user_profile.address        = request.POST['address']
        user_profile.job            = request.POST['job']
        user_profile.number_phone   = request.POST['number_phone']
        user_profile.save()
        return JsonResponse({'result':'saved'})
    else:
        return render(request, 'errors_pages/not_permission.html')


def EditSocialMediaAccount(request, usrnm):
    if usrnm == request.user.username:
        return render(request, 'my_account/edit_social_media_account.html')
    else:
        return render(request, 'errors_pages/not_permission.html')


def Do_RemoveSocialMediaAccount(request, usrnm):
    if request.user.username == usrnm:
        account_type = request.POST['Type']
        user_profile = Profile_Model.objects.get(User_Name=usrnm)
        if account_type == "Facebook":
            user_profile.Facebook_Link = ''
        elif account_type == "Twitter":
            user_profile.Twitter_Link = ''
        elif account_type == "LinkedIn":
            user_profile.LinkedIn_Link = ''
        elif account_type == "Youtube":
            user_profile.Youtube_Link = ''
        elif account_type == "Instagram":
            user_profile.Instagram_Link = ''
        elif account_type == "Github":
            user_profile.Github_Link = ''
        elif account_type == "Kaggle":
            user_profile.Kaggle_Link = ''
        elif account_type == "Codepen":
            user_profile.Codepen_Link = ''
        else:
            return HttpResponse(f'You havn\'t {account_type} account')
        user_profile.save()
        return JsonResponse({'eesult': 'Deleted'})
    else:
        return render(request, 'errors_pages/not_permission.html')


def Do_ChangeName(request, usrnm):
    if usrnm == request.user.username:
        user    = User.objects.get( username=usrnm )
        profile = Profile_Model.objects.get( username=user.id )
        if profile.Editable:
            user.first_name  = request.POST['firstName']
            user.last_name   = request.POST['lastName']
            profile.Editable = False
            user.save()
            profile.save()
            Data = {'result':'Success', 'message':'Saved'}
            return JsonResponse(Data)
        else:
            Data = {'result':'Error', 'message':'You can\'t edit your name again'}
            return JsonResponse(Data)
    else:
        return render(request, 'errors_pages/not_permission.html')


def Change_Email(request, usrnm):
    if usrnm == request.user.username:
        return render(request, 'my_account/change_email.html')
    else:
        return render(request, 'errors_pages/not_permission.html')


def Do_ChangeEmail(request, usrnm):
    if usrnm == request.user.username:
        old_email  = request.POST['current_email']
        new_email  = request.POST['new_email']
        check_pwd  = request.POST['check_password']
        user       = User.objects.get(username=usrnm)
        if User.objects.filter(email=new_email).exists():
            Data = {'result':'Error', 'message':'new email is exist,please enter you real email'}
            return JsonResponse(Data)
        else:
            check_auth = authenticate(username=usrnm, password=check_pwd)
            if check_auth is not None:
                if user.email == old_email:
                    user.email = new_email
                    user.save()
                    Data = {'result': 'Success', 'message': 'Changed'}
                    return JsonResponse(Data)
                else:
                    Data = {'result':'Error', 'message':f'{old_email} incorrect'}
                    return JsonResponse(Data)
            else:
                Data = {'result':'Error', 'message':'Wrong Password'}
                return JsonResponse(Data)
    else:
        return render(request, 'errors_pages/not_permission.html')


def Reset_Password_SendCode(request, usrnm):
    if usrnm == request.user.username:
        return render(request, 'my_account/reset_password_sendcode.html')
    else:
        return render(request, 'errors_pages/not_permission.html')


def Reset_Password_Verify(request, usrnm):
    if usrnm == request.user.username:
        return render(request, 'my_account/reset_password_verify.html')
    else:
        return render(request, 'errors_pages/not_permission.html')


def Reset_Password(request, usrnm):
    if usrnm == request.user.username:
        return render(request, 'my_account/reset_password.html')
    else:
        return render(request, 'errors_pages/not_permission.html')


def Delete_Profile(request, usrnm):
    if request.user.username == usrnm:
        user_instance = User.objects.get(username=usrnm)
        user_instance.delete()
        return HttpResponseRedirect(reverse('Home_Page'))
    else:
        return render(request, 'errors_pages/not_permission.html')


def Logging_Out(request, usrnm):
    if request.user.username == usrnm:
        logout(request)
        return HttpResponseRedirect(reverse('Home_Page'))
    else:
        return render(request, 'errors_pages/not_permission.html')
