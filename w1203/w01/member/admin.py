from django.contrib import admin
from member.models import Member
#

class MemberAdmin(admin.ModelAdmin):
  list_display = ['id','name','nicName','mdate']

admin.site.register(Member,MemberAdmin)












# # admin에서 보여지는거
# @admin.register(Member)
# class MemberAdmin(admin.ModelAdmin):
#   list_display = ['id','name','nicName','mdate']

# # 관리자페이지 컬럼 보이기
# # admin.site.register(Member,MemberAdmin)