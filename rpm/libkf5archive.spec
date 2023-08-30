Name:        libkf5archive
Version:     5.57.0
Release:     1
Summary:     KDE Frameworks 5 Tier 1 addon with archive functions
License:     LGPLv2+ and BSD
URL:         https://cgit.kde.org/karchive.git
Source0:     %{name}-%{version}.tar.gz

# Upstreamable patches
Patch1: 0001-Generate-pkg-config.patch
Patch2: 0002-Keep-Qt5.6-requirement.patch
Patch3: 0003-Add-an-option-to-automatically-rename-target-file-pa.patch
Patch4: 0004-Revert-Port-away-from-deprecated-methods-in-Qt-5.14.patch
Patch5: 0005-Revert-Port-to-QRandomGenerator-qrand-was-deprecated.patch
Patch6: 0006-Revert-Make-it-compiles-without-foreach.patch
Patch7: 0007-Revert-Test-reading-and-seeking-in-KCompressionDevic.patch

BuildRequires: cmake
BuildRequires: extra-cmake-modules
BuildRequires: pkgconfig(Qt5Core) >= 5.6.0
BuildRequires: pkgconfig(Qt5Test)
BuildRequires: pkgconfig(Qt5Network)
BuildRequires: bzip2-devel
BuildRequires: xz-devel
#FIXME?
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
%{summary}.

%package doc
Summary:   Documentation for %{name}
Requires:  %{name} = %{version}-%{release}

%description doc
%{summary}.

%prep
%autosetup -p1 -n %{name}-%{version}/karchive

%build
%cmake
%make_build

%install
%make_install

%define pkg_config_dir %{buildroot}%{_libdir}/pkgconfig/

mkdir -p %{pkg_config_dir}
cp -p KF5Archive.pc %{pkg_config_dir}

mkdir -p %{buildroot}%{_docdir}/%{name}-%{version}
install -m0644 -t %{buildroot}%{_docdir}/%{name}-%{version} \
        AUTHORS README.md

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%license LICENSES/*.txt
%{_datadir}/qlogging-categories5/*categories
%{_libdir}/libKF5Archive.so.*

%files devel
%{_includedir}/KF5/karchive_version.h
%{_includedir}/KF5/KArchive/
%{_qt5_libdir}/libKF5Archive.so
%{_qt5_libdir}/cmake/KF5Archive/
%{_qt5_libdir}/pkgconfig/KF5Archive.pc
%{_qt5_archdatadir}/mkspecs/modules/qt_KArchive.pri

%files doc
%defattr(-,root,root,-)
%{_docdir}/%{name}-%{version}
