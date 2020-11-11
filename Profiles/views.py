from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from django.contrib.auth.models import User
from My_Account.models import Sharing_Post, Sharing_Image, Profile_Model, User_Accounts
from .models import Posts_Good, Posts_Amazing, Posts_Shares


def Profile(request, profile):
    try:
        User_Profile  = Profile_Model.objects.get(User_Name=profile)
        Context       = {'user_profile': User_Profile}
        return render(request, 'profiles/profile.html', Context)
    except:
        return render(request, 'errors_pages/not_found.html')


def GetSocialMediaAccounts(request, profile):
    try:
        user_id = User.objects.get(username=profile).id
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
    except:
        return render(request, 'errors_pages/not_found.html')


def Profile_Gallery(request, profile):
    user_id = User.objects.get(username=profile).id
    Images  = Sharing_Image.objects.filter(username=user_id)
    data    = []
    for img in Images:
        Elem = {
        'User':img.username.username,
        'Path':img.Image.path,
        'Date':img.Image_Date,
        'Good':img.Good_Num,
        'Amazing':img.Amazing_Num,
        'Star':img.Stars_Num,
        }
        data.append(Elem)
        #Path, Goods, Amazings, Stars, Id
    print(data)
    return JsonResponse({'D': 'Done'})


def Check_Contacts(request, profile):
    username = request.user.username
    profile  = profile
    return JsonResponse()


def Reaction_Post(request, reaction, id):
    if request.user.is_authenticated:
        user_id = request.user.id
        post_id = id
        print(user_id, post_id)
        if reaction == "good":
            try:
                good        = Posts_Good.objects.get(username=user_id, Post=post_id)
                Target_Post = Sharing_Post.objects.get(id=post_id)
                Target_Post.Good_Num -= 1
                good.delete()
                Target_Post.save()
                data_response = {'reaction':reaction, 'is_action':False}
                return JsonResponse(data_response)
            except:
                user_instance = User.objects.get(id=user_id)
                post_instance = Sharing_Post.objects.get(id=post_id)
                like          = Posts_Good( username=user_instance, Post=post_instance )
                Target_Post   = Sharing_Post.objects.get(id=post_id)
                Target_Post.Good_Num += 1
                like.save()
                Target_Post.save()
                data_response = {'reaction': reaction, 'is_action': True}
                return JsonResponse(data_response)
        elif reaction == "amazing":
            try:
                amazing     = Posts_Amazing.objects.get(username=user_id, Post=post_id)
                Target_Post = Sharing_Post.objects.get(id=post_id)
                Target_Post.Amazing_Num -= 1
                amazing.delete()
                Target_Post.save()
                data_response = {'reaction': reaction, 'is_action': False}
                return JsonResponse(data_response)
            except:
                user_instance = User.objects.get(id=user_id)
                post_instance = Sharing_Post.objects.get(id=post_id)
                amazing       = Posts_Amazing(username=user_instance, Post=post_instance)
                Target_Post   = Sharing_Post.objects.get(id=post_id)
                Target_Post.Amazing_Num += 1
                amazing.save()
                Target_Post.save()
                data_response = {'reaction': reaction, 'is_action': True}
                return JsonResponse( data_response )
        elif reaction == "share":
            pass
        else:
            return HttpResponse(f"Sorry, but {reaction} is not found")
    else:
        return render(request, 'error_pages/not_permission.html')


def Reaction_Image(request, reaction, id):
    pass
