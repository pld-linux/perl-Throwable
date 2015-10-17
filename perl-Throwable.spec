#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	Throwable
%include	/usr/lib/rpm/macros.perl
Summary:	Throwable - a role for classes that can be thrown
#Summary(pl.UTF-8):
Name:		perl-Throwable
Version:	0.200013
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-authors/id/R/RJ/RJBS/Throwable-%{version}.tar.gz
# Source0-md5:	92d4934f601c2d291a65b0bf2ab08dd3
URL:		https://github.com/rjbs/Throwable
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Devel-StackTrace >= 1.32
BuildRequires:	perl-Class-Method-Modifiers
BuildRequires:	perl-Module-Runtime >= 0.002
BuildRequires:	perl-Moo
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Throwable is a role for classes that are meant to be thrown as
exceptions to standard program flow. It is very simple and does only
two things: saves any previous value for $@ and calls die $self.

Throwable is implemented with Moo, so you can stick to Moo or use
Moose, as you prefer.



# %description -l pl.UTF-8 # TODO

%prep
%setup -q -n %{pdir}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}//*.pm
%{perl_vendorlib}/Throwable/
%{_mandir}/man3/*
