from django.contrib import admin

from api.refbooks.models import (ReferenceBook,
                                 ReferenceBookVersion,
                                 ReferenceBookItem)

admin.site.register(ReferenceBook)
admin.site.register(ReferenceBookItem)


@admin.register(ReferenceBookVersion)
class ReferenceBookVersionAdmin(admin.ModelAdmin):

    class ReferenceBookItemInline(admin.StackedInline):
        model = ReferenceBookItem

    inlines = [ReferenceBookItemInline]
