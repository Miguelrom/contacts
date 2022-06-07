from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic

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
