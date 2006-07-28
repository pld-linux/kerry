#
# TODO:
#	- cleanup locale files
#
Summary:	Desktop search tool
Summary(pl):	Graficzne narzêdzie do wyszukiwania
Name:		kerry
Version:	0.1.1
Release:	0.9
License:	GPL
Group:		X11/Applications
Source0:	http://developer.kde.org/~binner/kerry/%{name}-%{version}.tar.bz2
# Source0-md5:	fedb001d73ad80d90ecb850dab19a709
BuildRequires:	beagle-devel
BuildRequires:	kdelibs-devel
Requires:	beagle
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A desktop search tool integrated with Beagle and KDE.

%description -l pl
Graficzne narzêdzie do wyszukiwania zintegrowane z Beagle i KDE.

%prep
%setup -q

%build
%{__make} -f admin/Makefile.common
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_desktopdir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}-%{version} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}-%{version}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kerry
%attr(755,root,root) %{_libdir}/kde3/kerry.so
%{_libdir}/kde3/kerry.la
%attr(755,root,root) %{_libdir}/libkdeinit_kerry.so*
%{_libdir}/libkdeinit_kerry.la
%{_iconsdir}/*/*/*/kerry.*
%{_desktopdir}/kde/kerry.desktop
%{_datadir}/autostart/beagled.desktop
%{_datadir}/autostart/kerry.autostart.desktop
