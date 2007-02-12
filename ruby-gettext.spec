Summary:	gettext binding for Ruby
Summary(pl.UTF-8):	Wiązanie gettexta dla języka Ruby
Name:		ruby-gettext
Version:	1.0.0
Release:	2
License:	GPL
Group:		Development/Languages
Source0:	http://rubyforge.org/frs/download.php/5885/%{name}-package-%{version}.tar.gz
# Source0-md5:	82e11ac909a982e95bacbdfe5384207e
Source1:	setup.rb
URL:		http://ponx.s5.xrea.com/hiki/ruby-gettext.html
BuildRequires:	gettext-devel
BuildRequires:	rpmbuild(macros) >= 1.277
BuildRequires:	ruby-devel
%{?ruby_mod_ver_requires_eq}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
gettext binding for Ruby.

%description -l pl.UTF-8
Wiązanie gettexta dla języka Ruby.

%prep
%setup -q -n %{name}-package-%{version}

%build
install %{SOURCE1} setup.rb
ruby setup.rb config \
	--siterubyver=%{ruby_rubylibdir} \
	--sodir=%{ruby_archdir}

ruby setup.rb setup

rdoc -o rdoc/ --main README README lib/* --title "%{name} %{version}" --inline-source
rdoc --ri -o ri lib/*

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_rubylibdir},%{ruby_ridir}}

ruby setup.rb install --prefix=$RPM_BUILD_ROOT

cp -a ri/ri/* $RPM_BUILD_ROOT%{ruby_ridir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc rdoc/*
%dir %{ruby_archdir}/gettext
%attr(755,root,root) %{ruby_archdir}/gettext/*.so
%{ruby_rubylibdir}/gettext*
# Does not merge well with others.
%{ruby_ridir}/GetText
