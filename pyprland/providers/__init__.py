"""This module is the entry point for the providers packages."""

from typing import Any

from pyprland.types import IOProvider

from . import dummy, hyprland

available_providers = {"hyprland": hyprland, "dummy": dummy}

enabled_providers: dict[str, Any] = {}


def get_providers() -> dict[str, IOProvider]:
    """Return the providers."""
    if not enabled_providers:
        for name, provider in available_providers.items():
            if provider.is_enabled():
                enabled_providers[name] = provider.get_handles()
    return enabled_providers
