#!/bin/sh

sudo pacman --noconfirm --needed -S gobject-introspection
sudo dnf install -y gobject-introspection-devel
sudo dnf install -y cairo-gobject-devel

echo atk-devel
echo gdk-pixbuf2-devel
echo sudo dnf install pango-devel
echo gtk3-devel
mkdir -p src
# stack run

echo stack build gi-harfbuzz
stack build
stack install

exit 0
