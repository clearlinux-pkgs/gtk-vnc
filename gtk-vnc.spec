#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : gtk-vnc
Version  : 0.7.0
Release  : 1
URL      : http://ftp.gnome.org/pub/gnome/sources/gtk-vnc/0.7/gtk-vnc-0.7.0.tar.xz
Source0  : http://ftp.gnome.org/pub/gnome/sources/gtk-vnc/0.7/gtk-vnc-0.7.0.tar.xz
Summary  : A GTK2 widget for VNC clients
Group    : Development/Tools
License  : LGPL-2.1 LGPL-2.1+
Requires: gtk-vnc-bin
Requires: gtk-vnc-data
Requires: gtk-vnc-lib
Requires: gtk-vnc-locales
Requires: gtk-vnc-doc
BuildRequires : gettext
BuildRequires : gobject-introspection-dev
BuildRequires : intltool
BuildRequires : libgcrypt-dev
BuildRequires : libgpg-error-dev
BuildRequires : perl(XML::Parser)
BuildRequires : pkgconfig(cairo)
BuildRequires : pkgconfig(gdk-pixbuf-2.0)
BuildRequires : pkgconfig(gio-2.0)
BuildRequires : pkgconfig(gio-unix-2.0)
BuildRequires : pkgconfig(gnutls)
BuildRequires : pkgconfig(gobject-2.0)
BuildRequires : pkgconfig(gthread-2.0)
BuildRequires : pkgconfig(gtk+-3.0)
BuildRequires : pkgconfig(x11)

%description
gtk-vnc is a VNC viewer widget for GTK2. It is built using coroutines
allowing it to be completely asynchronous while remaining single threaded.

%package bin
Summary: bin components for the gtk-vnc package.
Group: Binaries
Requires: gtk-vnc-data

%description bin
bin components for the gtk-vnc package.


%package data
Summary: data components for the gtk-vnc package.
Group: Data

%description data
data components for the gtk-vnc package.


%package dev
Summary: dev components for the gtk-vnc package.
Group: Development
Requires: gtk-vnc-lib
Requires: gtk-vnc-bin
Requires: gtk-vnc-data
Provides: gtk-vnc-devel

%description dev
dev components for the gtk-vnc package.


%package doc
Summary: doc components for the gtk-vnc package.
Group: Documentation

%description doc
doc components for the gtk-vnc package.


%package lib
Summary: lib components for the gtk-vnc package.
Group: Libraries
Requires: gtk-vnc-data

%description lib
lib components for the gtk-vnc package.


%package locales
Summary: locales components for the gtk-vnc package.
Group: Default

%description locales
locales components for the gtk-vnc package.


%prep
%setup -q -n gtk-vnc-0.7.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1493913327
%configure --disable-static --with-gtk=3.0 --without-sasl --disable-vala
make V=1  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1493913327
rm -rf %{buildroot}
%make_install
%find_lang gtk-vnc

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/gvnccapture

%files data
%defattr(-,root,root,-)
/usr/lib64/girepository-1.0/GVnc-1.0.typelib
/usr/lib64/girepository-1.0/GtkVnc-2.0.typelib
/usr/share/gir-1.0/*.gir

%files dev
%defattr(-,root,root,-)
/usr/include/gtk-vnc-2.0/gtk-vnc.h
/usr/include/gtk-vnc-2.0/vncdisplay.h
/usr/include/gtk-vnc-2.0/vncdisplayenums.h
/usr/include/gtk-vnc-2.0/vncgrabsequence.h
/usr/include/gtk-vnc-2.0/vncimageframebuffer.h
/usr/include/gvnc-1.0/gvnc.h
/usr/include/gvnc-1.0/vncaudio.h
/usr/include/gvnc-1.0/vncaudioformat.h
/usr/include/gvnc-1.0/vncaudiosample.h
/usr/include/gvnc-1.0/vncbaseaudio.h
/usr/include/gvnc-1.0/vncbaseframebuffer.h
/usr/include/gvnc-1.0/vnccolormap.h
/usr/include/gvnc-1.0/vncconnection.h
/usr/include/gvnc-1.0/vncconnectionenums.h
/usr/include/gvnc-1.0/vnccursor.h
/usr/include/gvnc-1.0/vncframebuffer.h
/usr/include/gvnc-1.0/vncpixelformat.h
/usr/include/gvnc-1.0/vncutil.h
/usr/lib64/libgtk-vnc-2.0.so
/usr/lib64/libgvnc-1.0.so
/usr/lib64/pkgconfig/gtk-vnc-2.0.pc
/usr/lib64/pkgconfig/gvnc-1.0.pc

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man1/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/libgtk-vnc-2.0.so.0
/usr/lib64/libgtk-vnc-2.0.so.0.0.2
/usr/lib64/libgvnc-1.0.so.0
/usr/lib64/libgvnc-1.0.so.0.0.1

%files locales -f gtk-vnc.lang
%defattr(-,root,root,-)
