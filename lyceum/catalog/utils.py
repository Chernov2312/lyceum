__all__ = ['get_image_upload_path', 'get_main_image_upload_path']


def get_image_upload_path(instance, filename):
    if hasattr(instance, 'items') and instance.items.exists():
        item = instance.items.first()
        return f'uploads/item_{item.id}/{filename}'

    return f'uploads/temp/{filename}'


def get_main_image_upload_path(instance, filename):
    if hasattr(instance, 'main_item') and instance.main_item.exists():
        item = instance.main_item.first()
        return f'main/item_{item.id}/{filename}'

    return f'main/temp/{filename}'
