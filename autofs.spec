#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : autofs
Version  : 5.1.2
Release  : 5
URL      : https://www.kernel.org/pub/linux/daemons/autofs/v5/autofs-5.1.2.tar.xz
Source0  : https://www.kernel.org/pub/linux/daemons/autofs/v5/autofs-5.1.2.tar.xz
Summary  : A tool from automatically mounting and umounting filesystems.
Group    : Development/Tools
License  : GPL-2.0
Requires: autofs-bin
Requires: autofs-config
Requires: autofs-lib
Requires: autofs-doc
BuildRequires : bison
BuildRequires : flex
BuildRequires : kmod
BuildRequires : krb5-dev
BuildRequires : libxml2-dev

%description
autofs is a daemon which automatically mounts filesystems when you use
them, and unmounts them later when you are not using them.  This can
include network filesystems, CD-ROMs, floppies, and so forth.

%package bin
Summary: bin components for the autofs package.
Group: Binaries
Requires: autofs-config

%description bin
bin components for the autofs package.


%package config
Summary: config components for the autofs package.
Group: Default

%description config
config components for the autofs package.


%package doc
Summary: doc components for the autofs package.
Group: Documentation

%description doc
doc components for the autofs package.


%package lib
Summary: lib components for the autofs package.
Group: Libraries
Requires: autofs-config

%description lib
lib components for the autofs package.


%prep
%setup -q -n autofs-5.1.2

%build
export CFLAGS="$CFLAGS -ffunction-sections -Os "
export FCFLAGS="$CFLAGS -ffunction-sections -Os "
export FFLAGS="$CFLAGS -ffunction-sections -Os "
export CXXFLAGS="$CXXFLAGS -ffunction-sections -Os "
%configure --disable-static --with-systemd
make V=1  %{?_smp_mflags}

%install
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)
/autofs

%files bin
%defattr(-,root,root,-)
/usr/bin/automount

%files config
%defattr(-,root,root,-)
/usr/lib/systemd/system/autofs.service

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man5/*
%doc /usr/share/man/man8/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/autofs/lookup_dir.so
/usr/lib64/autofs/lookup_file.so
/usr/lib64/autofs/lookup_files.so
/usr/lib64/autofs/lookup_hosts.so
/usr/lib64/autofs/lookup_multi.so
/usr/lib64/autofs/lookup_nis.so
/usr/lib64/autofs/lookup_nisplus.so
/usr/lib64/autofs/lookup_program.so
/usr/lib64/autofs/lookup_userhome.so
/usr/lib64/autofs/lookup_yp.so
/usr/lib64/autofs/mount_afs.so
/usr/lib64/autofs/mount_autofs.so
/usr/lib64/autofs/mount_bind.so
/usr/lib64/autofs/mount_changer.so
/usr/lib64/autofs/mount_generic.so
/usr/lib64/autofs/mount_nfs.so
/usr/lib64/autofs/mount_nfs4.so
/usr/lib64/autofs/parse_amd.so
/usr/lib64/autofs/parse_sun.so
