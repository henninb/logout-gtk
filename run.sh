#!/bin/sh

sudo pacman --noconfirm --needed -S gobject-introspection
sudo dnf install -y gobject-introspection-devel
mkdir -p src
# stack run

echo stack build gi-harfbuzz
stack build
stack install

exit 0
