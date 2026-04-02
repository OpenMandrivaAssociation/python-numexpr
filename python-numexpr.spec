%define module numexpr

Name:		python-numexpr
Summary: 	Fast numerical array expression evaluator for Python and NumPy
Version:	2.14.1
Release:	1
License:	MIT
Group:		Development/Python
URL:		https://github.com/pydata/numexpr
Source0:	%{URL}/archive/v%{version}/%{name}-%{version}.tar.gz
Source100:	%{name}.rpmlintrc

BuildSystem:	python
BuildRequires:	pkgconfig(python3)
BuildRequires:	python%{pyver}dist(numpy)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(wheel)

%description
The numexpr package evaluates multiple-operator array expressions many
times faster than NumPy can. It accepts the expression as a string,
analyzes it, rewrites it more efficiently, and compiles it to faster
Python code on the fly. It's the next best thing to writing the
expression in C and compiling it with a specialized just-in-time (JIT)
compiler, i.e. it does not require a compiler at runtime.

%build -p
export LDFLAGS="%{ldflags} -lpython%{pyver}"

%files
%doc README.rst site.cfg.example
%license LICENSE.txt
%{python_sitearch}/%{module}
%{python_sitearch}/%{module}-%{version}.dist-info
