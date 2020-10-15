from django.utils.translation import ugettext_lazy as _


from admin_tools.dashboard import modules, Dashboard, AppIndexDashboard


class MainDashboard(Dashboard):
    """
    Custom index dashboard for backend.
    """

    columns = 2
    title = ""

    def init_with_context(self, context):

        self.children.append(
            modules.ModelList(
                title=_("Users and groups"),
                models=[
                    "django.contrib.auth.*",
                    "accounts.models.*",
                ],
            )
        )

        self.children.append(
            modules.ModelList(
                title=_("Task Manager"),
                models=["django_celery_beat.models.*"],
            )
        )

        self.children.append(
            modules.ModelList(title=_("File manager"), models=["filer.*"])
        )

        self.children.append(
            modules.ModelList(
                title=_("Frontend"),
                models=["django.contrib.sites.*", "django.contrib.flatpages.*"],
            )
        )

        self.children.append(
            modules.LinkList(
                _("Support"),
                draggable=True,
                deletable=True,
                collapsible=True,
                children=[
                    {
                        "title": _("Página do desenvolvedor"),
                        "url": "https://www.linkedin.com/in/lauro-cesar/",
                        "external": True,
                        "attrs": {"target": "_blank"},
                    },
                    {
                        "title": _("lauro@hostcert.com.br"),
                        "url": "mailto://lauro@hostcert.com.br",
                        "external": True,
                        "attrs": {"target": "_blank"},
                    },
                ],
            )
        )


class MainAppIndexDashboard(AppIndexDashboard):
    """
    Custom app index dashboard for backend.
    """

    # we disable title because its redundant with the model list module
    title = ""

    def __init__(self, *args, **kwargs):
        AppIndexDashboard.__init__(self, *args, **kwargs)
        # append a model list module and a recent actions module
        self.children += [
            modules.ModelList(self.app_title, self.models),
            modules.RecentActions(
                _("Recent Actions"), include_list=self.get_app_content_types(), limit=5
            ),
        ]

    def init_with_context(self, context):
        """
        Use this method if you need to access the request context.
        """
        return super(MainAppIndexDashboard, self).init_with_context(context)
