Summary:	A client for memcached
Name:		apr_memcache
Version:	0.7.0
Release:	0.1
License:	Apache License
Group:		Libraries
Source0:	http://www.outoforder.cc/downloads/apr_memcache/%{name}-%{version}.tar.bz2
# Source0-md5:	1d62fea9253d17d304cfe9b26813ef4c
Patch0:		%{name}-libtool.patch
URL:		http://www.outoforder.cc/projects/libs/apr_memcache/
BuildRequires:	apr-devel >= 1.2.2
BuildRequires:	apr-util-devel >= 1.2.2
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
apr_memcache is a client for memcached written in C, using APR and
APR-Util. It provides pooled client connections and is thread safe,
making it perfect for use inside Apache Modules.

%package devel
Summary:	Development files for apr_memcache
Summary(pl.UTF-8):	Pliki nagłowkowe apr_memcache
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for apr_memcache.

%description devel -l pl.UTF-8
Pliki nagłowkowe apr_memcache.

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
%attr(755,root,root) %{_libdir}/lib*.so.*

%files devel
%defattr(644,root,root,755)
%{_includedir}/apr_memcache-0/
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
