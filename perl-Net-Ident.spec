%include	/usr/lib/rpm/macros.perl
%define		__find_provides %{_builddir}/Net-Ident-%{version}/find-perl-provides
Summary:	Net-Ident perl module
Summary(pl):	Modu³ perla Net-Ident
Name:		perl-Net-Ident
Version:	1.20
Release:	3
License:	GPL
Group:		Development/Languages/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Net/Net-Ident-%{version}.tar.gz
Patch0:		%{name}-dep.patch
BuildRequires:	rpm-perlprov >= 3.0.3-18
BuildRequires:	perl >= 5.6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Net-Ident - Perl Ident.

%description -l pl
Net-Ident - Ident w perlu.

%prep
%setup -q -n Net-Ident-%{version}
%patch -p1

chmod +x find-perl-provides

%build
yes "" | perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf Changes README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{perl_sitelib}/Net/Ident.pm
%{_mandir}/man3/*
