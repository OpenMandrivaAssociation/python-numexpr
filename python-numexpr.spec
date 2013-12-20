%define	module	numexpr
%define __noautoprov '.*\\.so'

Summary: 	Fast numerical array expression evaluator for Python and NumPy
Name:		python-%{module}
Version:	2.2.2
Release:	4
Source0:	http://numexpr.googlecode.com/files/%{module}-%{version}.tar.gz
License:	MIT
Group:		Development/Python
Url:		http://numexpr.googlecode.com/
BuildRequires:	python-devel
BuildRequires:	python-numpy-devel >= 1.6
BuildRequires:	pkgconfig(lapack)
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3-numpy
BuildRequires:  python-six
BuildRequires:  python3-six
Requires:	python-numpy >= 1.6

%description
The numexpr package evaluates multiple-operator array expressions many
times faster than NumPy can. It accepts the expression as a string,
analyzes it, rewrites it more efficiently, and compiles it to faster
Python code on the fly. It's the next best thing to writing the
expression in C and compiling it with a specialized just-in-time (JIT)
compiler, i.e. it does not require a compiler at runtime.

%package -n python3-%{module}
Summary:        Fast numerical array expression evaluator for Python3 and NumPy
Group:          Development/Python
Requires:       python3-numpy

%description -n python3-%{module}
The numexpr package evaluates multiple-operator array expressions many
times faster than NumPy can. It accepts the expression as a string,
analyzes it, rewrites it more efficiently, and compiles it to faster
Python code on the fly. It's the next best thing to writing the
expression in C and compiling it with a specialized just-in-time (JIT)
compiler, i.e. it does not require a compiler at runtime.

%prep
%setup -qc
sed -i "s|/usr/bin/env |/usr/bin/|" %{module}-%{version}/%{module}/cpuinfo.py

mv %{module}-%{version} python2
cp -a python2 python3

%build
pushd python2
PYTHONDONTWRITEBYTECODE= python setup.py build
popd

pushd python3
PYTHONDONTWRITEBYTECODE= python3 setup.py build
popd

%install
pushd python2
PYTHONDONTWRITEBYTECODE= python setup.py install --root=%{buildroot}
popd

pushd python3
PYTHONDONTWRITEBYTECODE= python3 setup.py install --root=%{buildroot}
popd

%files
%doc python2/ANNOUNCE.txt python2/LICENSE.txt python2/RELEASE_NOTES.txt python2/README.txt
%dir %{py_platsitedir}/%{module}
%{py_platsitedir}/%{module}/*
%{py_platsitedir}/%{module}-*.egg-info

%files -n python3-%{module}
%doc python3/ANNOUNCE.txt python3/LICENSE.txt python3/RELEASE_NOTES.txt python3/README.txt
%dir %{py3_platsitedir}/%{module}
%{py3_platsitedir}/%{module}/*
%{py3_platsitedir}/%{module}-*.egg-info
