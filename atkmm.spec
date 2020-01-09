%global apiver 1.6
# first two digits of version
%define release_version %(echo %{version} | awk -F. '{print $1"."$2}')

Name:           atkmm
Version:        2.22.7
Release:        3%{?dist}
Summary:        C++ interface for the ATK library

Group:          System Environment/Libraries
License:        LGPLv2+
URL:            http://www.gtkmm.org/
Source0:        http://ftp.gnome.org/pub/GNOME/sources/atkmm/%{release_version}/atkmm-%{version}.tar.xz

BuildRequires:  atk-devel
BuildRequires:  glibmm24-devel

# atkmm was split out into a separate package in gtkmm24 2.21.1
Conflicts:      gtkmm24 < 2.21.1

%description
atkmm provides a C++ interface for the ATK library. Highlights
include typesafe callbacks, widgets extensible via inheritance and a
comprehensive set of widget classes that can be freely combined to
quickly create complex user interfaces.


%package devel
Summary:        Development files for %{name}
Group:          Development/Libraries
Requires:       %{name} = %{version}-%{release}
Conflicts:      gtkmm24-devel < 2.21.1

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%package        doc
Summary:        Developer's documentation for the atkmm library
Group:          Documentation
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}
Requires:       glibmm24-doc

%description    doc
This package contains developer's documentation for the atkmm
library. Atkmm is the C++ API for the ATK accessibility toolkit library.

The documentation can be viewed either through the devhelp
documentation browser or through a web browser.


%prep
%setup -q


%build
%configure --disable-static
make %{?_smp_mflags}


%install
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'


%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files
%doc AUTHORS ChangeLog COPYING NEWS README
%{_libdir}/*.so.*

%files devel
%{_includedir}/atkmm-%{apiver}/
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_libdir}/atkmm-%{apiver}/

%files doc
%doc %{_docdir}/atkmm-%{apiver}/
%doc %{_datadir}/devhelp/


%changelog
* Fri Jan 24 2014 Daniel Mach <dmach@redhat.com> - 2.22.7-3
- Mass rebuild 2014-01-24

* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 2.22.7-2
- Mass rebuild 2013-12-27

* Mon Apr 29 2013 Kalev Lember <kalevlember@gmail.com> - 2.22.7-1
- Update to 2.22.7
- Drop -devel package deps that rpmbuild takes care of automatically

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.22.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.22.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Feb 27 2012 Kalev Lember <kalevlember@gmail.com> - 2.22.6-1
- Update to 2.22.6
- Switch to .xz tarballs

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.22.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Mar 31 2011 Kalev Lember <kalev@smartlink.ee> - 2.22.5-1
- Update to 2.22.5

* Fri Mar 25 2011 Kalev Lember <kalev@smartlink.ee> - 2.22.4-1
- Update to 2.22.4

* Tue Mar 01 2011 Kalev Lember <kalev@smartlink.ee> - 2.22.2-4
- Spec cleanup
- Actually co-own /usr/share/devhelp/ directory
- Require base package from -doc subpackage

* Mon Feb 21 2011 Haïkel Guémar <hguemar@fedoraproject.org> - 2.22.2-3
- split doc into subpackage
- fix documentation location
- co-own /usr/share/devhelp

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.22.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Jan 13 2011 Kalev Lember <kalev@smartlink.ee> - 2.22.2-1
- Update to 2.22.2

* Tue Sep 28 2010 Kalev Lember <kalev@smartlink.ee> - 2.22.0-1
- Update to 2.22.0

* Tue Sep 14 2010 Kalev Lember <kalev@smartlink.ee> - 2.21.2-2
- Co-own /usr/share/gtk-doc/ directory (#604169)

* Wed Jun 30 2010 Kalev Lember <kalev@smartlink.ee> - 2.21.2-1
- Update to 2.21.2

* Sat Jun 26 2010 Kalev Lember <kalev@smartlink.ee> - 2.21.1-2
- added missing Conflicts: gtkmm24-devel to -devel subpackage
- calculate two-digit download directory from three-digit package version

* Wed Jun 23 2010 Kalev Lember <kalev@smartlink.ee> - 2.21.1-1
- Initial RPM release
