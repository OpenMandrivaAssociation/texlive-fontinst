Name:		texlive-fontinst
Version:	62517
Release:	2
Summary:	Help with installing fonts for TeX and LaTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/utilities/fontinst
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fontinst.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fontinst.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fontinst.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Provides:	texlive-fontinst.bin = %{EVRD}

%description
TeX macros for converting Adobe Font Metric files to TeX metric
and virtual font format. Fontinst helps mainly with the number
crunching and shovelling parts of font installation. This means
in practice that it creates a number of files which give the
TeX metrics (and related information) for a font family that
(La)TeX needs to do any typesetting in these fonts. Fontinst
furthermore makes it easy to create fonts containing glyphs
from more than one base font, taking advantage of (e.g.)
"expert" font sets. Fontinst cannot examine files to see if
they contain any useful information, nor automatically search
for files or work with binary file formats; those tasks must
normally be done manually or with the help of some other tool,
such as the pltotf and vptovf programs.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_bindir}/fontinst
%{_texmfdistdir}/scripts/texlive-extra/fontinst.sh
%{_texmfdistdir}/tex/fontinst
%{_texmfdistdir}/tex/latex/fontinst
%doc %{_texmfdistdir}/doc/fonts/fontinst
%doc %{_mandir}/man1/fontinst.1*
%doc %{_texmfdistdir}/doc/man/man1/fontinst.man1.pdf
#- source
%doc %{_texmfdistdir}/source/fontinst

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_bindir}
pushd %{buildroot}%{_bindir}
ln -sf %{_texmfdistdir}/scripts/texlive-extra/fontinst.sh fontinst
popd
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf-dist %{buildroot}%{_datadir}
mkdir -p %{buildroot}%{_mandir}/man1
mv %{buildroot}%{_texmfdistdir}/doc/man/man1/*.1 %{buildroot}%{_mandir}/man1
