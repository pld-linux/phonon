%define		qtver		4.7.2

Summary:	Multimedia API for Qt4/KDE4
Summary(pl.UTF-8):	Biblioteka Phonon
Name:		phonon
Version:	4.5.0
Release:	2
License:	LGPL v2.1
Group:		X11/Libraries
Source0:	ftp://ftp.kde.org/pub/kde/stable/phonon/%{version}/src/%{name}-%{version}.tar.bz2
# Source0-md5:	32f8d388c18fde2e23dea7bb103f9713
Patch0:		%{name}-pkg.patch
URL:		http://phonon.kde.org/
BuildRequires:	QtCore-devel >= %{qtver}
BuildRequires:	QtDBus-devel >= %{qtver}
BuildRequires:	QtNetwork-devel >= %{qtver}
BuildRequires:	QtOpenGL-devel >= %{qtver}
BuildRequires:	QtSql-devel >= %{qtver}
BuildRequires:	QtTest-devel >= %{qtver}
BuildRequires:	automoc4 >= 0.9.86
BuildRequires:	cmake >= 2.8.0
BuildRequires:	gstreamer-plugins-base-devel >= 0.10.0
BuildRequires:	libqzeitgeist-devel
BuildRequires:	pkgconfig
BuildRequires:	pulseaudio-devel >= 0.9.21
BuildRequires:	qt4-build >= %{qtver}
BuildRequires:	qt4-qmake >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.293
BuildRequires:	xine-lib-devel >= 2:1.1.15-4
Requires:	kde-common-dirs >= 0.5
Suggests:	qt4-phonon-backend
Provides:	qt4-phonon
Obsoletes:	qt4-phonon
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Phonon is the multimedia API for Qt4/KDE4.

Phonon was originally created to allow KDE 4 to be independent of any
single multimedia framework such as GStreamer or Xine and to provide a
stable API for KDE4's lifetime. It was done to fix problems of
frameworks becoming unmaintained, API instability, and to create a
simple multimedia API.

%description -l pl.UTF-8
Biblioteka phonon.

%package devel
Summary:	Header files for Phonon library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki Phonon
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	QtCore-devel >= %{qtver}
Requires:	QtDBus-devel >= %{qtver}
Requires:	QtGui-devel >= %{qtver}
Provides:	qt4-phonon-devel
Obsoletes:	qt4-phonon-devel

%description devel
Header files for Phonon library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki Phonon.

%prep
%setup -q
%patch0 -p1

%build
install -d build
cd build
%cmake \
	-DCMAKE_BUILD_TYPE=%{!?debug:Release}%{?debug:Debug} \
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

install -d $RPM_BUILD_ROOT%{_includedir}/qt4
install -d $RPM_BUILD_ROOT%{_libdir}/kde4/plugins/phonon_backend
install -d $RPM_BUILD_ROOT%{_datadir}/kde4/services/phononbackends
ln -s ../phonon $RPM_BUILD_ROOT%{_includedir}/qt4/phonon
ln -s ../KDE/Phonon $RPM_BUILD_ROOT%{_includedir}/phonon/Phonon

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libphonon.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libphonon.so.4
%attr(755,root,root) %{_libdir}/libphononexperimental.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libphononexperimental.so.4
%{_datadir}/dbus-1/interfaces/org.kde.Phonon.AudioOutput.xml
%dir %{_libdir}/kde4/plugins/phonon_backend
%dir %{_datadir}/kde4/services/phononbackends

%files devel
%defattr(644,root,root,755)
%{_libdir}/libphonon.so
%{_libdir}/libphononexperimental.so
%{_includedir}/phonon
%dir %{_includedir}/KDE
%{_includedir}/KDE/Phonon
%{_includedir}/qt4/phonon
%{_pkgconfigdir}/phonon.pc
%{_datadir}/phonon-buildsystem
%{_datadir}/qt4/mkspecs/modules/qt_phonon.pri
