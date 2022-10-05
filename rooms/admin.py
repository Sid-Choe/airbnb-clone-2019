from django.contrib import admin
from . import models
from django.utils.safestring import mark_safe

@admin.register(models.RoomType, models.Amenity, models.Facility, models.HouseRule)
class ItemAdmin(admin.ModelAdmin):

    """ Room Admin Definition """

    list_display = ("name", "used_by")

    def used_by(self, obj):
        return obj.rooms.count()

    pass

class PhotoInline(admin.TabularInline):

    model = models.Photo

@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):

    """ Room Admin Definition """

    inlines = (PhotoInline, )

    fieldsets = (
        (
            "Basic Info",
            {"fields": ("name", "description", "country", "city", "address", "price")}
        ),
        (
            "Spaces", {"fields": ("guests", "beds", "bedrooms",)}
        ),
        (
            "Times",
            {"fields": ("check_in","check_out","instant_book")}
        ),
        (
            "More About the Space",
            {"fields": ("amenities", "facility", "house_rules")}
        ),
        (
            "Last Details", {"fields": ("host",)}
        )
    )

    list_display = (
        "name",
        "country",
        "city",
        "price",
        "guests",
        "beds",
        "bedrooms",
        "baths",
        "check_in",
        "check_out",
        "instant_book",
        "count_amenities",
        "photo_counts",
        "total_rating",
    )

    ordering = ("name",)

    list_filter = ("instant_book", "city", "country")

    search_fields = ("=city", "^host__username")

    raw_id_fields = ("host", )

    filter_horizontal = ("amenities", "facility", "house_rules")

    def count_amenities(self, obj):
        return obj.amenities.count()

    def photo_counts(self, obj):
        return obj.photos.count()


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):

    """ Photo Admin Definition """

    list_display = ("__str__", "get_thumbnail")

    def get_thumbnail(self, obj):
        return mark_safe(f'<img width="50px" src="{obj.file.url}" />')
    get_thumbnail.short_description = "Thumbnail"