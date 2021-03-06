subarch: i686
version_stamp: taz-v1.0-beta1
target: livecd-stage1
rel_type: default
profile: default/linux/x86/17.0/musl
snapshot: taz-v1.0-beta1
portage_confdir: /etc/catalyst/portage

# seed stage is from http://distfiles.gentoo.org/experimental/x86/musl/
source_subpath: default/stage3-i686-musl-vanilla

# overlays currently in use:
# * musl      (https://anongit.gentoo.org/git/proj/musl.git)
portage_overlay: /var/lib/layman

# useflags that get applied on top of profile useflags
livecd/use: 
    -calendar 
    cdda 
    cups 
    curl 
    dbus 
    -debug 
    exif 
    flac 
    -gnome 
    -gnome-keyring 
    gnutls 
    gtk
    -gtk3 
    jpeg
    jpeg2k
    -kde
    musl
    -nls
    ogg
    opengl
    perl
    -policykit
    -pulseaudio
    python
    -qt4
    -qt5
    -spell
    -sqlite
    svg
    -systemd
    vorbis
    X
    zeroconf

# packages that will get included on the CD
livecd/packages: 
    app-admin/conky
    app-admin/hardinfo
    app-admin/sudo
    app-antivirus/clamav
    app-arch/lz4
    app-arch/par2cmdline
    app-arch/xarchiver
    app-cdr/xfburn
    app-misc/livecd-tools
    app-misc/pwsafe
    app-editors/leafpad
    app-editors/nano
    app-office/abiword
    app-office/gnumeric
    app-office/impressive
    app-portage/porthole
    dev-python/httplib2
    dev-python/pip
    dev-python/requests
    dev-python/requests-oauthlib
    app-text/tesseract
    dev-util/geany
    dev-vcs/git
    lxde-base/lxappearance
    lxde-base/lxinput
    lxde-base/lxpanel
    lxde-base/lxrandr
    lxde-base/lxsession
    lxde-base/lxtask
    mail-client/claws-mail
    media-gfx/feh
    media-gfx/gimp
    media-gfx/gpicview
    media-gfx/inkscape
    media-gfx/sane-backends
    media-sound/alsaplayer
    media-sound/mps-youtube
    media-video/mpv
    net-im/gajim
    net-misc/curl
    net-misc/dhcpcd
    net-misc/dhcpcd-ui
    net-misc/ntp
    net-misc/wicd
    net-print/cups
    net-voip/yate
    net-wireless/bluez
    net-wireless/wireless-tools
    sci-calculators/galculator
    sys-apps/busybox
    sys-apps/man-pages
    sys-apps/net-tools
    sys-apps/openrc
    sys-apps/portage
    sys-apps/util-linux
    sys-block/gparted
    sys-boot/syslinux
    sys-devel/bc
    sys-fs/squashfs-tools
    www-client/palemoon
    www-plugins/lightspark
    x11-apps/mesa-progs
    x11-apps/setxkbmap
    x11-apps/xwd
    x11-base/xorg-server
    x11-libs/libva-vdpau-driver
    x11-drivers/xf86-video-intel
    x11-drivers/xf86-video-vesa
    x11-misc/gmrun
    x11-misc/pcmanfm
    x11-misc/slock
    x11-misc/xprintidle
    x11-terms/sakura
    x11-wm/openbox
