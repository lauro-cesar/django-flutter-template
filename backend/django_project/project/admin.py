from django.contrib import admin


class AdminSite(admin.AdminSite):
    site_header = "Django dashboard"
    site_title = "Admin Dashboard"
