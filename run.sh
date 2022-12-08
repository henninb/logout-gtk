#!/bin/sh

sudo pacman --noconfirm --needed -S gobject-introspection
sudo dnf install -y gobject-introspection-devel
sudo dnf install -y cairo-gobject-devel
sudo dnf install -y atk-devel
sudo dnf install -y gdk-pixbuf2-devel
sudo dnf install -y pango-devel
sudo dnf install -y gtk3-devel
mkdir -p src
# stack run

echo stack build gi-harfbuzz
stack build
stack install

exit 0
