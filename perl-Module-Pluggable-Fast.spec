%define module	Module-Pluggable-Fast
%define name	perl-%{module}
%define version 0.18
%define release %mkrel 4

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Fast plugins with instantiation
License:	Artistic/GPL
Group:		Development/Perl
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/Module/%{module}-%{version}.tar.bz2
URL:		http://search.cpan.org/dist/%{module}/
%if %{mdkversion} < 1010
Buildrequires:	perl-devel
%endif
Buildrequires:	perl(UNIVERSAL::exports)
Buildrequires:	perl(UNIVERSAL::require)
BuildArch:	noarch
Buildroot:	%{_tmppath}/%{name}-%{version}

%description
This module is similar to Module::Pluggable but instantiates plugins as soon as
they're found, useful for code generators like Class::DBI::Loader.

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%{__make} test

%install
rm -rf %{buildroot}
%makeinstall_std

%files
%defattr(-,root,root)
%doc README Changes
%{perl_vendorlib}/Module
%{_mandir}/*/*

%clean
rm -rf %{buildroot}

