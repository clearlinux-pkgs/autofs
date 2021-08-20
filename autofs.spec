#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : autofs
Version  : 5.1.7
Release  : 26
URL      : https://mirrors.kernel.org/pub/linux/daemons/autofs/v5/autofs-5.1.7.tar.xz
Source0  : https://mirrors.kernel.org/pub/linux/daemons/autofs/v5/autofs-5.1.7.tar.xz
Summary  : A tool from automatically mounting and umounting filesystems.
Group    : Development/Tools
License  : GPL-2.0
Requires: autofs-bin = %{version}-%{release}
Requires: autofs-lib = %{version}-%{release}
Requires: autofs-license = %{version}-%{release}
Requires: autofs-man = %{version}-%{release}
BuildRequires : bison
BuildRequires : e2fsprogs-dev
BuildRequires : flex
BuildRequires : kmod
BuildRequires : krb5-dev
BuildRequires : libxml2-dev
BuildRequires : openldap-dev
BuildRequires : pkgconfig(libnsl)
BuildRequires : pkgconfig(libsystemd)
BuildRequires : pkgconfig(libtirpc)
BuildRequires : pkgconfig(libxml-2.0)
BuildRequires : sssd-dev
Patch1: 0001-Only-create-yp-library-if-enabled.patch
Patch2: 0002-nsswitch.conf-search-in-usr-share-defaults-etc-nsswi.patch

%description
autofs is a daemon which automatically mounts filesystems when you use
them, and unmounts them later when you are not using them.  This can
include network filesystems, CD-ROMs, floppies, and so forth.

%package bin
Summary: bin components for the autofs package.
Group: Binaries
Requires: autofs-license = %{version}-%{release}

%description bin
bin components for the autofs package.


%package dev
Summary: dev components for the autofs package.
Group: Development
Requires: autofs-lib = %{version}-%{release}
Requires: autofs-bin = %{version}-%{release}
Provides: autofs-devel = %{version}-%{release}
Requires: autofs = %{version}-%{release}

%description dev
dev components for the autofs package.


%package lib
Summary: lib components for the autofs package.
Group: Libraries
Requires: autofs-license = %{version}-%{release}

%description lib
lib components for the autofs package.


%package license
Summary: license components for the autofs package.
Group: Default

%description license
license components for the autofs package.


%package man
Summary: man components for the autofs package.
Group: Default

%description man
man components for the autofs package.


%prep
%setup -q -n autofs-5.1.7
cd %{_builddir}/autofs-5.1.7
%patch1 -p1
%patch2 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1620765283
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%configure --disable-static --with-systemd \
--with-libtirpc
make  %{?_smp_mflags}

%install
export SOURCE_DATE_EPOCH=1620765283
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/autofs
cp %{_builddir}/autofs-5.1.7/COPYING %{buildroot}/usr/share/package-licenses/autofs/76bc12364899ccee70781b6bbcbb4a9ebe07da2d
cp %{_builddir}/autofs-5.1.7/COPYRIGHT %{buildroot}/usr/share/package-licenses/autofs/bae2eff587b39294edb2c7a790e8c1a0d00ad089
%make_install
## Remove excluded files
rm -f %{buildroot}/autofs
## install_append content
# No sysconfig
rm -f %{buildroot}autofs
## install_append end

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/automount

%files dev
%defattr(-,root,root,-)
/usr/lib64/libautofs.so

%files lib
%defattr(-,root,root,-)
/usr/lib64/autofs/lookup_dir.so
/usr/lib64/autofs/lookup_file.so
/usr/lib64/autofs/lookup_files.so
/usr/lib64/autofs/lookup_hosts.so
/usr/lib64/autofs/lookup_ldap.so
/usr/lib64/autofs/lookup_ldaps.so
/usr/lib64/autofs/lookup_multi.so
/usr/lib64/autofs/lookup_nis.so
/usr/lib64/autofs/lookup_nisplus.so
/usr/lib64/autofs/lookup_program.so
/usr/lib64/autofs/lookup_sss.so
/usr/lib64/autofs/lookup_userhome.so
/usr/lib64/autofs/lookup_yp.so
/usr/lib64/autofs/mount_afs.so
/usr/lib64/autofs/mount_autofs.so
/usr/lib64/autofs/mount_bind.so
/usr/lib64/autofs/mount_changer.so
/usr/lib64/autofs/mount_ext2.so
/usr/lib64/autofs/mount_ext3.so
/usr/lib64/autofs/mount_ext4.so
/usr/lib64/autofs/mount_generic.so
/usr/lib64/autofs/mount_nfs.so
/usr/lib64/autofs/mount_nfs4.so
/usr/lib64/autofs/parse_amd.so
/usr/lib64/autofs/parse_sun.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/autofs/76bc12364899ccee70781b6bbcbb4a9ebe07da2d
/usr/share/package-licenses/autofs/bae2eff587b39294edb2c7a790e8c1a0d00ad089

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man5/auto.master.5
/usr/share/man/man5/autofs.5
/usr/share/man/man5/autofs.conf.5
/usr/share/man/man5/autofs_ldap_auth.conf.5
/usr/share/man/man8/autofs.8
/usr/share/man/man8/automount.8
