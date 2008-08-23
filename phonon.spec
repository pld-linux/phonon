%define		qtver		4.4.1
%define		snap	r851285
Summary:	Phonon library
Summary(pl.UTF-8):	Biblioteka Phonon
Name:		phonon
Version:	4.2.1
Release:	0.%{snap}.1
License:	LGPL v2.1
Group:		X11/Libraries
#Source0:	ftp://ftp.kde.org/pub/kde/stable/phonon/%{version}/%{name}-%{version}.tar.bz2
Source0:	%{name}-%{version}-%{snap}.tar.bz2
# Source0-md5:	6d68c4605a04e68eb52f96d28e31a89d
URL:		http://phonon.kde.org/
BuildRequires:	QtCore-devel >= %{qtver}
BuildRequires:	QtDBus-devel >= %{qtver}
BuildRequires:	QtNetwork-devel >= %{qtver}
BuildRequires:	QtOpenGL-devel >= %{qtver}
BuildRequires:	QtSql-devel >= %{qtver}
BuildRequires:	QtTest-devel >= %{qtver}
BuildRequires:	automoc4 >= 0.9.86
BuildRequires:	cmake >= 2.6.1-2
BuildRequires:	gstreamer-plugins-base-devel >= 0.10.0
BuildRequires:	qt4-build >= %{qtver}
BuildRequires:	qt4-qmake >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.293
Provides:	qt4-phonon
Obsoletes:	qt4-phonon
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Phonon library.

%description -l pl.UTF-8
Biblioteka phonon.

%package devel
Summary:        Header files for Phonon library
Summary(pl.UTF-8):	Pliki nag³ówkowe biblioteki Phonon
Group:          Development/Libraries
Requires:	%{name} == %{version}-%{release}
Requires:	QtCore-devel >= %{qtver}
Requires:	QtDBus-devel >= %{qtver}
Requires:	QtGui-devel >= %{qtver}
Provides:	qt4-phonon-devel
Obsoletes:	qt4-phonon-devel

%description devel
Header files for phonon.

%description devel -l pl.UTF-8
Pliki nag³ówkowe dla phonon.

%package xine
Summary:	Xine backend to Phonon
Summary(pl.UTF-8):	Backend Xine dla Phonona
Group:		X11/Applications
Requires:	%{name} == %{version}-%{version}
Obsoletes:	kde4-phonon-xine

%description xine
Xine backend to Phonon.

%description xine -l pl.UTF-8
Backend Xine dla Phonona.

%prep
%setup -q -n %{name}-%{version}-%{snap}

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
%dir %{_libdir}/kde4
%dir %{_libdir}/kde4/plugins
%dir %{_libdir}/kde4/plugins/phonon_backend
%attr(755,root,root) %{_libdir}/kde4/plugins/phonon_backend/phonon_gstreamer.so
%{_datadir}/dbus-1/interfaces/org.kde.Phonon.AudioOutput.xml
%dir %{_datadir}/kde4
%dir %{_datadir}/kde4/services
%dir %{_datadir}/kde4/services/phononbackends
%{_datadir}/kde4/services/phononbackends/gstreamer.desktop

%files devel
%defattr(644,root,root,755)
%{_libdir}/libphonon.so
%{_libdir}/libphononexperimental.so
%{_includedir}/phonon
%dir %{_includedir}/KDE
%{_includedir}/KDE/Phonon
%{_pkgconfigdir}/phonon.pc

%files xine
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde4/plugins/phonon_backend/phonon_xine.so
%dir %{_datadir}/kde4/services/phononbackends
%{_datadir}/kde4/services/phononbackends/xine.desktop
