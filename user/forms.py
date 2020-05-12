from django import forms
from .models import user_profile, User


class django_user_form(forms.ModelForm):
    class Meta():
        model = User
        fields = ['username','first_name', 'last_name', 'password', 'email']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'field'}),
            'first_name': forms.TextInput(attrs={'class': 'field'}),
            'last_name': forms.TextInput(attrs={'class': 'field'}),
            'email': forms.EmailInput(attrs={'class': 'field'}),
            'password': forms.PasswordInput(attrs={'class': 'field'}),
        }

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if username.isupper():
            raise forms.ValidationError('username must be in lower case')
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        # print(User.objects.filter(email=email))
        if User.objects.filter(email=email):
            raise forms.ValidationError("email already in use")
        return email


class user_profile_form(forms.ModelForm):
    class Meta():
        model = user_profile
        fields = ['regno', 'branch','profile_pic','group','roomno','hostel']
        # exclude = ['user']
        widgets = {
            'regno': forms.NumberInput(attrs={'class': 'field'}),
            'roomno': forms.NumberInput(attrs={'class': 'field'}),
        }
       
    branch = forms.CharField(required=True, widget=forms.Select(
        attrs={
            "class": "field"
        }, choices=(
            ('cs', 'Computer Science'),
            ('it', 'Information Technology'),
            ('ece', 'Electronics & Comm.'),
            ('ee', 'Electrical'),
            ('mech', 'Mechanical'),
            ('chemical', 'Chemical'),
            ('civil', 'Civil'),
            ('pi', 'Production & Ind.'),
            ('bt', 'Biotechnology'),
            
        )
    )) 

    hostel = forms.CharField(required=True, widget=forms.Select(
        attrs={
            "class": "field"
        }, choices=(
            ('svbh', 'SVBH'),
            ('kngh', 'KNGH'),
            
            
            
        )
    ))
    group = forms.CharField(required=True, widget=forms.Select(
        attrs={
            "class": "field"
        }, choices=(
            ('A1','A1'),
            ('A2','A2'),
            ('B1','B1'),
            ('B2','B2'),
            ('C1','C1'),
            ('C2','C2'),
            ('D1','D1'),
            ('D2','D2'),
            ('E1','E1'),
            ('E2','E2'),
            ('F1','F1'),
            ('F2','F2'),
            ('G1','G1'),
            ('G2','G2'),
            ('H1','H1'),
            ('H2','H2'),
            ('I1','I1'),
            ('I2','I2'),
            ('J1','J1'),
            ('J2','J2'),
            
        )
    ))
        
 