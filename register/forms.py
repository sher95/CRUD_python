from django import forms
from .models import Emp
class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Emp
        fields = ('fullName', 'mobile', 'empCode', 'position')
        labels = {
            'fullName': 'Full Name',
            'empCode': 'EMP. Code'
        }

    def __init__(self, *args, **kwargs):
        super(EmployeeForm, self).__init__(*args, **kwargs)
        self.fields['position'].empty_label = "Tanlov"
        self.fields['empCode'].required = False