from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from django.urls import reverse_lazy

from .models import Contact


def index(request):
    return HttpResponse("Your home page goes here!!!")


class ContactListView(generic.ListView):
    model = Contact
    template_name = 'directory/contacts.html'
    context_object_name = 'contacts'
    paginate_by = 10


class ContactDetailView(generic.DetailView):
    model = Contact
    template_name = 'directory/contact_detail.html'
    context_object_name = 'contact'


class ContactDeleteView(generic.DeleteView):
    model = Contact
    template_name = "directory/contact_confirm_delete.html"
    success_url = reverse_lazy('contacts')


