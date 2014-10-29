%define	module	numexpr
%define __noautoprov '.*\\.so'

Summary: 	Fast numerical array expression evaluator for Python and NumPy
Name:		python-%{module}
Version:	2.4
Release:	1
Source0:	https://pypi.python.org/packages/source/n/numexpr/numexpr-%{version}.tar.gz
License:	MIT
Group:		Development/Python
Url:		http://numexpr.googlecode.com/
BuildRequires:	python-devel
BuildRequires:	python-numpy
BuildRequires:	python-numpy-devel >= 1.6
BuildRequires:	pkgconfig(lapack)
BuildRequires:  python-six
Requires:	python-numpy >= 1.6

%description
The numexpr package evaluates multiple-operator array expressions many
times faster than NumPy can. It accepts the expression as a string,
analyzes it, rewrites it more efficiently, and compiles it to faster
Python code on the fly. It's the next best thing to writing the
expression in C and compiling it with a specialized just-in-time (JIT)
compiler, i.e. it does not require a compiler at runtime.


%prep
%setup -qn %{module}-%{version}
sed -i "s|/usr/bin/env |/usr/bin/|" %{module}/cpuinfo.py

%build
PYTHONDONTWRITEBYTECODE= python setup.py build

%install
PYTHONDONTWRITEBYTECODE= python setup.py install --root=%{buildroot}

%files
%doc ANNOUNCE.txt LICENSE.txt RELEASE_NOTES.txt README.txt
%dir %{py_platsitedir}/%{module}
%{py_platsitedir}/%{module}/*
%{py_platsitedir}/%{module}-*.egg-info


