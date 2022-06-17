from django.forms import ModelForm

from .models import Contact

class ContactForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['phone_number'].widget.attrs.update({'minlength': '10'})

        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = Contact
        fields = ("name", 'last_name', 'email', 'phone_number', 'company')




