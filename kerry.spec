
Summary:	Desktop search tool
Summary(pl.UTF-8):   Graficzne narzędzie do wyszukiwania
Name:		kerry
Version:	0.2.1
Release:	0.1
License:	GPL
Group:		X11/Applications
Source0:	http://developer.kde.org/~binner/kerry/%{name}-%{version}.tar.bz2
# Source0-md5:	c5885de1b18c9c7cf944d8845eb9c64c
Patch0:		kde-ac260-lt.patch
BuildRequires:	beagle-devel
BuildRequires:	kdelibs-devel
Requires:	beagle
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A desktop search tool integrated with Beagle and KDE.

%description -l pl.UTF-8
Graficzne narzędzie do wyszukiwania zintegrowane z Beagle i KDE.

%prep
%setup -q
%patch0 -p1

%build
%{__make} -f admin/Makefile.common
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_desktopdir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}
%find_lang kcmbeagle

cat kcmbeagle.lang >> %{name}.lang

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kerry
%{_datadir}/applnk/.hidden/*.desktop
%{_datadir}/apps/kerry
%attr(755,root,root) %{_libdir}/kde3/kcm_beagle.so
%{_libdir}/kde3/kcm_beagle.la
%attr(755,root,root) %{_libdir}/kde3/kerry.so
%{_libdir}/kde3/kerry.la
%attr(755,root,root) %{_libdir}/libkdeinit_kerry.so*
%{_libdir}/libkdeinit_kerry.la
%{_iconsdir}/*/*/*/kerry*
%{_desktopdir}/kde/*
%{_datadir}/autostart/beagled.desktop
%{_datadir}/autostart/kerry.autostart.desktop
