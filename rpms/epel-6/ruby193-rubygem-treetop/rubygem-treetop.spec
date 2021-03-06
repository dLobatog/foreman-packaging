%{!?scl:%global pkg_name %{name}}
%{?scl:%scl_package rubygem-%{gem_name}}

%global gem_name treetop

Summary:        A Ruby-based text parsing and interpretation DSL
Name:           %{?scl_prefix}rubygem-%{gem_name}
Version:        1.4.10
Release:        6%{?dist}
Group:          Development/Languages
License:        MIT
URL:            http://treetop.rubyforge.org/
Source0:        http://rubygems.org/downloads/%{gem_name}-%{version}.gem
BuildRoot:      %{_tmppath}/%{pkg_name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires:       %{?scl_prefix}ruby(abi) = 1.9.1
Requires:       %{?scl_prefix}ruby(rubygems)
Requires:       %{?scl_prefix}rubygem(polyglot) >= 0.3.1
BuildRequires:  %{?scl_prefix}rubygems-devel
# The Following are required for testing
#BuildRequires:  %{?scl_prefix}rubygem(rake)
#BuildRequires:  %{?scl_prefix}rubygem(rspec)
#BuildRequires:  %{?scl_prefix}rubygem(ruby-debug)
BuildArch:      noarch
Provides:       %{?scl_prefix}rubygem(%{gem_name}) = %{version}

%description
Treetop is a language for describing languages. It helps you analyze syntax.


%prep
%setup -q -c -T
mkdir -p .%{gem_dir}
%{?scl:scl enable %scl "}
gem install --local --install-dir .%{gem_dir} \
            -V \
            --force --rdoc %{SOURCE0}
%{?scl:"}

pushd ./%{gem_dir}

%build


%install
mkdir -p $RPM_BUILD_ROOT%{gem_dir}
cp -a .%{gem_dir}/* %{buildroot}%{gem_dir}/
mkdir -p $RPM_BUILD_ROOT/%{_bindir}
mv $RPM_BUILD_ROOT%{gem_dir}/bin/* $RPM_BUILD_ROOT/%{_bindir}
rmdir $RPM_BUILD_ROOT%{gem_dir}/bin
find $RPM_BUILD_ROOT%{gem_instdir}/bin -type f |xargs chmod a+x
find $RPM_BUILD_ROOT%{gem_dir} -name '*.rb' |xargs chmod a-x

# Remove zero-length documentation files
find $RPM_BUILD_ROOT%{gem_docdir} -empty -delete


# Uncomment as soon as we have rubygem-rr in fedora
#%check
#pushd %{buildroot}%{gem_instdir}
#rake spec

%files
%{_bindir}/tt
%dir %{gem_instdir}
%{gem_instdir}/bin
%{gem_libdir}
%{gem_instdir}/Rakefile
%doc %{gem_instdir}/doc
%doc %{gem_instdir}/examples
%doc %{gem_instdir}/README.md
%doc %{gem_instdir}/LICENSE
%doc %{gem_instdir}/spec
%doc %{gem_instdir}/%{gem_name}.gemspec
%doc %{gem_docdir}
%exclude %{gem_cache}
%{gem_spec}


%changelog
* Thu Feb 21 2013 Miroslav Suchý <msuchy@redhat.com> 1.4.10-6
- new package built with tito

* Tue Jul 31 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 1.4.10-5
- Exclude the cached gem.

* Thu Jul 26 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 1.4.10-4
- Specfile cleanup

* Tue Apr 03 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 1.4.10-3
- Rebuilt for scl.

* Mon Jan 30 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 1.4.10-2
- Rebuilt for Ruby 1.9.3.

* Sun Jan 08 2012 <stahnma@fedoraproject.org> - 1.4.10-1
- Rebuilt and fix bz#716045

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Jan 10 2011 Mohammed Morsi <mmorsi@redhat.com> - 1.4.9-1
- Updated to latest upstream release

* Fri Jul 31 2009 Lubomir Rintel (Good Data) <lubo.rintel@gooddata.com> - 1.3.0-1
- Update to new upstream version
- Mark more documentation files as such

* Fri Jun 26 2009 Lubomir Rintel (Good Data) <lubo.rintel@gooddata.com> - 1.2.5-3
- Get rid of duplicate files (thanks to Mamoru Tasaka)

* Mon Jun 08 2009 Lubomir Rintel (Good Data) <lubo.rintel@gooddata.com> - 1.2.5-2
- Fix up documentation list
- Use gem_instdir macro where appropriate
- Do not move examples around
- Depend on ruby(abi)
- Replace defines with globals

* Fri Jun 05 2009 Lubomir Rintel (Good Data) <lubo.rintel@gooddata.com> - 1.2.5-1
- Package generated by gem2rpm
- Move examples into documentation
- Remove empty files
- Fix file permissions
- Fix up License
