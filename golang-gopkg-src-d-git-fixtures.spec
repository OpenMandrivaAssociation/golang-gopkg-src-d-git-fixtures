%global goipath         gopkg.in/src-d/go-git-fixtures.v3
%global forgeurl        https://github.com/src-d/go-git-fixtures
%global api             3
Version:                %{api}.1.0

%global common_description %{expand:
Git repository fixtures being used by go-git.}

%gometa

Name:    golang-gopkg-src-d-git-fixtures
Release: 2%{?dist}
Summary: Several git fixtures to run go-git tests
License: ASL 2.0
URL:     %{gourl}
Source:  %{gosource}

%description
%{common_description}

%package %{api}-devel
Summary:    %{summary}
BuildArch:  noarch

%description %{api}-devel
%{common_description}
 
This package contains the source code needed for building packages that import
the %{goipath} Go namespace.

%prep
%gosetup -q

%install
%goinstall
cp -pr data %{buildroot}%{gopath}/src/%{goipath}

%check
%gochecks

%files %{api}-devel -f devel.file-list
%doc README.md
%{gopath}/src/%{goipath}/data

%changelog
* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Apr 03 2018 Dominik Mierzejewski <dominik@greysector.net> - 3.1.0-1
- First package for Fedora
