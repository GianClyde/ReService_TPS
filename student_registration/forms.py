from django import forms 
from django.contrib.auth.forms import UserCreationForm,SetPasswordForm,PasswordResetForm
from django.forms import ModelForm
from .models import User,Profile,Driverprofile,StudentUser,DriverUser,Vehicle
from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model
# Create your forms here.

from django import forms

class DriverUserForm(UserCreationForm):
    class Meta:
        model = DriverUser
        fields = ('email','password1','password2','first_name','last_name','middle_name','contact_no')
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].widget.attrs.update({
            'class': 'form-input',
            'required':'',
            'name':'email',
            'id':'email',
            'type':'text',
            'placeholder':'Email'})
        self.fields['password1'].widget.attrs.update({
            'class': 'form-input',
            'required':'',
            'name':'password1',
            'id':'password1',
            'type':'text',
            'placeholder':'Password'})
        self.fields['password2'].widget.attrs.update({
            'class': 'form-input',
            'required':'',
            'name':'password2',
            'id':'password2',
            'type':'text',
            'placeholder':'Re enter Password'})
        self.fields['first_name'].widget.attrs.update({
            'class': 'form-input',
            'required':'',
            'name':'first_name',
            'id':'first_name',
            'type':'text',
            'placeholder':'First Name'})
        self.fields['last_name'].widget.attrs.update({
            'class': 'form-input',
            'required':'',
            'name':'last_name',
            'id':'last_name',
            'type':'text',
            'placeholder':'Last Name'})
        self.fields['middle_name'].widget.attrs.update({
            'class': 'form-input',
            'required':'',
            'name':'middle_name',
            'id':'middle_name',
            'type':'text',
            'placeholder':'Middle Name'})
        self.fields['contact_no'].widget.attrs.update({
            'class': 'form-input',
            'required':'',
            'name':'contact_no',
            'id':'contact_no',
            'type':'text',
            'placeholder':'contact_no'})
        
class StudentUserForm(UserCreationForm):
    class Meta:
        model = StudentUser
        fields = ('email','password1','password2','first_name','last_name','middle_name','contact_no')
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].widget.attrs.update({
            'class': 'form-input',
            'required':'',
            'name':'email',
            'id':'email',
            'type':'text',
            'placeholder':'Email'})
        self.fields['password1'].widget.attrs.update({
            'class': 'form-input',
            'required':'',
            'name':'password1',
            'id':'password1',
            'type':'text',
            'placeholder':'Password'})
        self.fields['password2'].widget.attrs.update({
            'class': 'form-input',
            'required':'',
            'name':'password2',
            'id':'password2',
            'type':'text',
            'placeholder':'Re enter Password'})
        self.fields['first_name'].widget.attrs.update({
            'class': 'form-input',
            'required':'',
            'name':'first_name',
            'id':'first_name',
            'type':'text',
            'placeholder':'First Name'})
        self.fields['last_name'].widget.attrs.update({
            'class': 'form-input',
            'required':'',
            'name':'last_name',
            'id':'last_name',
            'type':'text',
            'placeholder':'Last Name'})
        self.fields['middle_name'].widget.attrs.update({
            'class': 'form-input',
            'required':'',
            'name':'middle_name',
            'id':'middle_name',
            'type':'text',
            'placeholder':'Middle Name'})
        self.fields['contact_no'].widget.attrs.update({
            'class': 'form-input',
            'required':'',
            'name':'contact_no',
            'id':'contact_no',
            'type':'text',
            'placeholder':'contact_no'})

class ProfilePicture(ModelForm):
    image = forms.ImageField(label="Profile Pciture")
    class Meta:
        model = Profile
        fields=('image',)
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['image'].widget.attrs.update({
            'class': 'form-input'})

class DriverProfilePicture(ModelForm):
    image = forms.ImageField(label="Profile Pciture")
    class Meta:
        model = Driverprofile
        fields=('image',)
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['image'].widget.attrs.update({
            'class': 'form-input'})

