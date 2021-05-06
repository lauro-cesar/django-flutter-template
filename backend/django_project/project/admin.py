from django.contrib import admin


class BaseModelAdmin(admin.ModelAdmin):
    save_on_top = True
    date_hierarchy = "created"
    list_per_page = 10
    list_max_show_all = 50
    actions_on_bottom = True
    exclude = ["isActive", "isDone", "isComplete", "isPublic", "isProcessed"]


class BaseModelAdminTabular(admin.TabularInline):
    ""


class AdminSite(admin.AdminSite):
    site_header = "Django dashboard"
    site_title = "Admin Dashboard"
