from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone
from django.utils.datetime_safe import datetime
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class CustomUser(AbstractUser):
    email = models.EmailField(_('email address'), unique=True)


class Cause(models.Model):
    """
    models class for causes
    """
    name = models.CharField(max_length=2000, null=False, blank=False)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True)
    # image =
    description = models.TextField(max_length=5000, blank=True)
    hospital_address = models.CharField(max_length=2000, null=True, blank=False)
    target = models.DecimalField(max_digits=8, decimal_places=2)
    donated = models.DecimalField(max_digits=8, decimal_places=2, default=0.00)
    approved = models.BooleanField(default=False)
    donor_count = models.IntegerField(default=0)
    date_created = models.DateTimeField(default=timezone.now)
    last_updated = models.DateTimeField(default=timezone.now)

    @property
    def percentage_done(self):
        percent = round((self.donated/self.target) * 100)

        return percent

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
        super().save(*args, **kwargs)

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
    body = models.CharField(max_length=5000,  blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    slug = models.CharField(max_length=200, null=True, blank=True)
    date_created = models.DateTimeField(default=timezone.now)
    last_updated = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        """
        :return:
        """
        self.last_updated = datetime.now()
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('blog_detail', args=[str(self.id)])


class Comment(models.Model):
    """
    model class for comments in a blog post
    """
    body = models.CharField(max_length=1000, null=False, blank=True)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
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
