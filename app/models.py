import random
import string
import cloudinary
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone
from django.utils.datetime_safe import datetime
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django_quill.fields import QuillField
from Afford_Health import settings


def token_generator(size=4, chars=string.digits):
    """
    utility function to generate random identification numbers
    """

    return "AH" + ''.join(random.choice(string.digits) for x in range(size)) + ''.join(
        random.choice(string.ascii_uppercase) for x in range(size))


class CustomUser(AbstractUser):
    email = models.EmailField(_('email address'), unique=True)


class Cause(models.Model):
    """
    models class for causes
    """
    name = models.CharField(max_length=2000, null=False, blank=False)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, blank=True)
    image = CloudinaryField('image', null=True, blank=True, max_length=2000)
    description = models.TextField(max_length=5000, blank=True)
    hospital_address = models.CharField(max_length=2000, null=True, blank=False)
    reference_code = models.CharField(max_length=30, null=True, blank=False)
    target = models.DecimalField(max_digits=8, decimal_places=2)
    donated = models.DecimalField(max_digits=8, decimal_places=2, default=0.00)
    approved = models.BooleanField(default=False)
    donor_count = models.IntegerField(default=0)
    date_created = models.DateTimeField(default=timezone.now)
    last_updated = models.DateTimeField(default=timezone.now)

    @property
    def percentage_done(self):
        percent = round((self.donated / self.target) * 100)

        return percent

    @property
    def share_url(self):
        return settings.BASE_URL + 'cases/' + str(self.id)

    @property
    def completed(self):
        return self.donated >= self.target

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        """
        :return:
        """

        self.last_updated = datetime.now()
        self.reference_code = token_generator()

        super().save(*args, **kwargs)

    def __unicode__(self):
        try:
            public_id = self.image.public_id
        except AttributeError:
            public_id = ''
        return f"Photo {self.name} {public_id}"

    def get_absolute_url(self):
        return reverse('cause_detail', args=[str(self.id)])


class DonationTransactionHistory(models.Model):
    """
    Model for donation transactions
    """
    cause = models.ForeignKey(Cause, on_delete=models.CASCADE, null=True)
    amount_donated = models.DecimalField(max_digits=8, decimal_places=2, default=0.00)
    donor_name = models.CharField(null=True, blank=True, max_length=500)
    date_created = models.DateTimeField(default=timezone.now)
    last_updated = models.DateTimeField(default=timezone.now)


class Category(models.Model):
    """
    model class for blog category
    """
    name = models.CharField(max_length=500, unique=True, blank=False, null=False, primary_key=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"


class BlogPost(models.Model):
    """
    model class for blog post
    """
    title = models.CharField(max_length=500, blank=True)
    body = QuillField()
    block_quote = models.CharField(max_length=1000, null=True, blank=False)
    image = CloudinaryField('image', null=True, blank=True, max_length=2000)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, blank=True)
    slug = models.CharField(max_length=200, null=True, blank=True)
    date_created = models.DateTimeField(default=timezone.now)
    last_updated = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    @property
    def share_url(self):
        return settings.BASE_URL + 'blog/' + str(self.id)

    def save(self, *args, **kwargs):
        """
        :return:
        """
        self.last_updated = datetime.now()
        super().save(*args, **kwargs)

    def __unicode__(self):
        try:
            public_id = self.image.public_id
        except AttributeError:
            public_id = ''
        return f"Photo {self.title} {public_id}"

    def get_absolute_url(self):
        return reverse('blog_detail', args=[str(self.id)])


class Comment(models.Model):
    """
    model class for comments in a blog post
    """
    body = models.CharField(max_length=1000, null=False, blank=True)
    name = models.CharField(max_length=300, null=False, blank=False, default="foo")
    email = models.CharField(max_length=300, null=False, blank=False, default="foo@gmail.com")
    # author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    # replies = models.ForeignKey('self', on_delete=models.CASCADE)
    blog_post = models.ForeignKey(BlogPost, related_name="comments", on_delete=models.CASCADE)

    def __str__(self):
        return self.body

    def save(self, *args, **kwargs):
        """
        :return:
        """
        self.last_updated = datetime.now()
        super().save(*args, **kwargs)

#
# class CustomerInfo(models.Model):
#     full_name = models.CharField(max_length=150)
#     email = models.EmailField()
#     phone_number = models.CharField(max_length=20)
#     address = models.CharField(max_length=150)
