%include	/usr/lib/rpm/macros.perl
Summary:	ctrace is a multiprotocol traceroute tool
Summary(pl):	ctrace jest wieloprotokołowym narzędziem do śledzenia pakietów
Name:		ctrace
Version:	0.8
Release:	1
License:	distributable
Group:		Applications/Networking
Source0:	http://www.pratyeka.org/ctrace/download/%{name}-%{version}.tar.bz2
BuildRequires:	perl-Net-RawIP
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Multiprotocol traceroute tool.

%description -l pl
Wieloprotokołowe narzędzie do śledzenia tras pakietów.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sbindir},%{_mandir}/man1}

install ctrace $RPM_BUILD_ROOT%{_sbindir}
install ctrace.man $RPM_BUILD_ROOT%{_mandir}/man1/ctrace.1

gzip -9nf BUGS HISTORY

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_sbindir}/ctrace
%{_mandir}/man1/*
