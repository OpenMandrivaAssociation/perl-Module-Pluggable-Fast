%define upstream_name	 Module-Pluggable-Fast
%define upstream_version 0.19

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	Fast plugins with instantiation
License:	Artistic/GPL
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Module/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(UNIVERSAL::exports)
BuildRequires:	perl(UNIVERSAL::require)
BuildArch:	noarch

%description
This module is similar to Module::Pluggable but instantiates plugins as soon as
they're found, useful for code generators like Class::DBI::Loader.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc README Changes
%{perl_vendorlib}/Module
%{_mandir}/*/*

%changelog
* Sun Apr 18 2010 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 0.190.0-1mdv2010.1
+ Revision: 536191
- update to 0.19

* Tue Jul 28 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 0.180.0-1mdv2010.0
+ Revision: 401626
- rebuild using %%perl_convert_version
- fixed license field

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 0.18-8mdv2009.0
+ Revision: 257900
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 0.18-7mdv2009.0
+ Revision: 245947
- rebuild

* Sat Dec 22 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.18-5mdv2008.1
+ Revision: 137002
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sat Sep 15 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.18-4mdv2008.0
+ Revision: 86642
- rebuild


* Wed May 03 2006 Nicolas Lécureuil <neoclust@mandriva.org> 0.18-3mdk
- Fix According to perl Policy
	- BuildRequires
	- Source URL

* Thu Dec 22 2005 Michael Scherer <misc@mandriva.org> 0.18-2mdk
- Add perl-UNIVERSAL-require BuildRequires

* Mon Dec 19 2005 Guillaume Rousse <guillomovitch@mandriva.org> 0.18-1mdk
- New release 0.18
- spec cleanup
- fix directory ownership

* Wed Oct 26 2005 Lenny Cartier <lenny@mandriva.com> 0.16-3mdk
- rebuild for allegro

* Thu Sep 29 2005 Nicolas Lécureuil <neoclust@mandriva.org> 0.16-2mdk
- BuildRequires

* Thu Jun 09 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.16-1mdk
- 0.16

* Tue May 03 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.15-1mdk
- First Mandriva release

