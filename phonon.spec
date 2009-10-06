%define		qtver		4.5.1
Summary:	Multimedia API for KDE 4
Summary(pl.UTF-8):	Biblioteka Phonon
Name:		phonon
Version:	4.3.1
Release:	7
License:	LGPL v2.1
Group:		X11/Libraries
Source0:	ftp://ftp.kde.org/pub/kde/stable/4.3.1/src/%{name}-%{version}.tar.bz2
# Source0-md5:	767cb68052c108e95f293f30acdef3fb
Patch0:		%{name}-pkg.patch
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
Requires:	qt4-phonon-backend
Provides:	qt4-phonon
Obsoletes:	qt4-phonon
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Phonon is the multimedia API for KDE 4. Phonon was created to allow
KDE 4 to be independent of any single multimedia framework such as
GStreamer or xine and to provide a stable API for KDE 4's lifetime. It
was done to fix problems of frameworks becoming unmaintained, API
instability, and to create a simple multimedia API.

%description -l pl.UTF-8
Biblioteka phonon.

%package devel
Summary:	Header files for Phonon library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki Phonon
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
Pliki nagłówkowe biblioteki Phonon.

%package backend-xine
Summary:	Xine backend for Phonon
Summary(pl.UTF-8):	Wtyczki Xine dla Phonon
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Provides:	qt4-phonon-backend = %{version}
Obsoletes:	kde4-phonon-xine

%description backend-xine
Xine backend for Phonon.

%description backend-xine -l pl.UTF-8
Wtyczki Xine dla Phonon.

%package backend-gstreamer
Summary:	GStreamer backend for Phonon
Summary(pl.UTF-8):	Wtyczki GStreamera dla Phonon
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Provides:	qt4-phonon-backend = %{version}

%description backend-gstreamer
GStreamer backend for Phonon.

%description backend-gstreamer -l pl.UTF-8
Wtyczki GStreamera dla Phonon.

%prep
%setup -q
%patch0 -p1

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

mkdir -p $RPM_BUILD_ROOT%{_includedir}/qt4
ln -s ../phonon $RPM_BUILD_ROOT/%{_includedir}/qt4/phonon
ln -s ../KDE/Phonon $RPM_BUILD_ROOT/%{_includedir}/phonon/Phonon

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
%dir %{_datadir}/kde4
%dir %{_datadir}/kde4/services
%dir %{_datadir}/kde4/services/phononbackends
%dir %{_datadir}/kde4/services/phononbackends
%dir %{_libdir}/kde4/plugins
%dir %{_libdir}/kde4/plugins/phonon_backend
%{_datadir}/dbus-1/interfaces/org.kde.Phonon.AudioOutput.xml

%files backend-xine
%attr(755,root,root) %{_libdir}/kde4/plugins/phonon_backend/phonon_xine.so
%{_datadir}/kde4/services/phononbackends/xine.desktop
%{_iconsdir}/oxygen/*/apps/phonon-xine.png

%files backend-gstreamer
%attr(755,root,root) %{_libdir}/kde4/plugins/phonon_backend/phonon_gstreamer.so
%{_datadir}/kde4/services/phononbackends/gstreamer.desktop

%files devel
%defattr(644,root,root,755)
%{_libdir}/libphonon.so
%{_libdir}/libphononexperimental.so
%{_includedir}/phonon
%dir %{_includedir}/KDE
%{_includedir}/KDE/Phonon
%{_includedir}/qt4/phonon
%{_pkgconfigdir}/phonon.pc
