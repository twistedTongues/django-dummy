# from django.db.models.signals.post_delete import *
import os
# from pathlib import Path

"""For signals handlers"""


def photo_cover_cleaner(sender, instance, *args, **kwargs):
    print(f"The sender is: {sender}, the instance is: {instance}")
    try:
        os.remove(instance.photo_cover.file.name)
    except:
        pass
