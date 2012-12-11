%define	module	numexpr

Summary: 	Fast numerical array expression evaluator for Python and NumPy
Name:		python-%{module}
Version:	2.0.1
Release:	2
Source0:	http://numexpr.googlecode.com/files/%{module}-%{version}.tar.gz
License:	MIT
Group:		Development/Python
Url:		http://numexpr.googlecode.com/
BuildRequires:	python-devel
BuildRequires:	python-numpy-devel >= 1.6
BuildRequires:	pkgconfig(lapack)
Requires:	python-numpy >= 1.6

%description
The numexpr package evaluates multiple-operator array expressions many
times faster than NumPy can. It accepts the expression as a string,
analyzes it, rewrites it more efficiently, and compiles it to faster
Python code on the fly. It's the next best thing to writing the
expression in C and compiling it with a specialized just-in-time (JIT)
compiler, i.e. it does not require a compiler at runtime.

%prep
%setup -q -n %{module}-%{version}

%build
PYTHONDONTWRITEBYTECODE= %__python setup.py build

%install
PYTHONDONTWRITEBYTECODE= %__python setup.py install --root=%{buildroot} --record=FILE_LIST

%files -f FILE_LIST
%doc ANNOUNCE.txt LICENSE.txt RELEASE_NOTES.txt README.txt


%changelog
* Sun Jan 08 2012 Lev Givon <lev@mandriva.org> 2.0.1-1mdv2012.0
+ Revision: 758687
- Update to 2.0.1.

* Sun Nov 27 2011 Lev Givon <lev@mandriva.org> 2.0-1
+ Revision: 733748
- Update to 2.0.

* Fri Feb 04 2011 Lev Givon <lev@mandriva.org> 1.4.2-2
+ Revision: 635880
- Explicitly specify libm when building extension.
- Update to 1.4.2.

* Sat Oct 30 2010 Ahmad Samir <ahmadsamir@mandriva.org> 1.4.1-2mdv2011.0
+ Revision: 590627
- rebuild for python-2.7
- drop the obsolete %%py_require macro and replace it with python-devel BR

* Wed Oct 20 2010 Lev Givon <lev@mandriva.org> 1.4.1-1mdv2011.0
+ Revision: 587009
- Update to 1.4.1.

* Sun Aug 01 2010 Lev Givon <lev@mandriva.org> 1.4-1mdv2011.0
+ Revision: 564875
- Update to 1.4.

* Tue Jul 13 2010 Lev Givon <lev@mandriva.org> 1.3.1-1mdv2011.0
+ Revision: 551335
- import python-numexpr

