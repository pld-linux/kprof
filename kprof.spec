Summary:	KProf - Profiling results viewer
Summary(pl):	KProf - przeglądarka wyników profilowania
Name:		kprof
Version:	1.1
Release:	1
License:	GPL
Group:		X11/Development/Tools
Source0:	http://download.sourceforge.net/kprof/%{name}-%{version}.tar.gz
URL:		http://kprof.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
A visual tool for developers that displays the execution profiling
output generated by gprof(1).

%description -l pl
Wizualne narzędzie dla programistów wyświetlające wyniki profilowania
wygenerowane przez gprof(1).

%prep
%setup -q -n kprof-1.1

%build
rm -f missing
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	kdelnkdir=%{_applnkdir}/Development

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kprof
%{_applnkdir}/Development/kprof.desktop
%{_datadir}/apps/kprof
%{_datadir}/icons/medium/locolor/apps/kprof.png
%{_datadir}/icons/small/locolor/apps/kprof.png
