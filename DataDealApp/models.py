from django.db import models

# Create your models here.

class SiteInfo(models.Model):
    site_ip = models.CharField(u'站点', max_length=100)
    site_urls = models.CharField(u'具体地址', max_length=200)


    def __str__(self):
        return str(self.id)


class ComplaintRawData(models.Model):
    title = models.CharField(u'站点', max_length=100)
    site_urls = models.CharField(u'具体地址', max_length=200)

    def __str__(self):
        return str(self.id)