%define		pkg	json-stringify-safe
Summary:	Like JSON.stringify, but doesn't blow up on circular refs
Name:		nodejs-%{pkg}
Version:	5.0.0
Release:	1
License:	BSD
Group:		Development/Libraries
Source0:	http://registry.npmjs.org/%{pkg}/-/%{pkg}-%{version}.tgz
# Source0-md5:	197b319fb2d2772f4830c8443e57faba
URL:		https://github.com/isaacs/json-stringify-safe
BuildRequires:	rpmbuild(macros) >= 1.634
Requires:	nodejs
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Like JSON.stringify, but doesn't blow up on circular refs.

%prep
%setup -qc
mv package/* .

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{nodejs_libdir}/%{pkg}
cp -pr stringify.js package.json $RPM_BUILD_ROOT%{nodejs_libdir}/%{pkg}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md
%{nodejs_libdir}/%{pkg}
