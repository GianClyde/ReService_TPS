from django.shortcuts import render, redirect
from django.db.models import Q
from django.http import HttpResponse
from .models import User,Profile,Driverprofile,Reservation
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout,get_user_model
from django.contrib.auth.decorators import login_required
from .forms import  DriverProfilePicture,EditDriverProfileForm,EditProfileForm,SetPasswordForm,PasswordResetForm,EditUserForm,ProfileForm,ProfilePicture,DriverProfileForm,StudentUserForm,DriverUserForm
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.core.mail import EmailMessage
from .tokens import account_activation_token
from .decorators import unauthenticated_user,allowed_users
from django.contrib.auth.models import Group
# Create your views here.

def activate(request, uidb64, token):
    User = get_user_model()
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except:
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        messages.success(request, "Thank you for your email confirmation. Now you can login your account.")
        login(request,user)
        if user.is_student:
            return redirect('profile-fillup')
        else:
            return redirect('driver-profile-fillup')
    else:
        messages.error(request, "Activation link is invalid!")

    return redirect('navPage')

def activateEmail(request, user, to_email):
    mail_subject = "Activate your user account."
    message = render_to_string("student_registration/activate_account.html", {
        'user': user.email,
        'domain': get_current_site(request).domain,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': account_activation_token.make_token(user),
        "protocol": 'https' if request.is_secure() else 'http'
    })
    email = EmailMessage(mail_subject, message, to=[to_email])
    if email.send():
        messages.success(request, f'Dear <b>{user}</b>, please go to you email <b>{to_email}</b> inbox and click on \
                received activation link to confirm and complete the registration. <b>Note:</b> Check your spam folder.')
    else:
        messages.error(request, f'Problem sending email to {to_email}, check if you typed it correctly.')

def passwordResetConfirm(request, uidb64, token):
    User = get_user_model()
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except:
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        if request.method == 'POST':
            form = SetPasswordForm(user, request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, "Your password has been set. You may go ahead and <b>log in </b> now.")
                return redirect('login')
            else:
                for error in list(form.errors.values()):
                    messages.error(request, error)

        form = SetPasswordForm(user)
        return render(request, 'student_registration/password_change.html', {'form': form})
    else:
        messages.error(request, "Link is expired")

    messages.error(request, 'Something went wrong, redirecting back to Homepage')
    return redirect("login")

def password_reset_request(request):
    if request.method == 'POST':
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            user_email = form.cleaned_data['email']
            associated_user = get_user_model().objects.filter(Q(email=user_email)).first()
            if associated_user:
                subject = "Password Reset request"
                message = render_to_string("student_registration/forgot_password_request.html", {
                    'user': associated_user,
                    'domain': get_current_site(request).domain,
                    'uid': urlsafe_base64_encode(force_bytes(associated_user.pk)),
                    'token': account_activation_token.make_token(associated_user),
                    "protocol": 'https' if request.is_secure() else 'http'
                })
                email = EmailMessage(subject, message, to=[associated_user.email])
                if email.send():
                    messages.success(request,
                        """
                        <h2>Password reset sent</h2><hr>
                        <p>
                            We've emailed you instructions for setting your password, if an account exists with the email you entered. 
                            You should receive them shortly.<br>If you don't receive an email, please make sure you've entered the address 
                            you registered with, and check your spam folder.
                        </p>
                        """
                    )
                else:
                    messages.error(request, "Problem sending reset password email, <b>SERVER PROBLEM</b>")

            return redirect('login')

    
    form = PasswordResetForm()
    context={"form": form}
    return render(request,'student_registration/forgot_password_page.html', context)

def password_change(request):
    user = request.user
    if request.method == 'POST':
        form = SetPasswordForm(user, request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your password has been changed")
            return redirect('login')
        else:
            for error in list(form.errors.values()):
                messages.error(request, error)

    form = SetPasswordForm(user)
    context = {'form': form}
    return render(request, 'student_registration/password_change.html', context )

def identify(request):
    context={}
    return render(request, 'student_registration/index.html',context)

#Student Views.....
def profile_fillUp(request):
    form = ProfileForm()
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES,instance=request.user.profile)
        if form.is_valid():
            form.save()
            messages.success(request,"Profile updated succesfully")
            return redirect('navPage')
        else:
            for error in list(form.errors.values()):
                messages.error(request, error)
    context ={'form':form}
    return render(request,'student_registration/student/student_profile_form.html',context)

@unauthenticated_user
def login_page(request):
    page = 'student_login'
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password1')

        try:
            user = User.objects.get(email=email)
        except:
            messages.error(request,'user not found')

        user = authenticate(request,email=email, password=password)
        if user is not None:
            login(request,user)
            if user.is_superuser:
                return redirect('admin')
            else:
                return redirect('navPage')
        else:
            messages.error(request,'user does not exist')
    context ={'page':page}
    return render(request,'student_registration/student/student_login_page.html', context)


def registerUser(request):
    form = StudentUserForm()
    if request.method == 'POST':
        form = StudentUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.email = user.email.lower()
            user.is_student=True
            user.role = "STUDENT"
            group = Group.objects.get(name='student')
            user.save()
            user.groups.add(group)
            
            activateEmail(request, user, form.cleaned_data.get('email'))
            return redirect('navPage')
        else:
            for error in list(form.errors.values()):
                messages.error(request,error)
    context = {'form':form}
    return render(request,'student_registration/student/student_login_page.html',context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['student'])
def mainNavPage(request):
    context ={}
    return render(request,'student_registration/student/student_navigation_page.html',context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['student'])
