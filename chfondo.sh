#!/usr/bin/env bash

if [[ $XDG_CURRENT_DESKTOP == "i3" ]]; then
	export DISPLAY=:1.0
	feh --randomize --bg-scale ~/Imágenes/Wallpapers/
fi

if [[ $XDG_CURRENT_DESKTOP == "GNOME" ]]; then
	export DISPLAY=:1.0
	img="file:///home/rutolo/Imágenes/Wallpapers/"$(ls /home/rutolo/Imágenes/Wallpapers | sort -R | head -n1)
	echo $img
	gsettings set org.gnome.desktop.background picture-uri $img
	gsettings set org.gnome.desktop.screensaver picture-uri $img
fi
