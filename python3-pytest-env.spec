#
# Conditional build:
%bcond_without	tests	# unit tests

Summary:	Set environment variables for pytest sessions
Summary(pl.UTF-8):	Ustawianie zmiennych środowiskowych dla sesji pytesta
Name:		python3-pytest-env
Version:	1.8.4
Release:	1
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/pytest-env/
Source0:	https://files.pythonhosted.org/packages/source/p/pytest-env/pytest_env-%{version}.tar.gz
# Source0-md5:	29ad968fcce228a23d7b960653b9adc7
URL:		https://pypi.org/project/pytest-env/
BuildRequires:	python3-build
BuildRequires:	python3-hatch-fancy-pypi-readme >= 25.1
BuildRequires:	python3-hatch-vcs >= 0.5
BuildRequires:	python3-hatchling >= 1.32.4
BuildRequires:	python3-installer
BuildRequires:	python3-modules >= 1:3.11
%if %{with tests}
BuildRequires:	python3-dotenv >= 1.2.4
BuildRequires:	python3-pytest >= 9.1.1
BuildRequires:	python3-pytest-mock >= 3.16
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 2.044
Requires:	python3-modules >= 1:3.11
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A pytest plugin that sets environment variables from pyproject.toml,
pytest.toml, .pytest.toml, or pytest.ini configuration files. It can
also load variables from .env files.

%description -l pl.UTF-8
Wtyczka pytesta, ustawiająca zmienne środowiskowe z plików
konfiguracyjnych pyproject.toml, pytest.toml, .pytest.toml lub
pytest.ini. Potrafi także ładować zmienne z plików .env.

%prep
%setup -q -n pytest_env-%{version}

%build
%py3_build_pyproject

%if %{with tests}
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
PYTEST_PLUGINS=pytest_mock.plugin \
PYTHONPATH=$(pwd)/src \
%{__python3} -m pytest tests
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py3_install_pyproject

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG.md LICENSE README.md
%{py3_sitescriptdir}/pytest_env
%{py3_sitescriptdir}/pytest_env-%{version}.dist-info
