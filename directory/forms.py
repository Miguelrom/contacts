from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _

from .models import Contact

class ContactForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['phone_number'].widget.attrs.update({'minlength': '10'})

        self.fields['email'].widget.attrs.update({'placeholder': 'username@email.com'})
        self.fields['phone_number'].widget.attrs.update({'placeholder': '5555555555'})


        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = Contact
        fields = ("name", 'last_name', 'email', 'phone_number', 'company')

        labels = {
            'name': _('Name(s)'),
            'last_name': _('Last name(s)'),
        }




