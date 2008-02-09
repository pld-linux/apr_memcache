Summary:	A client for memcached
Summary(pl.UTF-8):	Klient memcached
Name:		apr_memcache
Version:	0.7.0
Release:	1
License:	Apache v2.0
Group:		Libraries
Source0:	http://www.outoforder.cc/downloads/apr_memcache/%{name}-%{version}.tar.bz2
# Source0-md5:	1d62fea9253d17d304cfe9b26813ef4c
Patch0:		%{name}-libtool.patch
URL:		http://www.outoforder.cc/projects/libs/apr_memcache/
BuildRequires:	apr-devel >= 1:1.2.2
BuildRequires:	apr-util-devel >= 1:1.2.2
BuildRequires:	autoconf >= 2.53
BuildRequires:	automake
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
apr_memcache is a client for memcached written in C, using APR and
APR-Util. It provides pooled client connections and is thread safe,
making it perfect for use inside Apache Modules.

%description -l pl.UTF-8
apr_memcache to klient memcached napisany w C, wykorzystujący APR i
APR-Util. Udostępnia pule połączeń klienckich i może być używany
wielowątkowo, co czyni go dobrze nadającym się do używania w modułach
Apache'a.

%package devel
Summary:	Development files for apr_memcache
Summary(pl.UTF-8):	Pliki nagłówkowe apr_memcache
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	apr-devel >= 1:1.2.2
Requires:	apr-util-devel >= 1:1.2.2

%description devel
Header files for apr_memcache.

%description devel -l pl.UTF-8
Pliki nagłówkowe apr_memcache.

%package static
Summary:	Static apr_memcache library
Summary(pl.UTF-8):	Statyczna biblioteka apr_memcache
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static apr_memcache library.

%description static -l pl.UTF-8
Statyczna biblioteka apr_memcache.

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoheader}
%{__automake}
%{__autoconf}

%configure \
	--with-apr=%{_bindir}/apr-1-config \
	--with-apr-util=%{_bindir}/apu-1-config

%{__make} \
	CFLAGS="%{rpmcflags} `apu-1-config --includes` `apr-1-config --includes`"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc LICENSE NOTICE test
%attr(755,root,root) %{_libdir}/libapr_memcache.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libapr_memcache.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libapr_memcache.so
%{_libdir}/libapr_memcache.la
%{_includedir}/apr_memcache-0

%files static
%defattr(644,root,root,755)
%{_libdir}/libapr_memcache.a
