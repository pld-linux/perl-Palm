#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
Summary:	Set of Palm modules
Name:		perl-Palm
Version:	1.3.0
Release:	1
License:	(enter GPL/LGPL/BSD/BSD-like/Artistic/other license name here)
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Palm/ARENSB/p5-Palm-%{version}.tar.gz
# Source0-md5:	67770a4c650f3880a8b1cbded0696e70
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Set of Palm releated modules
Palm::Address Palm::Datebook Palm::Mail Palm::Memo Palm::PDB Palm::Raw Palm::StdAppInfo Palm::ToDo

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
%{perl_vendorlib}/Palm/*pm
%{_bindir}/pdbdump
%{_mandir}/man[13]/*
