Summary:	Peacock, A HTML Editor for GTK+/GNOME
Summary(pl):	Peacock - edytor HTML pod GTK+/GNOME
Name:		peacock
Version:	0.2
Release:	1
License:	GPL
Group:		Development/Tools
Source0:	ftp://download.sourceforge.net/pub/sourceforge/peacock/%{name}-%{version}.tar.gz
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
URL:		http://peacock.sourceforge.net/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%define		_prefix		/usr/X11R6

%description
Peacock is a HTML Editor for GTK+/GNOME. It supports most of basic
HTML. It features Session Management and HTML Preview using the
Gtk-XmHTML widget. It is licensed under GPL.

%description -l pl
Peacock jest edytorem HTML dla GTK+/GNOME. Obs³uguje wiêkszo¶æ podstaw
HTML. Cechuj± go zarz±dzanie sesj± i podgl±d HTML przy u¿yciu widgetu
Gtk-XmHTML. Jest na licencji GPL.

%prep
%setup -q

%build
rm -f missing
gettextize --copy --force
aclocal -I macros
autoconf
automake -a -c
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} DESTDIR=$RPM_BUILD_ROOT \
	sysdir=%{_applnkdir}/Office/Editors install

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
