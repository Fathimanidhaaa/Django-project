class customerUserForm(forms.MdelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','password']
        widgets={
            'password':forms.passwordInput()
        }
class CustomerForm(forms.ModelForm):
    class Meta:
        model=Customer
        fields=['address','mobile','profile_pic']