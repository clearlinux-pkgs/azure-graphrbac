#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : azure-graphrbac
Version  : 0.61.1
Release  : 6
URL      : https://files.pythonhosted.org/packages/52/31/87dd867c239b5b2c5bccade8a0fd81c28b9b380ece3db47b58ae05270842/azure-graphrbac-0.61.1.zip
Source0  : https://files.pythonhosted.org/packages/52/31/87dd867c239b5b2c5bccade8a0fd81c28b9b380ece3db47b58ae05270842/azure-graphrbac-0.61.1.zip
Summary  : Microsoft Azure Graph RBAC Client Library for Python
Group    : Development/Tools
License  : MIT
Requires: azure-graphrbac-python = %{version}-%{release}
Requires: azure-graphrbac-python3 = %{version}-%{release}
Requires: azure-nspkg
Requires: msrest
Requires: msrestazure
BuildRequires : azure-common
BuildRequires : azure-nspkg
BuildRequires : buildreq-distutils3
BuildRequires : msrest
BuildRequires : msrestazure

%description
==============================
        
        This is the Microsoft Azure Graph RBAC Client Library.
        
        This package has been tested with Python 2.7, 3.4, 3.5, 3.6 and 3.7.

%package python
Summary: python components for the azure-graphrbac package.
Group: Default
Requires: azure-graphrbac-python3 = %{version}-%{release}

%description python
python components for the azure-graphrbac package.


%package python3
Summary: python3 components for the azure-graphrbac package.
Group: Default
Requires: python3-core
Provides: pypi(azure_graphrbac)
Requires: pypi(azure_common)
Requires: pypi(msrest)
Requires: pypi(msrestazure)

%description python3
python3 components for the azure-graphrbac package.


%prep
%setup -q -n azure-graphrbac-0.61.1
cd %{_builddir}/azure-graphrbac-0.61.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1588694801
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
