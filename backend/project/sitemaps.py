from django.contrib.sitemaps import Sitemap
from django.contrib.flatpages.models import FlatPage


class FlapPagesSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.5
    protocol = "https"

    def items(self):
        return FlatPage.objects.all()
