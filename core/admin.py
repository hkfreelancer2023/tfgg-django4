from django.contrib import admin
from core.models import Area, District
# Register your models here.
@admin.register(Area)
class AreaAdmin(admin.ModelAdmin):
    list_display=('id','area_code', 'area_name','area_name_zh_hk')

@admin.register(District)
class DistrictAdmin(admin.ModelAdmin):
    
    #list_editable=('area_code','district_code', 'district_name')
    list_display_links = ('id','district_code')
    readonly_fields = ('lastupdate','createdat')
    
    def get_readonly_fields(self, request, obj=None):
        if obj: # editing an existing object
            if 'district_code' not in self.readonly_fields:
                readonly_list = list(self.readonly_fields)
                readonly_list.insert(0,'district_code')
                self.readonly_fields = tuple(readonly_list)
            #return ('district_code') +self.readonly_fields
            return self.readonly_fields            
        return self.readonly_fields
    
    list_display=('id','area_code','district_code', 'district_name','lastupdate')
    fields=('area_code','district_code', 'district_name','district_name_zh_hk',('createdat','lastupdate'))
    