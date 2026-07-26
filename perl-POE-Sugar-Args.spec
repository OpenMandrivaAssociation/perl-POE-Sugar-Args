%define	module	POE-Sugar-Args
%define	pdir	POE

Summary:	%{module} module for perl
Name:		perl-%{module}
Version:	1.3
Release:	5
License:	GPL or Artistic
Group:		Development/Perl
Source0:	https://cpan.metacpan.org/authors/id/C/CW/CWEST/POE-Sugar-Args-%{version}.tar.gz
Url:		https://metacpan.org/dist/POE-Sugar-Args
BuildArch:	noarch
BuildRequires:	make
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
%{makeinstall_std}

%clean 

%files
%doc README
%{perl_vendorlib}/POE/*
%{_mandir}/*/*

