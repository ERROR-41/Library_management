from django.contrib import admin
from library.models import Author, Book, BorrowRecord

# Register your models here.
admin.site.register(Author)


class BorrowRecordAdmin(admin.ModelAdmin):
    list_display = ("book", "borrow_date", "return_date")
    list_filter = ("borrow_date", "return_date")


class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "availability_status")
    ordering = ("id",)


admin.site.register(BorrowRecord, BorrowRecordAdmin)
admin.site.register(Book, BookAdmin)
