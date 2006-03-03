Summary:	Desktop search tool
Summary(pl):	Graficzne narzêdzie do wyszukiwania
Name:		kerry
Version:	0.07
Release:	4
License:	GPL
Group:		X11/Applications
Source0:	%{name}-%{version}.tar.bz2
# Source0-md5:	f90997ff0e42f7c5a18fe33d8ccc56fb
BuildRequires:	beagle-devel
BuildRequires:	kdelibs-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A desktop search tool integrated with Beagle and KDE.

%description -l pl
Graficzne narzêdzie do wyszukiwania zintegrowane z Beagle i KDE.

%prep
%setup -q -n %{name}

%build
%{__make} -f admin/Makefile.common
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_desktopdir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

mv $RPM_BUILD_ROOT{%{_datadir}/applnk/kerry.desktop,%{_desktopdir}}

%find_lang %{name} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kerry
%attr(755,root,root) %{_libdir}/kde3/kerry.so
%{_libdir}/kde3/kerry.la
%attr(755,root,root) %{_libdir}/libkdeinit_kerry.so*
%{_libdir}/libkdeinit_kerry.la
%{_iconsdir}/*/*/*/kerry.*
%{_desktopdir}/kerry.desktop
%{_datadir}/autostart/beagled.desktop
%{_datadir}/autostart/kerry.autostart.desktop