class ProfileForm(ModelForm):
    class Meta:
        model=Profile
        fields= ('parent','parent_contactNo','parent_address','birth_date','lot','street','village','city','zipcode',
                 'age','school_branch','section','year_level')
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['parent'].widget.attrs.update({
            'class': 'form-input',
            'required':'',
            'name':'parent',
            'id':'parent',
            'type':'text',
            'placeholder':'parent'})
        self.fields['parent_contactNo'].widget.attrs.update({
            'class': 'form-input',
            'required':'',
            'name':'parent_contactNo',
            'id':'parent_contactNo',
            'type':'text',
            'placeholder':'parent contact number'})
        self.fields['parent_address'].widget.attrs.update({
            'class': 'form-input',
            'required':'',
            'name':'parent_address',
            'id':'parent_address',
            'type':'text',
            'placeholder':'parent address'})
        self.fields['birth_date'].widget.attrs.update({
            'class': 'form-input',
            'required':'',
            'name':'birth_date',
            'id':'birth_date',
            'type': 'date',
            'placeholder': 'yyyy-mm-dd (DOB)'})
        self.fields['lot'].widget.attrs.update({
            'class': 'form-input-add',
            'required':'',
            'name':'lot',
            'id':'lot',
            'type':'text',
            'placeholder':'lot/house no,/bldg no.'})
        self.fields['street'].widget.attrs.update({
            'class': 'form-input-add',
            'required':'',
            'name':'street',
            'id':'street',
            'type':'text',
            'placeholder':'street'})
        self.fields['village'].widget.attrs.update({
            'class': 'form-input-add2',
            'required':'',
            'name':'village',
            'id':'village',
            'type':'text',
            'placeholder':'village'})
        self.fields['city'].widget.attrs.update({
            'class': 'form-input-add2',
            'required':'',
            'name':'city',
            'id':'city',
            'type':'text',
            'placeholder':'city'})
        self.fields['zipcode'].widget.attrs.update({
            'class': 'form-input-add2',
            'required':'',
            'name':'zipcode',
            'id':'zipcode',
            'type':'text',
            'placeholder':'zipcode'})
        self.fields['age'].widget.attrs.update({
            'class': 'form-input',
            'required':'',
            'name':'age',
            'id':'age',
            'type':'text',
            'placeholder':'age'})
        self.fields['school_branch'].widget.attrs.update({
            'class': 'form-input',
            'required':'',
            'name':'school_branch',
            'id':'school_branch',
            'placeholder':'school_branch'})
        self.fields['section'].widget.attrs.update({
            'class': 'form-input',
            'required':'',
            'name':'section',
            'id':'section',
            'type':'text',
            'placeholder':'section'})
        self.fields['year_level'].widget.attrs.update({
            'class': 'form-input',
            'required':'',
            'name':'year_level',
            'id':'year_level',
            'type':'text',
            'placeholder':'year level'})
class EditDriverProfileForm(ModelForm):
    class Meta:
        model=Driverprofile
        fields= ('birth_date','lot','street','village','city','zipcode',
                 'age')
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['birth_date'].widget.attrs.update({
            'class': 'form-input',
            'required':'',
            'name':'birth_date',
            'id':'birth_date',
            'type': 'date',
            'placeholder': 'yyyy-mm-dd (DOB)'})
        self.fields['lot'].widget.attrs.update({
            'class': 'form-input-add',
            'required':'',
            'name':'lot',
            'id':'lot',
            'type':'text',
            'placeholder':'lot/house no,/bldg no.'})
        self.fields['street'].widget.attrs.update({
            'class': 'form-input-add',
            'required':'',
            'name':'street',
            'id':'street',
            'type':'text',
            'placeholder':'street'})
        self.fields['village'].widget.attrs.update({
            'class': 'form-input-add2',
            'required':'',
            'name':'village',
            'id':'village',
            'type':'text',
            'placeholder':'village'})
        self.fields['city'].widget.attrs.update({
            'class': 'form-input-add2',
            'required':'',
            'name':'city',
            'id':'city',
            'type':'text',
            'placeholder':'city'})
        self.fields['zipcode'].widget.attrs.update({
            'class': 'form-input-add2',
            'required':'',
            'name':'zipcode',
            'id':'zipcode',
            'type':'text',
            'placeholder':'zipcode'})
        self.fields['age'].widget.attrs.update({
            'class': 'form-input',
            'required':'',
            'name':'age',
            'id':'age',
            'type':'text',
            'placeholder':'age'})
        

