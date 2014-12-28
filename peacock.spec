Summary:	Peacock, A HTML Editor for GTK+/GNOME
Summary(pl.UTF-8):	Peacock - edytor HTML pod GTK+/GNOME
Name:		peacock
Version:	1.9.1
Release:	1
License:	GPL v2
Group:		X11/Applications/Editors
Source0:	http://dl.sourceforge.net/peacock/%{name}-%{version}.tar.gz
# Source0-md5:	85283f1c5f6e271ed7f977b18d7504b0
URL:		http://peacock.sourceforge.net/
BuildRequires:	gettext-tools
BuildRequires:	gtksourceview-devel >= 0.5
BuildRequires:	libbonoboui-devel >= 2.2.0
BuildRequires:	libglade2-devel >= 2.0.1
BuildRequires:	libgnomeui-devel >= 2.2.0
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Peacock is a HTML Editor for GTK+/GNOME. It supports most of basic
HTML. It features Session Management and HTML Preview using the
Gtk-XmHTML widget. It is licensed under GPL.

%description -l pl.UTF-8
Peacock jest edytorem HTML dla GTK+/GNOME. Obsługuje większość podstaw
HTML. Cechują go zarządzanie sesją i podgląd HTML przy użyciu widgetu
Gtk-XmHTML. Jest na licencji GPL.

%prep
%setup -q

%build
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
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/peacock-2
%{_datadir}/peacock-2
