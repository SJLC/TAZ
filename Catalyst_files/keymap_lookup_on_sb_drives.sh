#!/bin/bash
# Place this file in /etc/local.d (see https://wiki.gentoo.org/wiki//etc/local.d )
# This file tells the system to look for (and execute) the keymap.sh file in the folder /bootscripts/ on any USB device
# (in practice, only USB sticks should be used). Automounting is available (due to AutoFS), so any connected USB sticks will
# automatically be searched for the indicated file/folder.
./*/bootscripts/keymap.sh
