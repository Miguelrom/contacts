from django.db import models
from django.urls import reverse

class Contact(models.Model):

    name = models.CharField(max_length=50)

    last_name = models.CharField(max_length=100)

    email = models.EmailField()

    phone_number = models.CharField(max_length=10, blank=True)

    company = models.CharField(max_length=50, blank=True)

    class Meta:
        ordering = ['last_name']
        db_table = 'contacts'

    def get_absolute_url(self):
        """Returns the url to access a detail view of a contact instance."""
        return reverse('contact-detail', args=[str(self.id)])

    def __str__(self):
        return self.name + " " + self.last_name


