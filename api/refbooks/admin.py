from django.contrib import admin

from api.refbooks.models import (ReferenceBook,
                                 ReferenceBookVersion,
                                 ReferenceBookElement)

admin.site.register(ReferenceBook)
admin.site.register(ReferenceBookElement)


@admin.register(ReferenceBookVersion)
class ReferenceBookVersionAdmin(admin.ModelAdmin):

    class ReferenceBookItemInline(admin.StackedInline):
        model = ReferenceBookElement

    inlines = [ReferenceBookItemInline]
