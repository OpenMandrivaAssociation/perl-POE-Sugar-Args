%define	module	POE-Sugar-Args
%define	name	perl-%{module}
%define	version	1.3
%define	release %mkrel 3
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

