#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Curses
Version  : 1.36
Release  : 10
URL      : https://cpan.metacpan.org/authors/id/G/GI/GIRAFFED/Curses-1.36.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/G/GI/GIRAFFED/Curses-1.36.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libc/libcurses-perl/libcurses-perl_1.36-1.debian.tar.xz
Summary  : ~
Group    : Development/Tools
License  : Artistic-1.0 GPL-1.0
Requires: perl-Curses-data = %{version}-%{release}
Requires: perl-Curses-lib = %{version}-%{release}
Requires: perl-Curses-license = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : pkgconfig(ncursesw)

%description
The Curses Perl Module
============================================================
COPYRIGHT AND LICENSE INFORMATION IS AT THE END OF THIS FILE
============================================================

%package data
Summary: data components for the perl-Curses package.
Group: Data

%description data
data components for the perl-Curses package.


%package dev
Summary: dev components for the perl-Curses package.
Group: Development
Requires: perl-Curses-lib = %{version}-%{release}
Requires: perl-Curses-data = %{version}-%{release}
Provides: perl-Curses-devel = %{version}-%{release}

%description dev
dev components for the perl-Curses package.


%package lib
Summary: lib components for the perl-Curses package.
Group: Libraries
Requires: perl-Curses-data = %{version}-%{release}
Requires: perl-Curses-license = %{version}-%{release}

%description lib
lib components for the perl-Curses package.


%package license
Summary: license components for the perl-Curses package.
Group: Default

%description license
license components for the perl-Curses package.


%prep
%setup -q -n Curses-1.36
cd ..
%setup -q -T -D -n Curses-1.36 -b 1
mkdir -p deblicense/
mv %{_topdir}/BUILD/debian/* %{_topdir}/BUILD/Curses-1.36/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Curses
cp Copying %{buildroot}/usr/share/package-licenses/perl-Curses/Copying
cp deblicense/copyright %{buildroot}/usr/share/package-licenses/perl-Curses/deblicense_copyright
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.28.1/x86_64-linux-thread-multi/Curses.pm

%files data
%defattr(-,root,root,-)
/usr/share/package-licenses/perl-Curses/Copying

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Curses.3

%files lib
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.28.1/x86_64-linux-thread-multi/auto/Curses/Curses.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Curses/deblicense_copyright
