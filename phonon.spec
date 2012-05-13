%define		qtver		4.8.1

Summary:	Phonon: multimedia API for Qt4/KDE4
Summary(pl.UTF-8):	Phonon - biblioteka multimedialna dla Qt4/KDE4
Name:		phonon
Version:	4.6.0
Release:	3
License:	LGPL v2.1 or LGPL v3
Group:		X11/Libraries
Source0:	ftp://ftp.kde.org/pub/kde/stable/phonon/%{version}/src/%{name}-%{version}.tar.xz
# Source0-md5:	bbe0c1c62ed14c31479c4c1a6cf1e173
Patch0:		%{name}-pkg.patch
Patch1:		fix-plugindir-for-qt-app.patch
URL:		http://phonon.kde.org/
BuildRequires:	QtCore-devel >= %{qtver}
BuildRequires:	QtDBus-devel >= %{qtver}
BuildRequires:	QtNetwork-devel >= %{qtver}
BuildRequires:	QtOpenGL-devel >= %{qtver}
BuildRequires:	QtSql-devel >= %{qtver}
BuildRequires:	QtTest-devel >= %{qtver}
BuildRequires:	automoc4 >= 0.9.86
BuildRequires:	cmake >= 2.8.0
BuildRequires:	glib2-devel >= 2.0
BuildRequires:	libqzeitgeist-devel >= 0.8
BuildRequires:	pkgconfig
BuildRequires:	pulseaudio-devel >= 0.9.21
BuildRequires:	qt4-build >= %{qtver}
BuildRequires:	qt4-qmake >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.603
Requires:	kde-common-dirs >= 0.5
Requires:	libqzeitgeist >= 0.8
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
Phonon to biblioteka multimedialna dla Qt4/KDE4.

Pierwotnie powstała, aby pozwolić na niezależność KDE 4 od konkretnego
środowiska multimedialnego, takiego jak GStreamer czy Xine, oraz
zapewnić stabilne API na cały czas życia KDE4. Została stworzona w
celu wyeliminowania problemów z porzucaniem bibliotek i
niestabilnością ich API, a także w celu stworzenia prostego API
multimedialnego.

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
%patch1 -p1


%build
install -d build
cd build
# disable designer plugin - currently packaged in QtDesigner package
%cmake .. \
	-DPHONON_BUILD_DESIGNER_PLUGIN=OFF

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
%attr(755,root,root) %{_libdir}/libphonon.so
%attr(755,root,root) %{_libdir}/libphononexperimental.so
%{_includedir}/phonon
%dir %{_includedir}/KDE
%{_includedir}/KDE/Phonon
%{_includedir}/qt4/phonon
%{_pkgconfigdir}/phonon.pc
%{_libdir}/cmake/phonon
%dir %{_datadir}/phonon
%{_datadir}/phonon/buildsystem
%{_datadir}/qt4/mkspecs/modules/qt_phonon.pri
