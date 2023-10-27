from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.
class Area(models.Model):
    """
    define area table
    """
    class Meta:
        verbose_name_plural = _('Area')
        ordering = ["id"]

    ## Automatic primary key fields
    ## id = models.BigAutoField(primary_key=True)
    area_code = models.CharField(verbose_name=_('Area Code'),unique=True, max_length=8, null = False,blank=True)
    area_name = models.CharField(verbose_name=_('Area Name'),max_length=50, null = False,blank=True)
    area_name_zh_hk = models.CharField(verbose_name=_('Area Chinese Name'),max_length=50, null = False,blank=True)
    createdat = models.DateTimeField(verbose_name=_("Created at"), auto_now_add=True, null=True )
    lastupdate = models.DateTimeField(verbose_name=_("Last update Time"), auto_now_add=True, null=True )

    def __str__(self):
        return f'{self.area_name} ({self.area_code})'

class District(models.Model):
    """
    define area table
    """
    class Meta:
        verbose_name_plural = _('Districts')
        ordering = ["id"]

    district_code = models.CharField(verbose_name=_('District Code'),unique=True, max_length=8, null = False,blank=False)
    #area_code = models.CharField(verbose_name=_('Area Code'),unique=True, max_length=8, null = False,blank=True)
    area_code = models.ForeignKey(Area, to_field= 'area_code', on_delete= models.CASCADE)
    #area = models.ForeignKey(Area, on_delete= models.PROTECT)
    district_name = models.CharField(verbose_name=_('District Name'),max_length=50, null = False,blank=True)
    district_name_zh_hk = models.CharField(verbose_name=_('District Chinese Name'),max_length=50, null = False,blank=True)
    createdat = models.DateTimeField(verbose_name=_("Created at"), auto_now_add=True, null=True )
    lastupdate = models.DateTimeField(verbose_name=_("Last update Time"), auto_now_add=True, null=True )

    def __str__(self) -> str:
        return f'{self.district_name} ({self.area_code})'