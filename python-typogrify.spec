%define pypi_name typogrify

Name:           python-%{pypi_name}
Version:        2.0.7
Release:        1
Summary:        Filters to enhance web typography, with support for Django & Jinja templates
Group:          Development/Python
License:        BSD
URL:            https://github.com/mintchaos/typogrify
Source0:        https://files.pythonhosted.org/packages/8a/bf/64959d6187d42472acb846bcf462347c9124952c05bd57e5769d5f28f9a6/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  pkgconfig(python)
BuildRequires:  python3dist(setuptools)

%{?python_provide:%python_provide python3-%{pypi_name}}

%description
Typogrify provides a set of custom filters that automatically apply various
transformations to plain text in order to yield typographically-improved HTML.
While often used in conjunction with Jinja_ and Django_ template systems, the
filters can be used in any environment.


%prep
%autosetup -n %{pypi_name}-%{version}

# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

# remove shebang line from the python scripts
for lib in $(find -type f -name '*.py'); do
 sed -i.python -e '1{\@^#!@d}' $lib
done

%build
%py_build

%install
%py_install

%files -n python3-%{pypi_name}
%license LICENSE.txt
%doc README.rst
%{python_sitelib}/%{pypi_name}/
%{python_sitelib}/%{pypi_name}-%{version}-py%{python_version}.egg-info
