%include	/usr/lib/rpm/macros.perl
%define		__find_provides %{_builddir}/Net-Ident-%{version}/find-perl-provides
Summary:	Net-Ident perl module
Summary(pl):	Modu� perla Net-Ident
Name:		perl-Net-Ident
Version:	1.20
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/J�zyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Net/Net-Ident-%{version}.tar.gz
Patch0:		perl-Net-Ident-dep.patch
BuildRequires:	rpm-perlprov >= 3.0.3-18
BuildRequires:	perl >= 5.005_03-14
%requires_eq	perl
Requires:	%{perl_sitearch}
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

(
  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/Net/Ident
  sed -e "s#$RPM_BUILD_ROOT##" .packlist >.packlist.new
  mv .packlist.new .packlist
)

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man3/* \
        Changes README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {Changes,README}.gz

%{perl_sitelib}/Net/Ident.pm
%{perl_sitearch}/auto/Net/Ident

%{_mandir}/man3/*
