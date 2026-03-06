from pathlib import Path

from django.conf import settings
from django.http import FileResponse, Http404

__all__ = ['download']


def download(request, file_path):
    base_dir = Path(settings.MEDIA_ROOT)
    full_path = base_dir / file_path

    if not str(full_path.resolve()).startswith(str(base_dir.resolve())):
        raise Http404('Недопустимый путь к файлу')

    if not full_path.exists() or not full_path.is_file():
        raise Http404('Файл не найден')

    return FileResponse(
        open(full_path, 'rb'),
        as_attachment=True,
        filename=full_path.name,  # вместо os.path.basename
    )
