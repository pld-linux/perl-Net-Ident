%include	/usr/lib/rpm/macros.perl
%define	pdir	Net
%define	pnam	Ident
Summary:	Net::Ident perl module
Summary(pl):	Modu³ perla Net::Ident
Name:		perl-Net-Ident
Version:	1.20
Release:	8
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl >= 5.6.1
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoprov	"perl(FileHandle)"

%description
Net::Ident - Perl Ident.

%description -l pl
Net::Ident - Ident w perlu.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
yes "" | perl Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Net/Ident.pm
%{_mandir}/man3/*
