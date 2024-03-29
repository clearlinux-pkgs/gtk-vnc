#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: meson
# autospec version: v3
# autospec commit: c1050fe
#
Name     : gtk-vnc
Version  : 1.3.1
Release  : 34
URL      : https://download.gnome.org/sources/gtk-vnc/1.3/gtk-vnc-1.3.1.tar.xz
Source0  : https://download.gnome.org/sources/gtk-vnc/1.3/gtk-vnc-1.3.1.tar.xz
Summary  : A GTK widget for VNC clients
Group    : Development/Tools
License  : BSD-3-Clause GPL-2.0 LGPL-2.0+ LGPL-2.1
Requires: gtk-vnc-bin = %{version}-%{release}
Requires: gtk-vnc-data = %{version}-%{release}
Requires: gtk-vnc-lib = %{version}-%{release}
Requires: gtk-vnc-license = %{version}-%{release}
Requires: gtk-vnc-locales = %{version}-%{release}
Requires: gtk-vnc-man = %{version}-%{release}
BuildRequires : buildreq-gnome
BuildRequires : buildreq-meson
BuildRequires : gnutls-dev
BuildRequires : libgcrypt-dev
BuildRequires : libgpg-error-dev
BuildRequires : libgpg-error-extras
BuildRequires : pkgconfig(gnutls)
BuildRequires : pkgconfig(gpg-error)
BuildRequires : pkgconfig(gtk+-3.0)
BuildRequires : pkgconfig(libpulse-simple)
BuildRequires : pkgconfig(libsasl2)
BuildRequires : vala-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
gtk-vnc is a VNC viewer widget for GTK. It is built using coroutines
allowing it to be completely asynchronous while remaining single threaded.

%package bin
Summary: bin components for the gtk-vnc package.
Group: Binaries
Requires: gtk-vnc-data = %{version}-%{release}
Requires: gtk-vnc-license = %{version}-%{release}

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
Requires: gtk-vnc-lib = %{version}-%{release}
Requires: gtk-vnc-bin = %{version}-%{release}
Requires: gtk-vnc-data = %{version}-%{release}
Provides: gtk-vnc-devel = %{version}-%{release}
Requires: gtk-vnc = %{version}-%{release}

%description dev
dev components for the gtk-vnc package.


%package lib
Summary: lib components for the gtk-vnc package.
Group: Libraries
Requires: gtk-vnc-data = %{version}-%{release}
Requires: gtk-vnc-license = %{version}-%{release}

%description lib
lib components for the gtk-vnc package.


%package license
Summary: license components for the gtk-vnc package.
Group: Default

%description license
license components for the gtk-vnc package.


%package locales
Summary: locales components for the gtk-vnc package.
Group: Default

%description locales
locales components for the gtk-vnc package.


%package man
Summary: man components for the gtk-vnc package.
Group: Default

%description man
man components for the gtk-vnc package.


%prep
%setup -q -n gtk-vnc-1.3.1
cd %{_builddir}/gtk-vnc-1.3.1
pushd ..
cp -a gtk-vnc-1.3.1 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1701967259
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
meson --libdir=lib64 --prefix=/usr --buildtype=plain   builddir
ninja -v -C builddir
CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 -O3" CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 " LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3" meson --libdir=lib64 --prefix=/usr --buildtype=plain   builddiravx2
ninja -v -C builddiravx2

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
meson test -C builddir --print-errorlogs

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
mkdir -p %{buildroot}/usr/share/package-licenses/gtk-vnc
cp %{_builddir}/gtk-vnc-%{version}/COPYING.LIB %{buildroot}/usr/share/package-licenses/gtk-vnc/81221edbef5521188d99b7c699d326e85b8c3e87 || :
cp %{_builddir}/gtk-vnc-%{version}/subprojects/keycodemapdb/LICENSE.BSD %{buildroot}/usr/share/package-licenses/gtk-vnc/ea5b412c09f3b29ba1d81a61b878c5c16ffe69d8 || :
cp %{_builddir}/gtk-vnc-%{version}/subprojects/keycodemapdb/LICENSE.GPL2 %{buildroot}/usr/share/package-licenses/gtk-vnc/06877624ea5c77efe3b7e39b0f909eda6e25a4ec || :
DESTDIR=%{buildroot}-v3 ninja -C builddiravx2 install
DESTDIR=%{buildroot} ninja -C builddir install
%find_lang gtk-vnc
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/V3/usr/bin/gvnccapture
/usr/bin/gvnccapture

%files data
%defattr(-,root,root,-)
/usr/lib64/girepository-1.0/GVnc-1.0.typelib
/usr/lib64/girepository-1.0/GVncPulse-1.0.typelib
/usr/lib64/girepository-1.0/GtkVnc-2.0.typelib
/usr/share/gir-1.0/*.gir
/usr/share/vala/vapi/gtk-vnc-2.0.deps
/usr/share/vala/vapi/gtk-vnc-2.0.vapi
/usr/share/vala/vapi/gvnc-1.0.deps
/usr/share/vala/vapi/gvnc-1.0.vapi
/usr/share/vala/vapi/gvncpulse-1.0.deps
/usr/share/vala/vapi/gvncpulse-1.0.vapi

%files dev
%defattr(-,root,root,-)
/usr/include/gtk-vnc-2.0/gtk-vnc.h
/usr/include/gtk-vnc-2.0/vnccairoframebuffer.h
/usr/include/gtk-vnc-2.0/vncdisplay.h
/usr/include/gtk-vnc-2.0/vncdisplayenums.h
/usr/include/gtk-vnc-2.0/vncgrabsequence.h
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
/usr/include/gvnc-1.0/vncversion.h
/usr/include/gvncpulse-1.0/gvncpulse.h
/usr/include/gvncpulse-1.0/vncaudiopulse.h
/usr/lib64/libgtk-vnc-2.0.so
/usr/lib64/libgvnc-1.0.so
/usr/lib64/libgvncpulse-1.0.so
/usr/lib64/pkgconfig/gtk-vnc-2.0.pc
/usr/lib64/pkgconfig/gvnc-1.0.pc
/usr/lib64/pkgconfig/gvncpulse-1.0.pc

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/libgtk-vnc-2.0.so.0.0.2
/V3/usr/lib64/libgvnc-1.0.so.0.0.1
/V3/usr/lib64/libgvncpulse-1.0.so.0.0.1
/usr/lib64/libgtk-vnc-2.0.so.0
/usr/lib64/libgtk-vnc-2.0.so.0.0.2
/usr/lib64/libgvnc-1.0.so.0
/usr/lib64/libgvnc-1.0.so.0.0.1
/usr/lib64/libgvncpulse-1.0.so.0
/usr/lib64/libgvncpulse-1.0.so.0.0.1

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/gtk-vnc/06877624ea5c77efe3b7e39b0f909eda6e25a4ec
/usr/share/package-licenses/gtk-vnc/81221edbef5521188d99b7c699d326e85b8c3e87
/usr/share/package-licenses/gtk-vnc/ea5b412c09f3b29ba1d81a61b878c5c16ffe69d8

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/gvnccapture.1

%files locales -f gtk-vnc.lang
%defattr(-,root,root,-)

