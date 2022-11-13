Name:		texlive-lps
Version:	21322
Release:	1
Summary:	Class for "Logic and Philosophy of Science"
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/lps
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lps.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lps.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lps.source.r%{version}.tar.xz
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
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
