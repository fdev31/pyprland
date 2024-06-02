"""Provides hyprland IO support."""

import os

from pyprland.hyprland_ipc import get_event_stream, hyprctl, hyprctl_json, notify, notify_error, notify_fatal, notify_info
from pyprland.hyprland_ipc import init as ipc_init
from pyprland.types import IOProvider


def get_handles() -> IOProvider:
    return IOProvider(
        notify_info=notify_info,
        notify_error=notify_error,
        notify_fatal=notify_fatal,
        get_event_stream=get_event_stream,
        init=ipc_init,
        notify=notify,
        send_command=hyprctl,
        get_info=hyprctl_json,
    )


def is_enabled() -> bool:
    return "HYPRLAND_INSTANCE_SIGNATURE" in os.environ
