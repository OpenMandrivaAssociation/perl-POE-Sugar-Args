%define	module	POE-Sugar-Args
%define	name	perl-%{module}
%define	version	1.3
%define	release %mkrel 7
%define	pdir	POE

Summary:	%{module} module for perl
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL or Artistic
Group:		Development/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/POE/%{module}-%{version}.tar.bz2
Url:		http://search.cpan.org/dist/%{module}
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	perl-devel
BuildRequires:  perl(Module::Build)

%description
%{module} module for perl.  This module give an OO representation to
arguments POE passes to event states.  I will not lie to you.  This
adds heavy, bulky code underneath.  On the other hand, it makes
arguments for POE events much more palatable.  Of course, this is a
Sugar module, meaning, it will rot your program in odd (you'll be
hooked) and unexpected ways (performace), but you took the candy so
you can suffer the consequences.

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%install
rm -rf $RPM_BUILD_ROOT
%{makeinstall_std}

%clean 
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README
%{perl_vendorlib}/POE/*
%{_mandir}/*/*



%changelog
* Fri Sep 04 2009 Thierry Vignaud <tvignaud@mandriva.com> 1.3-7mdv2010.0
+ Revision: 430530
- rebuild

* Thu Jul 31 2008 Thierry Vignaud <tvignaud@mandriva.com> 1.3-6mdv2009.0
+ Revision: 258274
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tvignaud@mandriva.com> 1.3-5mdv2009.0
+ Revision: 246331
- rebuild

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 1.3-3mdv2008.1
+ Revision: 136345
- restore BuildRoot

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request

* Tue May 08 2007 Olivier Thauvin <nanardon@mandriva.org> 1.3-3mdv2008.0
+ Revision: 25145
- rebuild


* Wed May 03 2006 Nicolas Lécureuil <neoclust@mandriva.org> 1.3-2mdk
- Fix According to perl Policy
	- BuildRequires
	- Source URL
	- URL
- use mkrel

* Thu Jun 03 2004 Per Ã˜yvind Karlsen <peroyvind@linux-mandrake.com> 1.3-1mdk
- 1.3
- cosmetics
- no hardcoded path in %%files

* Mon Mar 01 2004 Michael Scherer <misc@mandrake.org> 1.2-2mdk
- use automatic Requires

