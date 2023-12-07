#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: configure
# autospec version: v3
# autospec commit: c1050fe
#
Name     : autofs
Version  : 5.1.9
Release  : 34
URL      : https://mirrors.kernel.org/pub/linux/daemons/autofs/v5/autofs-5.1.9.tar.xz
Source0  : https://mirrors.kernel.org/pub/linux/daemons/autofs/v5/autofs-5.1.9.tar.xz
Summary  : A tool from automatically mounting and umounting filesystems.
Group    : Development/Tools
License  : GPL-2.0
Requires: autofs-bin = %{version}-%{release}
Requires: autofs-lib = %{version}-%{release}
Requires: autofs-license = %{version}-%{release}
Requires: autofs-man = %{version}-%{release}
BuildRequires : bison
BuildRequires : buildreq-configure
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
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}
Patch1: 0001-nsswitch.conf-search-in-usr-share-defaults-etc-nsswi.patch

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
%setup -q -n autofs-5.1.9
cd %{_builddir}/autofs-5.1.9
%patch -P 1 -p1
pushd ..
cp -a autofs-5.1.9 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1701935228
export GCC_IGNORE_WERROR=1
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
%configure --disable-static --with-systemd \
--with-libtirpc
make  %{?_smp_mflags}

unset PKG_CONFIG_PATH
pushd ../buildavx2/
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -m64 -march=x86-64-v3 "
LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
%configure --disable-static --with-systemd \
--with-libtirpc
make  %{?_smp_mflags}
popd
%install
export GCC_IGNORE_WERROR=1
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1701935228
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/autofs
cp %{_builddir}/autofs-%{version}/COPYING %{buildroot}/usr/share/package-licenses/autofs/76bc12364899ccee70781b6bbcbb4a9ebe07da2d || :
cp %{_builddir}/autofs-%{version}/COPYRIGHT %{buildroot}/usr/share/package-licenses/autofs/bae2eff587b39294edb2c7a790e8c1a0d00ad089 || :
pushd ../buildavx2/
%make_install_v3
popd
%make_install
## Remove excluded files
rm -f %{buildroot}*/autofs
## install_append content
# No sysconfig
rm -f %{buildroot}autofs
## install_append end
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/V3/usr/bin/automount
/usr/bin/automount

%files dev
%defattr(-,root,root,-)
/V3/usr/lib64/libautofs.so
/usr/lib64/libautofs.so

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/autofs/lookup_dir.so
/V3/usr/lib64/autofs/lookup_file.so
/V3/usr/lib64/autofs/lookup_hosts.so
/V3/usr/lib64/autofs/lookup_ldap.so
/V3/usr/lib64/autofs/lookup_multi.so
/V3/usr/lib64/autofs/lookup_program.so
/V3/usr/lib64/autofs/lookup_sss.so
/V3/usr/lib64/autofs/lookup_userhome.so
/V3/usr/lib64/autofs/lookup_yp.so
/V3/usr/lib64/autofs/mount_afs.so
/V3/usr/lib64/autofs/mount_autofs.so
/V3/usr/lib64/autofs/mount_bind.so
/V3/usr/lib64/autofs/mount_changer.so
/V3/usr/lib64/autofs/mount_ext2.so
/V3/usr/lib64/autofs/mount_generic.so
/V3/usr/lib64/autofs/mount_nfs.so
/V3/usr/lib64/autofs/parse_amd.so
/V3/usr/lib64/autofs/parse_sun.so
/usr/lib64/autofs/lookup_dir.so
/usr/lib64/autofs/lookup_file.so
/usr/lib64/autofs/lookup_files.so
/usr/lib64/autofs/lookup_hosts.so
/usr/lib64/autofs/lookup_ldap.so
/usr/lib64/autofs/lookup_ldaps.so
/usr/lib64/autofs/lookup_multi.so
/usr/lib64/autofs/lookup_nis.so
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
