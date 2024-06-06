"""Not a real Plugin - provides some core features and some caching of commonly requested structures."""

from ..common import state
from ..types import VersionInfo
from .interface import Plugin

DEFAULT_VERSION = VersionInfo(9, 9, 9)


class Extension(Plugin):
    """Internal built-in plugin allowing caching states and implementing special commands."""

    requires = ["hyprland"]

    def set_commands(self, **cmd_map) -> None:
        """Set some commands, made available as run_`name` methods."""
        for name, fn in cmd_map.items():
            setattr(self, f"run_{name}", fn)

    async def on_reload(self) -> None:
        """Reload the plugin."""
        state.variables = self.config.get("variables", {})
