#
# Conditional build:
%bcond_with	tests	# do not perform "make test"

%define		pdir	Net
%define		pnam	Ident
%include	/usr/lib/rpm/macros.perl
Summary:	Net::Ident perl module
Summary(pl.UTF-8):	Moduł perla Net::Ident
Name:		perl-Net-Ident
Version:	1.23
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	f9a2943dc6310c1f31458c49f926b007
URL:		http://search.cpan.org/dist/Net-Ident/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoprov	"perl(FileHandle)"

%description
Net::Ident - Perl Ident.

%description -l pl.UTF-8
Net::Ident - Ident w perlu.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
yes "" | perl Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Net/Ident.pm
%{_mandir}/man3/*
