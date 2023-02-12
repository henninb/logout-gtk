#!/bin/sh

if command -v pacman; then
  sudo pacman --noconfirm --needed -S gobject-introspection
fi

if command -v dnf; then
  sudo dnf install -y gobject-introspection-devel
  sudo dnf install -y cairo-gobject-devel
  sudo dnf install -y atk-devel
  sudo dnf install -y gdk-pixbuf2-devel
  sudo dnf install -y pango-devel
  sudo dnf install -y gtk3-devel
fi

sudo xbps-install -y gobject-introspection

mkdir -p src
# stack run

echo stack build gi-harfbuzz
stack build
stack install

exit 0
