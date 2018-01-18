Name:        libkf5archive
Version:     5.41.0
Release:     1
Summary:     KDE Frameworks 5 Tier 1 addon with archive functions
License:     LGPLv2+ and BSD
URL:         https://cgit.kde.org/karchive.git
Source0:     %{name}-%{version}.tar.gz

# Upstreamable patches
Patch1: 0001-Generate-pkg-config.patch
Patch2: 0002-Keep-Qt5.6-requirement.patch
Patch3: 0003-Add-an-option-to-automatically-rename-target-file-pa.patch

BuildRequires: cmake
BuildRequires: extra-cmake-modules
BuildRequires: pkgconfig(Qt5Core) >= 5.6.0
BuildRequires: pkgconfig(Qt5Test)
BuildRequires: pkgconfig(Qt5Network)
BuildRequires: bzip2-devel
BuildRequires: xz-devel

Requires: qt5-qtcore

%description
KDE Frameworks 5 Tier 1 addon with archive functions.

KArchive provides classes for easy reading, creation and manipulation
of "archive" formats like ZIP and TAR.

This package is part of KDE Frameworks 5.

%package devel
Summary: Development files for %{name}
Requires: %{name} = %{version}-%{release}

%description devel
%summary.

%prep
%setup -n %{name}-%{version}/karchive

%patch1 -p1 -b .generate-pkgconfg
%patch2 -p1 -b .keep-qt5.6-build-req
%patch3 -p1 -b .auto-rename

%build
cmake . -DCMAKE_INSTALL_PREFIX=/usr
%{__make} %{?_smp_mflags}

%install
%{make_install}

%define pkg_config_dir %{buildroot}/usr/lib/pkgconfig/

mkdir -p %{pkg_config_dir}
cp -p KF5Archive.pc %{pkg_config_dir}

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%doc COPYING COPYING.LIB
%{_sysconfdir}/xdg/karchive.*
%{_libdir}/libKF5Archive.so.*

%files devel
%doc COPYING.LIB AUTHORS README.md
%{_includedir}/KF5/karchive_version.h
%{_includedir}/KF5/KArchive/
%{_libdir}/libKF5Archive.so
%{_libdir}/cmake/KF5Archive/
%{_libdir}/pkgconfig/KF5Archive.pc
%{_datadir}/qt5/mkspecs/modules/qt_KArchive.pri
