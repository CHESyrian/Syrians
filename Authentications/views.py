
from django.shortcuts import render, HttpResponseRedirect, reverse
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from My_Account.models import Profile_Model, User_Accounts
from .forms import Register_Form


def Register_Page(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('MyProfile', args=[request.user.username]))
    else:
        RegForm = Register_Form(request.POST or None)
        Context = {'Register_Fields': RegForm,
                   'Msg_Error'      :''}
        if RegForm.is_valid():
            UserName   = RegForm.cleaned_data['User_Name']
            Email      = RegForm.cleaned_data['Email']
            PassWord   = RegForm.cleaned_data['Password']
            ConfPass   = RegForm.cleaned_data['Confirm_Password']
            FirstName  = RegForm.cleaned_data['First_Name']
            LastName   = RegForm.cleaned_data['Last_Name']
            chars_not_allowed = ",;'\"()\\/%&^![]{}<>`@# -+=*|"
            for char in chars_not_allowed:
                if char in UserName:
                    Context['Msg_Error'] = f"some characters in username not allowed.\n As {chars_not_allowed}"
                    return render(request, 'authentications/register.html', Context)
            try:
                user_check = User.objects.get(username=UserName)
                Context['Msg_Error']  = "UserName is Exist:)"
                return render(request, 'authentications/register.html', Context)
            except: pass
            try:
                email_check = User.objects.get(email=Email)
                Context['Msg_Error'] = "Email is Exist:)"
                return render(request, 'authentications/register.html', Context)
            except:
                if PassWord == ConfPass:
                    USER   = User.objects.create_user(email=Email, username=UserName, password=PassWord)
                    USER.first_name = FirstName
                    USER.last_name  = LastName
                    USER.save()
                    user_instance           = User.objects.get(username=UserName)
                    user_profile            = Profile_Model(username=user_instance)
                    user_profile.User_Name  = UserName
                    user_profile.First_Name = FirstName
                    user_profile.Last_Name  = LastName
                    user_profile.save()
                    user_accounts           = User_Accounts(username=user_instance)
                    user_accounts.save()
                    return render(request, 'authentications/login.html')
                else:
                    Context['Msg_Error'] = "Password is different"
                    return render(request, 'authentications/register.html', Context)
        return render(request, 'authentications/register.html', Context)


def Username_Validate(request, user_name):
    chars_not_allowed = ",;'\"()\\/%&^![]{}<>`@# -+=*|"
    for char in chars_not_allowed:
        if char in user_name:
            response_data = {'is_available': False}
            return JsonResponse(response_data)
    try:
        user = User.objects.get(username=user_name)
        response_data = {'is_available': False}
        return JsonResponse(response_data)
    except:
        response_data = {'is_available': True}
        return JsonResponse(response_data)



def Login_Page(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('MyProfile', args=[request.user.username]))
    else:
        return render(request, 'authentications/login.html')

def Logging_In(request):
    UserName  = request.POST['User']
    PassWord  = request.POST['Pass']
    user_auth = authenticate(username=UserName, password=PassWord)
    if user_auth is not None:
        login(request, user_auth)

        return HttpResponseRedirect(reverse('News'))
    return render(request, 'authentications/login.html')
