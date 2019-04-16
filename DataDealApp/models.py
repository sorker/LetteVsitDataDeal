from django.db import models

# Create your models here.

class SiteInfo(models.Model):
    site_ip = models.CharField(u'站点', max_length=100)

    def __str__(self):
        return str(self.id)


class ComplaintRawData(models.Model):
    title = models.CharField(u'标题', max_length=200)
    content = models.CharField(u'内容', max_length=2000)
    reflecting_time = models.CharField(u'反映时间', max_length=20)
    reply_unit = models.CharField(u'答复单位', max_length=50)
    reply_time = models.CharField(u'答复时间', max_length=20)
    reply_opinion = models.CharField(u'答复意见', max_length=2000)
    province = models.CharField(u'省', max_length=10, default='浙江省')
    city = models.CharField(u'城市', max_length=20)
    city_area = models.CharField(u'地区', max_length=20)
    datetime = models.DateField(u'获取时间', auto_now=True)

    def __str__(self):
        return str(self.id)


class CityArea(models.Model):
    city = models.CharField(u'城市', max_length=10)
    city_area = models.CharField(u'地区', max_length=20)

    def __str__(self):
        return str(self.id)
