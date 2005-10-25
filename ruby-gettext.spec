%define	ruby_archdir	%(ruby -r rbconfig -e 'print Config::CONFIG["archdir"]')
%define ruby_rubylibdir %(ruby -r rbconfig -e 'print Config::CONFIG["rubylibdir"]')
%define	ruby_ridir	%(ruby -r rbconfig -e 'include Config; print File.join(CONFIG["datadir"], "ri", CONFIG["ruby_version"], "system")')
Summary:	gettext binding for Ruby.
Name:		ruby-gettext
Version:	1.0.0
Release:	1
License:	GPL
Group:		Development/Languages
Source0:	http://rubyforge.org/frs/download.php/5885/%{name}-package-%{version}.tar.gz
# Source0-md5:	82e11ac909a982e95bacbdfe5384207e
Source1:	setup.rb
URL:		http://ponx.s5.xrea.com/hiki/ruby-gettext.html
BuildRequires:	ruby
BuildRequires:	ruby-devel
BuildRequires:	gettext-devel
Requires:	ruby
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
gettext binding for Ruby.

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