class EditProfileForm(ModelForm):
    class Meta:
        model=Profile
        fields= ('parent','parent_contactNo','parent_address','birth_date','lot','street','village','city','zipcode',
                 'age')
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['parent'].widget.attrs.update({
            'class': 'form-input',
            'required':'',
            'name':'parent',
            'id':'parent',
            'type':'text',
            'placeholder':'parent'})
        self.fields['parent_contactNo'].widget.attrs.update({
            'class': 'form-input',
            'required':'',
            'name':'parent_contactNo',
            'id':'parent_contactNo',
            'type':'text',
            'placeholder':'parent contact number'})
        self.fields['parent_address'].widget.attrs.update({
            'class': 'form-input',
            'required':'',
            'name':'parent_address',
            'id':'parent_address',
            'type':'text',
            'placeholder':'parent address'})
        self.fields['birth_date'].widget.attrs.update({
            'class': 'form-input',
            'required':'',
            'name':'birth_date',
            'id':'birth_date',
            'type': 'date',
            'placeholder': 'yyyy-mm-dd (DOB)'})
        self.fields['lot'].widget.attrs.update({
            'class': 'form-input-add',
            'required':'',
            'name':'lot',
            'id':'lot',
            'type':'text',
            'placeholder':'lot/house no,/bldg no.'})
        self.fields['street'].widget.attrs.update({
            'class': 'form-input-add',
            'required':'',
            'name':'street',
            'id':'street',
            'type':'text',
            'placeholder':'street'})
        self.fields['village'].widget.attrs.update({
            'class': 'form-input-add2',
            'required':'',
            'name':'village',
            'id':'village',
            'type':'text',
            'placeholder':'village'})
        self.fields['city'].widget.attrs.update({
            'class': 'form-input-add2',
            'required':'',
            'name':'city',
            'id':'city',
            'type':'text',
            'placeholder':'city'})
        self.fields['zipcode'].widget.attrs.update({
            'class': 'form-input-add2',
            'required':'',
            'name':'zipcode',
            'id':'zipcode',
            'type':'text',
            'placeholder':'zipcode'})
        self.fields['age'].widget.attrs.update({
            'class': 'form-input',
            'required':'',
            'name':'age',
            'id':'age',
            'type':'text',
            'placeholder':'age'})

        
