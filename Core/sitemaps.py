from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from dogefather_web.config import protocol


class StaticViewSitemap(Sitemap):
    priority = 1
    changefreq = 'weekly'

    def items(self):
        return ['home', 'tesla']

    def location(self, item):
        return reverse(item)
