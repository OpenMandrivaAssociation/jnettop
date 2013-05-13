Summary: 	Network traffic tracker
Name: 		jnettop
Version:	0.13.0
Release:	%mkrel 9
Group: 		Monitoring
Url:		http://jnettop.kubs.info/
License: 	GPLv2
Source0: 	http://jnettop.kubs.info/dist/%{name}-%{version}.tar.bz2
BuildRequires:	pkgconfig(ncurses)
BuildRequires:	pcap-devel = 1.3.0-2
BuildRequires:	libglib2-devel

%description
Nettop is visualising active network traffic as top does with processes.
It displays active network streams sorted by bandwidth used. This is
often usable when you want to get a fast grip of what is going on on your
outbound router.

%prep
%setup -q

%build
%configure 
%make

%install
%makeinstall

%files
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README .jnettop
%{_bindir}/jnettop
%{_prefix}/share/%{name}/*
%_mandir/man8/jnettop.*
