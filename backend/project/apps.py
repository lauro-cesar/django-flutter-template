from django.contrib.admin.apps import AdminConfig


class ProjectConfig(AdminConfig):
    default_site = "project.admin.AdminSite"
