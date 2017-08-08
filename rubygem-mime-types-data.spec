# Generated from mime-types-data-3.2016.0521.gem by gem2rpm -*- rpm-spec -*-
%global gem_name mime-types-data

Name: rubygem-%{gem_name}
Version: 3.2016.0521
Release: 2%{?dist}
Summary: A registry for information about MIME media type definitions
Group: Development/Languages
License: MIT
URL: https://github.com/mime-types/mime-types-data/
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby >= 2.0
Provides:      rubygem(%{gem_name}) = %{version}
BuildArch: noarch

%description
mime-types-data provides a registry for information about MIME media type
definitions. It can be used with the Ruby mime-types library or other software
to determine defined filename extensions for MIME types, or to use filename
extensions to look up the likely MIME type definitions.


%package doc
Summary: Documentation for %{name}
Group: Documentation
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
gem unpack %{SOURCE0}

%setup -q -D -T -n  %{gem_name}-%{version}

gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec

%build
# Create the gem as gem install only works on a gem file
gem build %{gem_name}.gemspec

# %%gem_install compiles any C extensions and installs the gem into ./%%gem_dir
# by default, so that we can move it into the buildroot in %%install
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/




# Run the test suite
%check
pushd .%{gem_instdir}
# There is nothing to test, since this is just the data package.
popd

%files
%dir %{gem_instdir}
%license %{gem_instdir}/Licence.md
%{gem_instdir}/data
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/Code-of-Conduct.md
%doc %{gem_instdir}/Contributing.md
%doc %{gem_instdir}/History.md
%{gem_instdir}/Manifest.txt
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile

%changelog
* Tue Aug 08 2017 Matthias Runge <mrunge@redhat.com> - 3.2016.0521-2
- add provides for rubygem(mime-data-types)

* Thu Jun 30 2016 Vít Ondruch <vondruch@redhat.com> - 3.2016.0521-1
- Initial package
