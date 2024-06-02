"""This module is the entry point for the providers packages."""

from . import hyprland
from . import dummy
from pyprland.types import IOProvider

from typing import Any

available_providers = {"hyprland": hyprland, "dummy": dummy}

enabled_providers: dict[str, Any] = {}


def get_providers() -> dict[str, dict[str, IOProvider]]:
    """Return the providers."""
    if not enabled_providers:
        for name, provider in available_providers.items():
            if provider.is_enabled():
                enabled_providers[name] = provider.get_handles()
    return enabled_providers
