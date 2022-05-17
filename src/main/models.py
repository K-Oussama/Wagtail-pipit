# from .pages import *
from statistics import mode
from unicodedata import name
from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from customimage.models import CustomRendition
from mptt.models import MPTTModel, TreeForeignKey

from django.contrib.auth.models import User
# Create your models here.


from modelcluster.fields import ParentalKey

from wagtail.core.models import Page, Orderable
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers  import FieldPanel, MultiFieldPanel, InlinePanel
from wagtail.search import index



class Category(MPTTModel):
    name = models.CharField(verbose_name=_("Category Name"), help_text=_("Required and unique"), max_length=255, unique=True,)
    slug= models.SlugField(verbose_name=_("Category Safe URL"), max_length=255, unique=True)
    parent = TreeForeignKey("self", on_delete=models.CASCADE, null=True, blank=True, related_name="children")
    is_active = models.BooleanField(default=True)

    class MPTTMeta:
        order_insertion_by = ["name"]

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")

    def get_absolute_url(self):
        return reverse("store:category_list", args=[self.slug])

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    cover_photo = models.ForeignKey('wagtailimages.Image',null=True, blank=True,on_delete=models.SET_NULL,related_name='+')
    image = models.ImageField(verbose_name=_("image"), help_text=_("Upload a Post image"), upload_to="images/", default="images/default.png",)
    content = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.RESTRICT)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete= models.CASCADE,related_name='blog_posts')
    created_on = models.DateTimeField(auto_now_add=True, editable=False)
    updated_on = models.DateTimeField(auto_now= True)
    is_active = models.BooleanField(verbose_name=_("Post visibility"),help_text=_("Change Post visibility"),default=True,)

 #   panels = [
 #       FieldPanel('title'),
 #       FieldPanel('author'),
 #      FieldPanel('cover_photo')
 #  ]

    class Meta:
        ordering = ['-created_on']
        verbose_name_plural = _("Posts")

    def __str__(self):
        return self.title

'''
class PostImage(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="post_image")
    image = models.ImageField(verbose_name=_("image"), help_text=_("Upload a Post image"), upload_to="images/", default="images/default.png",)
    alt_text = models.CharField(verbose_name=_("Alturnative text"), help_text=_("Please add alturnative text"), max_length=255, null=True, blank=True,)
    is_feature = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("Post Image")
        verbose_name_plural = _("Post Images")
'''