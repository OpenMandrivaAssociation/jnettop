Summary: 	Network traffic tracker
Name: 		jnettop
Version:	0.13.0
Release:	%mkrel 6
Group: 		Monitoring
Url:		http://jnettop.kubs.info/
License: 	GPL
Source: 	http://jnettop.kubs.info/dist/%{name}-%{version}.tar.bz2
Buildroot: 	%{_tmppath}/%{name}-%{version}-buildroot
BuildRequires:	libncurses-devel
BuildRequires:	libpcap-devel
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
rm -rf $RPM_BUILD_ROOT
%makeinstall

%clean
rm -r $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README .jnettop
%{_bindir}/jnettop
%{_prefix}/share/%{name}/*
%_mandir/man8/jnettop.*


