Summary:	gettext binding for Ruby
Summary(pl.UTF-8):	Wiązanie gettexta dla języka Ruby
Name:		ruby-gettext
Version:	2.1.0
Release:	1
License:	GPL
Group:		Development/Languages
Source0:	http://rubyforge.org/frs/download.php/67097/%{name}-package-%{version}.tar.gz
# Source0-md5:	18b1c5268b6e14c2f11c1c93a5bcf11a
Source1:	setup.rb
URL:		http://ponx.s5.xrea.com/hiki/ruby-gettext.html
BuildRequires:	rpmbuild(macros) >= 1.277
BuildRequires:	ruby-modules
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

rdoc -o rdoc/ --main README lib/* --title "%{name} %{version}" --inline-source
rdoc --ri -o ri lib/*
rm ri/created.rid

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_rubylibdir},%{ruby_ridir}}

ruby setup.rb install --prefix=$RPM_BUILD_ROOT

cp -a ri/* $RPM_BUILD_ROOT%{ruby_ridir}

%find_lang rgettext

%clean
rm -rf $RPM_BUILD_ROOT

%files -f rgettext.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/rgettext
%attr(755,root,root) %{_bindir}/rmsgfmt
%attr(755,root,root) %{_bindir}/rmsgmerge
%doc rdoc/*
%{ruby_rubylibdir}/gettext*
# Does not merge well with others.
%{ruby_ridir}/GetText
