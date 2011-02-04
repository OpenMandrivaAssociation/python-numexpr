%define	module	numexpr
%define name	python-%{module}
%define version	1.4.2
%define release	%mkrel 2

Summary: 	Fast numerical array expression evaluator for Python and NumPy
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	http://numexpr.googlecode.com/files/%{module}-%{version}.tar.gz
Patch0:		setup-lm.patch
License:	MIT
Group:		Development/Python
Url:		http://numexpr.googlecode.com/
BuildRoot: 	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	python-devel
BuildRequires:	python-numpy-devel >= 1.0
Requires:	python-numpy >= 1.0

%description
The numexpr package evaluates multiple-operator array expressions many
times faster than NumPy can. It accepts the expression as a string,
analyzes it, rewrites it more efficiently, and compiles it to faster
Python code on the fly. It's the next best thing to writing the
expression in C and compiling it with a specialized just-in-time (JIT)
compiler, i.e. it does not require a compiler at runtime.

%prep
%setup -q -n %{module}-%{version}
%patch0 -p0 

%build
PYTHONDONTWRITEBYTECODE= %__python setup.py build

%install
%__rm -rf %{buildroot}
PYTHONDONTWRITEBYTECODE= %__python setup.py install --root=%{buildroot} --record=FILE_LIST

%clean
%__rm -rf %{buildroot}

%files -f FILE_LIST
%defattr(-,root,root)
%doc ANNOUNCE.txt LICENSE.txt RELEASE_NOTES.txt README.txt
