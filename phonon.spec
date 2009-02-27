%define		qtver		4.4.3
Summary:	Phonon library
Summary(pl.UTF-8):	Biblioteka Phonon
Name:		phonon
Version:	4.3.1
Release:	1
License:	LGPL v2.1
Group:		X11/Libraries
#Source0:	%{name}-%{version}-%{snap}.tar.bz2
#Source0:	ftp://ftp.kde.org/pub/kde/unstable/4.1.80/src/%{name}-%{version}.tar.bz2
Source0:	http://nomeno.pl/~shadzik/kde4/%{name}-%{version}.tar.bz2
# Source0-md5:	767cb68052c108e95f293f30acdef3fb
URL:		http://phonon.kde.org/
BuildRequires:	QtCore-devel >= %{qtver}
BuildRequires:	QtDBus-devel >= %{qtver}
BuildRequires:	QtNetwork-devel >= %{qtver}
BuildRequires:	QtOpenGL-devel >= %{qtver}
BuildRequires:	QtSql-devel >= %{qtver}
BuildRequires:	QtTest-devel >= %{qtver}
BuildRequires:	automoc4 >= 0.9.86
BuildRequires:	cmake >= 2.6.2
BuildRequires:	gstreamer-plugins-base-devel >= 0.10.0
BuildRequires:	qt4-build >= %{qtver}
BuildRequires:	qt4-qmake >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.293
BuildRequires:	xine-lib-devel >= 2:1.1.15-4
Requires:	kde-common-dirs >= 0.4
Provides:	qt4-phonon
Obsoletes:	qt4-phonon
Obsoletes:	kde4-phonon-xine
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Phonon library.

%description -l pl.UTF-8
Biblioteka phonon.

%package devel
Summary:	Header files for Phonon library
Summary(pl.UTF-8):	Pliki nag≈√≥wkowe biblioteki Phonon
Group:		X11/Development/Libraries
Requires:	%{name} == %{version}-%{release}
Requires:	QtCore-devel >= %{qtver}
Requires:	QtDBus-devel >= %{qtver}
Requires:	QtGui-devel >= %{qtver}
Provides:	qt4-phonon-devel
Obsoletes:	qt4-phonon-devel

%description devel
Header files for Phonon library.

%description devel -l pl.UTF-8
Pliki nag≈√≥wkowe biblioteki Phonon.

%prep
%setup -q

%build
install -d build
cd build
%cmake \
	-DCMAKE_INSTALL_PREFIX=%{_prefix} \
%if "%{_lib}" == "lib64"
	-DLIB_SUFFIX=64 \
%endif
	..

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libphonon.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libphonon.so.?
%attr(755,root,root) %{_libdir}/libphononexperimental.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libphononexperimental.so.?
%attr(755,root,root) %{_libdir}/kde4/plugins/phonon_backend/phonon_xine.so
%dir %{_datadir}/kde4/services/phononbackends
%{_datadir}/kde4/services/phononbackends/xine.desktop
%dir %{_libdir}/kde4
%dir %{_libdir}/kde4/plugins
%dir %{_libdir}/kde4/plugins/phonon_backend
%attr(755,root,root) %{_libdir}/kde4/plugins/phonon_backend/phonon_gstreamer.so
%{_datadir}/dbus-1/interfaces/org.kde.Phonon.AudioOutput.xml
%dir %{_datadir}/kde4
%dir %{_datadir}/kde4/services
%dir %{_datadir}/kde4/services/phononbackends
%{_datadir}/kde4/services/phononbackends/gstreamer.desktop
%{_iconsdir}/oxygen/*/apps/phonon-xine.png

%files devel
%defattr(644,root,root,755)
%{_libdir}/libphonon.so
%{_libdir}/libphononexperimental.so
%{_includedir}/phonon
%dir %{_includedir}/KDE
%{_includedir}/KDE/Phonon
%{_pkgconfigdir}/phonon.pc
