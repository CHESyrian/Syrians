from django.db.models import Q
from django.shortcuts import render, HttpResponseRedirect, HttpResponse, reverse
from My_Account.models import Sharing_Post, Sharing_Image, Profile_Model


def Explore_Page(request):
    return render(request, 'explore/explore.html')


def News_Page(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('News_Posts'))
    else:
        return HttpResponseRedirect(reverse('Home_Page'))


def News_Posts(request):
    if request.user.is_authenticated:
        shares_posts = Sharing_Post.objects.all().order_by('-Post_Date')
        Context = {'Posts': shares_posts}
        return render(request, 'explore/news_posts.html', Context)
    else:
        return HttpResponseRedirect(reverse('Home_Page'))

def News_Images(request):
    if request.user.is_authenticated:
        shares_images = Sharing_Image.objects.all().order_by( '-Image_Date' )
        Context = {'Images': shares_images}
        return render(request, 'explore/news_images.html', Context)
    else:
        return HttpResponseRedirect(reverse('Home_Page'))


def Search(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            keyword = request.POST['SearchEngine']
            if keyword == '':
                return HttpResponseRedirect(reverse('Home_Page'))
            else:
                return HttpResponseRedirect(reverse('Search_Users', args=[keyword]))
        else:
            return HttpResponse('Sorry', request.method)
    else:
        return render(request, 'errors_pages/not_permission.html')


def Search_Users(request, keyword):
    if request.user.is_authenticated:
        users_filter = Profile_Model.objects.filter(Q(User_Name__regex=f'{keyword}') | Q(First_Name__regex=f'{keyword}') | Q(Last_Name__regex=f'{keyword}'))
        Context      = {'keyword':keyword, 'users_filter':users_filter}
        return render(request, 'explore/search_results_users.html', Context)
    else:
        return render(request, 'errors_pages/not_permission.html')


def Search_Posts(request, keyword):
    if request.user.is_authenticated:
        posts_filter = Sharing_Post.objects.filter(Q(Post__regex=f'{keyword}'))
        Context         = {'keyword':keyword, 'posts_filter':posts_filter}
        return render(request, 'explore/search_results_posts.html', Context)
    else:
        return render(request, 'errors_pages/not_permission.html')


def Search_Images(request, keyword):
    if request.user.is_authenticated:
        images_filter   = Sharing_Image.objects.filter(Q(Image_Text__regex=f'{keyword}'))
        Context         = {'keyword':keyword, 'images_filter':images_filter}
        return render(request, 'explore/search_results_images.html', Context)
    else:
        return render(request, 'errors_pages/not_permission.html')