class DriverProfileForm(ModelForm):
    class Meta:
        model=Driverprofile
        fields= ('birth_date','lot','street','village','city','zipcode',
                 'age','school_branch','franchise','assigned_route','franchise_no','operator','vehicle')
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['vehicle'].widget.attrs.update({
            'class': 'form-input',
            'required':'',
            'name':'vehicle',
            'id':'vehicle',
            'type':'text',
            'placeholder':'Vehicle'})
        self.fields['franchise_no'].widget.attrs.update({
            'class': 'form-input',
            'required':'',
            'name':'franchise_no',
            'id':'franchise_no',
            'type':'text',
            'placeholder':'Franchise no.'})
        self.fields['operator'].widget.attrs.update({
            'class': 'form-input',
            'required':'',
            'name':'operator',
            'id':'operator',
            'type':'text',
            'placeholder':'Operator'})
        self.fields['assigned_route'].widget.attrs.update({
            'class': 'form-input',
            'required':'',
            'name':'assigned_route',
            'id':'assigned_route',
            'type':'text',
            'placeholder':'Route'})
        self.fields['franchise'].widget.attrs.update({
            'class': 'form-input',
            'required':'',
            'name':'franchise',
            'id':'franchise',
            'type':'text',
            'placeholder':'franchise'})
        self.fields['birth_date'].widget.attrs.update({
            'class': 'form-input',
            'required':'',
            'name':'birth_date',
            'id':'birth_date',
            'type': 'date',
            'placeholder': 'yyyy-mm-dd (DOB)'})
        self.fields['lot'].widget.attrs.update({
            'class': 'form-input-add',
            'required':'',
            'name':'lot',
            'id':'lot',
            'type':'text',
            'placeholder':'lot/house no,/bldg no.'})
        self.fields['street'].widget.attrs.update({
            'class': 'form-input-add',
            'required':'',
            'name':'street',
            'id':'street',
            'type':'text',
            'placeholder':'street'})
        self.fields['village'].widget.attrs.update({
            'class': 'form-input-add2',
            'required':'',
            'name':'village',
            'id':'village',
            'type':'text',
            'placeholder':'village'})
        self.fields['city'].widget.attrs.update({
            'class': 'form-input-add2',
            'required':'',
            'name':'city',
            'id':'city',
            'type':'text',
            'placeholder':'city'})
        self.fields['zipcode'].widget.attrs.update({
            'class': 'form-input-add2',
            'required':'',
            'name':'zipcode',
            'id':'zipcode',
            'type':'text',
            'placeholder':'zipcode'})
        self.fields['age'].widget.attrs.update({
            'class': 'form-input',
            'required':'',
            'name':'age',
            'id':'age',
            'type':'text',
            'placeholder':'age'})
        self.fields['school_branch'].widget.attrs.update({
            'class': 'form-input',
            'required':'',
            'name':'school_branch',
            'id':'school_branch',
            'placeholder':'school_branch'})
    


    
class EditUserForm(ModelForm):
    class Meta:
        model = User
        fields = ('first_name','last_name','middle_name','contact_no')
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs.update({
            'class': 'form-control',
            'required':'',
            'name':'first_name',
            'id':'first_name',
            'type':'text',
            'placeholder':'First Name'})
        self.fields['last_name'].widget.attrs.update({
            'class': 'form-control',
            'required':'',
            'name':'last_name',
            'id':'last_name',
            'type':'text',
            'placeholder':'Last Name'})
        self.fields['middle_name'].widget.attrs.update({
            'class': 'form-control',
            'required':'',
            'name':'middle_name',
            'id':'middle_name',
            'type':'text',
            'placeholder':'Middle Name'})
        self.fields['contact_no'].widget.attrs.update({
            'class': 'form-control',
            'required':'',
            'name':'contact_no',
            'id':'contact_no',
            'type':'text',
            'placeholder':'contact_no'})

    
class SetPasswordForm(SetPasswordForm):
    class Meta:
        model = get_user_model()
        fields = ['new_password1', 'new_password2']
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['new_password1'].widget.attrs.update({
                'class': 'form-input',
                'required':'',
                'name':'new_password1',
                'id':'new_password1',
                'type':'text',
                'placeholder':'new password'})
            self.fields['new_password2'].widget.attrs.update({
                'class': 'form-input',
                'required':'',
                'name':'new_password2',
                'id':'new_password2',
                'type':'text',
                'placeholder':'re-enter new password'})

class PasswordResetForm(PasswordResetForm):
    email = forms.EmailField()
    def __init__(self, *args, **kwargs):
        super(PasswordResetForm, self).__init__(*args, **kwargs)
        self.fields['email'].widget.attrs.update({
                'class': 'form-input',
                'required':'',
                'name':'email',
                'id':'email',
                'type':'text',
                'placeholder':'Email'})