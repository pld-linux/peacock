Summary:	Peacock, A HTML Editor for GTK+/GNOME
Summary(pl):	Peacock - edytor HTML pod GTK+/GNOME
Name:		peacock
Version:	0.5
Release:	0.2
License:	GPL v2
Group:		X11/Applications/Editors
Source0:	ftp://download.sourceforge.net/pub/sourceforge/peacock/%{name}-%{version}.tar.gz
Patch0:		%{name}-DESTDIR.patch
Patch1:		%{name}-libraries.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gdk-pixbuf-devel
BuildRequires:	gdk-pixbuf-gnome-devel
BuildRequires:	gettext-devel
BuildRequires:	gtkhtml-devel >= 0.4
BuildRequires:	libglade-devel >= 0.16
BuildRequires:	pong-devel
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
#%patch0 -p1
#%patch1 -p1

%build
#cat /usr/share/aclocal/intltool.m4 >> aclocal.m4
#rm -f missing
#%{__gettextize}
#intltoolize --copy --force
#aclocal -I macros
#%{__autoconf}
#%{__automake}
%configure2_13

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} DESTDIR=$RPM_BUILD_ROOT \
	sysdir=%{_applnkdir}/Office/Editors install

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog HACKING NEWS README THANKS TODO
%attr(755,root,root) %{_bindir}/peacock
%{_pixmapsdir}/peacock
%{_applnkdir}/Office/Editors/peacock.desktop
