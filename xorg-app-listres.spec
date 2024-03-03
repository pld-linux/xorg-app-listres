Summary:	listres application - list resources in widgets
Summary(pl.UTF-8):	Aplikacja listres - lista zasobów w widgetach
Name:		xorg-app-listres
Version:	1.0.6
Release:	1
License:	MIT
Group:		X11/Applications
Source0:	https://xorg.freedesktop.org/releases/individual/app/listres-%{version}.tar.xz
# Source0-md5:	b4763856d2d9a816cba6eab1410711a0
URL:		https://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	tar >= 1:1.22
BuildRequires:	xorg-lib-libXaw-devel
BuildRequires:	xorg-lib-libXmu-devel
BuildRequires:	xorg-lib-libXt-devel
BuildRequires:	xorg-util-util-macros >= 1.8
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The listres program generates a list of a widget's resource database.
The class in which each resource is first defined, the instance and
class name, and the type of each resource is listed. If no specific
widgets or the -all switch are given, a two-column list of widget
names and their class hierarchies is printed.

%description -l pl.UTF-8
Program listres generuje listę bazy danych zasobów widgetów.
Wypisywana jest klasa, w której każdy zasób jest po raz pierwszy
definiowany, nazwa instancji i klasy oraz typ zasobu. Jeśli nie podano
określonego widgetu lub podano parametr -all, wypisywana jest
dwukolumnowa lista nazw widgetów i ich hierarchii klas.

%prep
%setup -q -n listres-%{version}

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog
%attr(755,root,root) %{_bindir}/listres
%{_mandir}/man1/listres.1*
