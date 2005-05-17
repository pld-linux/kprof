Summary:	KProf - Profiling results viewer
Summary(pl):	KProf - przeglądarka wyników profilowania
Name:		kprof
Version:	1.4.3
Release:	1
License:	GPL
Group:		X11/Development/Tools
Source0:	http://dl.sourceforge.net/kprof/%{name}-%{version}.tar.bz2
# Source0-md5:	d2b1286f8fea7eb1d3e67215e07d296f
Source1:        http://ep09.pld-linux.org/~djurban/kde/kde-common-admin.tar.bz2
# Source1-md5:	81e0b2f79ef76218381270960ac0f55f
Patch0:		%{name}-assert.patch
Patch1:		%{name}-desktop.patch
URL:		http://kprof.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	kdelibs-devel >= 9:3.2.0
BuildRequires:	unsermake >= 040805
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A visual tool for developers that displays the execution profiling
output generated by gprof(1).

%description -l pl
Wizualne narzędzie dla programistów wyświetlające wyniki profilowania
wygenerowane przez gprof(1).

%prep
%setup -q -n %{name} -a1
%patch0 -p1
%patch1 -p1

%build
cp -f /usr/share/automake/config.sub admin
export UNSERMAKE=/usr/share/unsermake/unsermake
%{__make} -f admin/Makefile.common cvs

%configure \
	--with-qt-libraries=%{_libdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir} \
	kde_libs_htmldir=%{_kdedocdir}

%find_lang %{name} --with-kde
install -d $RPM_BUILD_ROOT%{_desktopdir}
mv $RPM_BUILD_ROOT{%{_datadir}/applnk/Development,%{_desktopdir}}/kprof.desktop

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kprof
%{_desktopdir}/kprof.desktop
%{_datadir}/apps/kprof
%{_iconsdir}/*/*/apps/kprof.png
