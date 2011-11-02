Name:		texlive-lps
Version:	0.7
Release:	1
Summary:	Class for "Logic and Philosophy of Science"
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/lps
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lps.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lps.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lps.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
The 'Logic and Philosophy of Science' journal is an online
publication of the University of Trieste (Italy). The class
builds on the standard article class to offer a format that
LaTeX authors may use when submitting to the journal.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
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
