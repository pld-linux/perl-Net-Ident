#
# Conditional build:
%bcond_without	tests	# test suite

%define		pdir	Net
%define		pnam	Ident
Summary:	Lookup the username on the remote end of a TCP/IP connection
Summary(pl.UTF-8):	Wyszukiwanie nazwy użytkownika po zdalnej stronie połączenia TCP/IP
Name:		perl-Net-Ident
Version:	1.31
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	https://www.cpan.org/modules/by-module/Net/TODDR/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	d6c9047a79dd1c904fba3098c5aba2fb
URL:		https://metacpan.org/dist/Net-Ident
BuildRequires:	perl-devel >= 1:5.10
%if %{with tests}
BuildRequires:	perl-Test-Simple
%endif
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.745
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoprov_perl	FileHandle

%description
Net::Ident is a module that looks up the username on the remote side
of a TCP/IP connection through the ident (auth/tap) protocol described
in RFC 1413 (which supersedes RFC 931). Note that this requires the
remote site to run a daemon (often called identd) to provide the
requested information, so it is not always available for all TCP/IP
connections.

%description -l pl.UTF-8
Net::Ident to moduł sprawdzający nazwę użytkownika zdalnego końca
połączenia TCP/IP poprzez protokół ident (auth/tap), opisany w RFC 1413
(zastępującym RFC 931). Wymaga to, aby po drugiej stronie działał
demon (zwykle o nazwie identd), zapewniający żądane informacje, więc
nie jest to dostępne dla wszystkich połączeń TCP/IP.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make}

%if %{with tests}
%{__make} test
%endif

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README.md
%{perl_vendorlib}/Net/Ident.pm
%{_mandir}/man3/Net::Ident.3pm*
