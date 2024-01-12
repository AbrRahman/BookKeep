from django.contrib import admin
from books.models import Book,Category,Borrow,Comment

class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        "name",
    )
    prepopulated_fields = {"slug": ("name",)}

admin.site.register(Book)
admin.site.register(Borrow)
admin.site.register(Comment)
admin.site.register(Category,CategoryAdmin)


