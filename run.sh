#!/bin/sh

if command -v pacman; then
  sudo pacman --noconfirm --needed -S gobject-introspection
elif command -v apt; then
  sudo apt install -y gobject-introspection
  sudo apt install -y libatk1.0-dev
  sudo apt install -y libpango1.0-dev
  sudo apt install -y libgdk-pixbuf-2.0-dev
  sudo apt install -y libgirepository1.0-dev
elif command -v dnf; then
  sudo dnf install -y gobject-introspection-devel
  sudo dnf install -y cairo-gobject-devel
  sudo dnf install -y atk-devel
  sudo dnf install -y gdk-pixbuf2-devel
  sudo dnf install -y pango-devel
  sudo dnf install -y gtk3-devel
elif command -v xbps-install; then
  sudo xbps-install -y gobject-introspection
else
  echo "$OS is not yet implemented."
  exit 1
fi

mkdir -p src
# stack run

echo stack build gi-harfbuzz
stack build
stack install

exit 0
