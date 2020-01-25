#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%define	pnam	Palm
Summary:	Set of Palm modules
Summary(pl.UTF-8):	Zestaw modułów Palm
Name:		perl-Palm
Version:	1.3.0
Release:	2
License:	Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-authors/id/A/AR/ARENSB/p5-%{pnam}-%{version}.tar.gz
# Source0-md5:	67770a4c650f3880a8b1cbded0696e70
URL:		http://search.cpan.org/dist/-Palm/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Set of Palm related modules: Palm::Address, Palm::Datebook,
Palm::Mail, Palm::Memo, Palm::PDB, Palm::Raw, Palm::StdAppInfo,
Palm::ToDo.

%description -l pl.UTF-8
Zestaw modułów związanych z Palmem: Palm::Address, Palm::Datebook,
Palm::Mail, Palm::Memo, Palm::PDB, Palm::Raw, Palm::StdAppInfo,
Palm::ToDo.

%prep
%setup -q -n p5-Palm-1.003_000

%build
%{__perl} Makefile.PL \
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
%doc ChangeLog README
%attr(755,root,root) %{_bindir}/pdbdump
%dir %{perl_vendorlib}/Palm
%{perl_vendorlib}/Palm/*pm
%{_mandir}/man[13]/*
