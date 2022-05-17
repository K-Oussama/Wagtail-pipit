from django.contrib import admin
from main import pages

from sitesettings.models import SiteSetting
#from wagtail.models import Page, Orderable
from mptt.admin import MPTTModelAdmin
from main.models import(
    Category,
    Post,
    #PostImage,
)
from wagtail.contrib.modeladmin.options import(
   ModelAdmin,
   modeladmin_register,
)
from wagtail.search import index
#wagtail Default

class SiteSettingAdmin(admin.ModelAdmin):
    pass

admin.site.register(SiteSetting, SiteSettingAdmin)


#django

admin.site.register(Category, MPTTModelAdmin)
"""
class PostImageInline(admin.TabularInline):
    model = PostImage

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    inlines = [
       PostImageInline 
    ]
"""
#wagtail


class PostAdmin (ModelAdmin):
    #PostImage admin
    model=Post
    menu_label="Posts"
    menu_icon="placeholder"
    add_to_settings_menu=False
    menu_order=291
    exclude_from_explorer=False
    list_display=("cover_photo","title", "slug","author","updated_on","is_active")
    search_fields=("title", "slug","author","category")
"""
    search_fields = Page.search_fields + [
        index.SearchField('title'),
        index.FilterField('date'),
    ]
"""
modeladmin_register(PostAdmin)


class CategoryAdmin (ModelAdmin):
    #PostImage admin
    model=Category
    menu_label="Categories"
    menu_icon="placeholder"
    add_to_settings_menu=False
    menu_order=290
    exclude_from_explorer=False
    list_display=("name", "parent","is_active")
    search_fields=("name", "parent","is_active")

modeladmin_register(CategoryAdmin)



