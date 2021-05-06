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
    # class Media:
    #     css = {'all': ('css/mymenu.css',)}
    #     js = ('js/mymenu.js',)

    def __init__(self, **kwargs):
        super(MainMenu, self).__init__(**kwargs)
        self.children += [
            items.MenuItem("Painel administrativo", reverse("admin:index")),
            items.Bookmarks("Atalhos salvos"),
            items.MenuItem(
                "Filmes",
                children=[
                    items.MenuItem(
                        "Adicionar filme",
                        "/admin/movies/moviemodel/add/",
                    ),
                    items.MenuItem(
                        "Adicionar genero",
                        "/admin/movies/genremodel/add/",
                    ),
                ],
            ),
        ]

    def init_with_context(self, context):
        """
        Use this method if you need to access the request context.
        """
        return super(MainMenu, self).init_with_context(context)
