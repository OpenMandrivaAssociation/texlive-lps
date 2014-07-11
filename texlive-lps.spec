# revision 21322
# category Package
# catalog-ctan /macros/latex/contrib/lps
# catalog-date 2011-02-03 16:11:01 +0100
# catalog-license lppl
# catalog-version 0.7
Name:		texlive-lps
Version:	0.7
Release:	8
Summary:	Class for "Logic and Philosophy of Science"
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/lps
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lps.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lps.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lps.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The 'Logic and Philosophy of Science' journal is an online
publication of the University of Trieste (Italy). The class
builds on the standard article class to offer a format that
LaTeX authors may use when submitting to the journal.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/lps/lps.cls
%doc %{_texmfdistdir}/doc/latex/lps/README
%doc %{_texmfdistdir}/doc/latex/lps/lps.pdf
%doc %{_texmfdistdir}/doc/latex/lps/lpstemplate.tex
#- source
%doc %{_texmfdistdir}/source/latex/lps/lps.dtx
%doc %{_texmfdistdir}/source/latex/lps/lps.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.7-2
+ Revision: 753459
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 0.7-1
+ Revision: 718882
- texlive-lps
- texlive-lps
- texlive-lps
- texlive-lps

