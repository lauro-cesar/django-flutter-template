from django.contrib import admin
from leaflet.admin import LeafletGeoAdmin


class BaseModelAdmin(LeafletGeoAdmin):
    save_on_top = True
    date_hierarchy = "created"
    list_per_page = 10
    list_max_show_all = 50


class AdminSite(admin.AdminSite):
    site_header = "Project site name"
    site_title = "Admin Dashboard"
