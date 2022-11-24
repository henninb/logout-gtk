#!/bin/sh

sudo pacman --noconfirm --needed -S gobject-introspection
mkdir -p src
# stack run

echo stack build gi-harfbuzz
stack build
stack install

exit 0
