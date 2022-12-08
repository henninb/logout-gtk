#!/bin/sh

sudo pacman --noconfirm --needed -S gobject-introspection
sudo dnf install -y gobject-introspection-devel
sudo dnf install -y cairo-gobject-devel
mkdir -p src
# stack run

echo stack build gi-harfbuzz
stack build
stack install

exit 0
