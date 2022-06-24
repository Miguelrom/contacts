from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from django.urls import reverse_lazy
from django.db.models import Q

from .models import Contact
from .forms import ContactForm

class AboutTemplateView(generic.TemplateView):
    template_name = 'directory/about.html'


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


class ContactUpdateView(generic.UpdateView):
    model = Contact
    form_class = ContactForm
    template_name = "directory/contact_update_form.html"


class ContactCreateView(generic.CreateView):
    model = Contact
    form_class = ContactForm
    template_name = "directory/contact_create_form.html"


class ContactSearchView(generic.ListView):
    model = Contact
    template_name = 'directory/contact_search.html'
    context_object_name = 'contacts'
    paginate_by = 10
    success_url = reverse_lazy('contact-search')

    def get_queryset(self, **kwargs):
        if 'search_query' in self.request.GET:
            queryset = Contact.objects.filter(
                Q(name__icontains=self.request.GET['search_query']) |
                Q(last_name__icontains=self.request.GET['search_query']))

            return queryset
        else:
            return Contact.objects.none()


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_query'] = self.request.GET['search_query']
        return context




