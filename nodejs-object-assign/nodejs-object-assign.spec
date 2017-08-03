%global npm_name object-assign

Name: nodejs-%{npm_name}
Version: 4.1.1
Release: 1%{?dist}
Summary: ES2015 `Object
License: MIT
URL: https://github.com/sindresorhus/object-assign
Source0: http://registry.npmjs.org/%{npm_name}/-/%{npm_name}-%{version}.tgz
BuildRequires: nodejs-packaging
BuildArch:  noarch
ExclusiveArch: %{nodejs_arches} noarch
Provides: npm(%{npm_name}) = %{version}

%{?nodejs_find_provides_and_requires}

%define npm_cache_dir /tmp/npm_cache_%{name}-%{version}-%{release}
%description
%{summary}

%prep
%setup -q -n package

%build
%nodejs_symlink_deps --build

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr index.js license package.json readme.md %{buildroot}%{nodejs_sitelib}/%{npm_name}

%clean
rm -rf %{buildroot} %{npm_cache_dir}

%files
%{nodejs_sitelib}/%{npm_name}

%doc license
%doc readme.md

%changelog
* Thu Aug 3 2017 author@example.com <Author Name> - 4.1.1-1
- First release
