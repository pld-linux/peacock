Summary:	Peacock, A HTML Editor for GTK+/GNOME
Name:		peacock
Version:	0.2
Release:	1
License:	GPL
Group:		Development/Tools
Group(de):	Entwicklung/Werkzeuge
Group(fr):	Development/Outils
Group(pl):	Programowanie/Narzêdzia
Source0:	ftp://download.sourceforge.net/pub/sourceforge/peacock/%{name}-%{version}.tar.gz
BuildRequires:	gettext-devel
URL:		http://peacock.sourceforge.net/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%define		_prefix		/usr/X11R6

%description
Peacock is a HTML Editor for GTK+/GNOME. It supports most of basic
HTML. It features Session Management and HTML Preview using the
Gtk-XmHTML widget. It is licensed under GPL.

%prep
%setup -q

%build
gettextize --copy --force
aclocal -I macros
autoconf
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	sysdir=%{_applnkdir}/Office/Editors

gzip -9nf README AUTHORS NEWS TODO ChangeLog THANKS HACKING

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/peacock
%{_pixmapsdir}/peacock
%{_applnkdir}/Office/Editors/peacock.desktop