def profile(request, pk):
    user = User.objects.get(id=pk)
    context = {'user':user}
    return render(request,'student_registration/student/student_profile_page.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['student'])
def editProfile(request,pk):
    user = User.objects.get(id=pk)
    profile_user= Profile.objects.get(user__id=request.user.id)
    form = StudentUserForm(instance=user)
    pform=ProfilePicture(instance=profile_user)
    form_p=ProfileForm(instance=profile_user)

    if request.method == 'POST':
        form = EditUserForm(request.POST, request.FILES, instance=user)
        pform=ProfilePicture(request.POST, request.FILES, instance=profile_user)
        form_p= EditProfileForm(request.POST, request.FILES, instance=profile_user)
        if form.is_valid() and pform.is_valid() and form_p.is_valid():
            form.save()
            pform.save()
            form_p.save()
            messages.success(request,"Profile updated succesfully")
            return redirect('profile', pk=pk)
        else:
            for error in list(form.errors.values()):
                messages.error(request, error)
    context ={'form':form,'pform':pform, "profile_user":profile_user,'form_p':form_p}
    return render(request,'student_registration/student/edit_student_profile.html',context)

def reservation(request):
    drivers = User.objects.filter(role='DRIVER')
    context={'drivers':drivers}
    return render(request,'student_registration/reservation_page.html',context)

def reservation_driver_info(request,pk):
    driver = User.objects.get(id=pk)
    context = {'driver':driver}
    return render(request,'student_registration/reserve-driver-info.html',context)

def reserve_service(request,pk):
    current_driver = User.objects.get(id=pk)
    profile_driver = Driverprofile.objects.get(user__id=pk)
    profile_user= Profile.objects.get(user__id=request.user.id)
    reservation=Reservation.objects.get(user__id=request.user.id)
    reservation.driver= profile_driver
    reservation.save()
    context={'driver': current_driver ,'profile_user':profile_user,'reservation':reservation}
    return render(request,'student_registration/reserve-driver-info.html',context)

#Student views ends here....


#Driver views....
@login_required(login_url='login')
@allowed_users(allowed_roles=['driver','admin'])
def driver_profile_fillUp(request):
    form = DriverProfileForm()
    if request.method == 'POST':
        form = DriverProfileForm(request.POST, request.FILES,instance=request.user.driverprofile)
        if form.is_valid():
            form.save()
            messages.success(request,"Profile updated succesfully")
            return redirect('DrivernavPage')
        else:
            for error in list(form.errors.values()):
                messages.error(request, error)
    context ={'form':form}
    return render(request,'student_registration/driver/driver_profile_form.html',context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['driver'])
def edit_driver_profile(request,pk):
    user = User.objects.get(id=pk)
    profile_user = Driverprofile.objects.get(user__id=request.user.id)
    form = DriverUserForm(instance=user)
    pform=DriverProfilePicture(instance=profile_user)
    form_p=EditDriverProfileForm(instance=profile_user)

    if request.method == 'POST':
        form = EditUserForm(request.POST, request.FILES, instance=user)
        pform=DriverProfilePicture(request.POST, request.FILES, instance=profile_user)
        form_p= EditDriverProfileForm(request.POST, request.FILES, instance=profile_user)
        if form.is_valid() and pform.is_valid() and form_p.is_valid():
            form.save()
            pform.save()
            form_p.save()
            messages.success(request,"Profile updated succesfully")
            return redirect('driver-profile', pk=pk)
        else:
            for error in list(form.errors.values()):
                messages.error(request, error)
    context ={'form':form,'pform':pform, "profile_user":profile_user,'form_p':form_p}
    return render(request,'student_registration/driver/edit_driver_profile.html',context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['driver','admin'])
def driver_profile_page(request,pk):
    user = User.objects.get(id=pk)
    context = {'user':user}
    return render(request,'student_registration/driver/driver_profile_page.html', context)

def driver_security_settings(request,pk):
    user = User.objects.get(id=pk)
    context = {'user':user}
    return render(request,'student_registration/driver/security_setting.html', context)

@unauthenticated_user
def driver_login_page(request):
    page = 'driver_login'
    if request.user.is_authenticated:
        return redirect('DrivernavPage')
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password1')

        try:
            user = User.objects.get(email=email)
        except:
            messages.error(request,'user not found')

        user = authenticate(request,email=email, password=password)
        if user is not None:
    
            login(request,user)
            return redirect('DrivernavPage')
        else:
            messages.error(request,'user does not exist')
    context ={'page':page}
    return render(request,'student_registration/driver/driver_login_page.html', context)

def driver_register_page(request):
    page = 'driver_register'
    form = DriverUserForm()
    if request.method == 'POST':
        form = DriverUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.email = user.email.lower()
            user.role = "DRIVER"
            user.is_driver=True
            group = Group.objects.get(name='driver')
            user.save()
            user.groups.add(group)
            
            activateEmail(request, user, form.cleaned_data.get('email'))
            return redirect('navPage')
        else:
            for error in list(form.errors.values()):
                messages.error(request,error)
    context = {'form':form, 'page':page}
    return render(request,'student_registration/driver/driver_login_page.html', context)

@login_required(login_url='driver-login')
@allowed_users(allowed_roles=['driver','admin'])
def drivermainNavPage(request):
    context ={}
    return render(request,'student_registration/driver/driver_navigation_page.html',context )
#driver views ends here.....

@login_required(login_url='login')
def logoutPage(request):
    logout(request)
    return redirect('identify')

def not_allowed(request):
    context = {}
    return render(request,'student_registration/not_allowed.html',context)






