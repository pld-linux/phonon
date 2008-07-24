%define		qtbrver		4.4.0
Summary:	Phonon library
Summary(pl.UTF-8):	Biblioteka phonon
Name:		phonon
Version:	4.2.0
Release:	2
License:	GPL v2
Group:		X11/Libraries
Source0:	ftp://ftp.kde.org/pub/kde/stable/phonon/%{version}/%{name}-%{version}.tar.bz2
# Source0-md5:	de80b0f055886a6946acc7886713e23e
URL:		http://phonon.kde.org/
BuildRequires:	QtCore-devel >= %{qtbrver}
BuildRequires:	QtDBus-devel >= %{qtbrver}
BuildRequires:	QtNetwork-devel >= %{qtbrver}
BuildRequires:	QtOpenGL-devel >= %{qtbrver}
BuildRequires:	QtSql-devel >= %{qtbrver}
BuildRequires:	QtTest-devel >= %{qtbrver}
BuildRequires:	automoc4 >= 0.9.83
BuildRequires:	cmake
BuildRequires:	gstreamer-plugins-base-devel >= 0.10.20
BuildRequires:	qt4-build >= %{qtbrver}
BuildRequires:	qt4-qmake >= %{qtbrver}
BuildRequires:	rpmbuild(macros) >= 1.293
Provides:	qt4-phonon
Obsoletes:	qt4-phonon
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Phonon library.

%description -l pl.UTF-8
Biblioteka phonon.

%package devel
Summary:        Phonon files
Group:          Development/Libraries
Requires:	%{name} == %{version}-%{release}
Provides:	qt4-phonon-devel
Obsoletes:	qt4-phonon-devel

%description devel
Header files for phonon.

%description devel -l pl.UTF-8
Pliki nagłówkowe dla phonon.

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
%dir %{_libdir}/kde4
%dir %{_libdir}/kde4/plugins
%dir %{_libdir}/kde4/plugins/phonon_backend
%attr(755,root,root) %{_libdir}/kde4/plugins/phonon_backend/phonon_gstreamer.so
%dir %{_datadir}/dbus-1/interfaces
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
