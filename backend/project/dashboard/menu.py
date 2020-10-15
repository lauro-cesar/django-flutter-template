"""
This file was generated with the custommenu management command, it contains
the classes for the admin menu, you can customize this class as you want.

To activate your custom menu add the following to your settings.py::
    ADMIN_TOOLS_MENU = 'backend.mymenu.CustomMenu'
"""

from django.utils.translation import ugettext_lazy as _
from django.urls import reverse
from admin_tools.menu import items, Menu


class MainMenu(Menu):
    def __init__(self, **kwargs):
        Menu.__init__(self, **kwargs)
        self.children += [
            items.MenuItem(_("Dashboard"), reverse("admin:index")),
        ]

    def init_with_context(self, context):
        """
        Use this method if you need to access the request context.
        """
        return super(MainMenu, self).init_with_context(context)
