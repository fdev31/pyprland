"""Provides hyprland IO support."""

import os


from pyprland.types import IOProvider


async def notify(message, *a, **kw):
    os.system(f"notify-send {message}")


async def nothing(*a, **kw):
    pass


def get_handles() -> IOProvider:
    return IOProvider(
        notify_info=notify,
        notify_error=notify,
        notify_fatal=notify,
        get_event_stream=None,
        init=lambda: None,
        notify=notify,
        send_command=nothing,
        get_info=nothing,
    )


def is_enabled():
    return True
