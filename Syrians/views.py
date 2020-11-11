from django.shortcuts import HttpResponseRedirect, reverse


def Home_Page(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('News'))
    else:
        return HttpResponseRedirect(reverse('Login_Page'))