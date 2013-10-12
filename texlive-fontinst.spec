# revision 29764
# category Package
# catalog-ctan /fonts/utilities/fontinst
# catalog-date 2012-07-06 12:12:34 +0200
# catalog-license lppl
# catalog-version 1.933
Name:		texlive-fontinst
Version:	1.933
Release:	6
Summary:	Help with installing fonts for TeX and LaTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/utilities/fontinst
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fontinst.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fontinst.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fontinst.source.tar.xz
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
%{_texmfdistdir}/scripts/texlive/fontinst.sh
%{_texmfdistdir}/tex/fontinst/base/bbox.sty
%{_texmfdistdir}/tex/fontinst/base/cfntinst.sty
%{_texmfdistdir}/tex/fontinst/base/finstmsc.sty
%{_texmfdistdir}/tex/fontinst/base/fontinst.ini
%{_texmfdistdir}/tex/fontinst/base/fontinst.sty
%{_texmfdistdir}/tex/fontinst/base/multislot.sty
%{_texmfdistdir}/tex/fontinst/base/xfntinst.sty
%{_texmfdistdir}/tex/fontinst/latinetx/8r.etx
%{_texmfdistdir}/tex/fontinst/latinetx/8y.etx
%{_texmfdistdir}/tex/fontinst/latinetx/ot1.etx
%{_texmfdistdir}/tex/fontinst/latinetx/ot1c.etx
%{_texmfdistdir}/tex/fontinst/latinetx/ot1cj.etx
%{_texmfdistdir}/tex/fontinst/latinetx/ot1ctt.etx
%{_texmfdistdir}/tex/fontinst/latinetx/ot1i.etx
%{_texmfdistdir}/tex/fontinst/latinetx/ot1ij.etx
%{_texmfdistdir}/tex/fontinst/latinetx/ot1itt.etx
%{_texmfdistdir}/tex/fontinst/latinetx/ot1j.etx
%{_texmfdistdir}/tex/fontinst/latinetx/ot1tt.etx
%{_texmfdistdir}/tex/fontinst/latinetx/t1.etx
%{_texmfdistdir}/tex/fontinst/latinetx/t1c.etx
%{_texmfdistdir}/tex/fontinst/latinetx/t1cj.etx
%{_texmfdistdir}/tex/fontinst/latinetx/t1i.etx
%{_texmfdistdir}/tex/fontinst/latinetx/t1ij.etx
%{_texmfdistdir}/tex/fontinst/latinetx/t1j.etx
%{_texmfdistdir}/tex/fontinst/latinetx/txtfdmns.etx
%{_texmfdistdir}/tex/fontinst/latinmtx/8r.mtx
%{_texmfdistdir}/tex/fontinst/latinmtx/8y.mtx
%{_texmfdistdir}/tex/fontinst/latinmtx/latin.mtx
%{_texmfdistdir}/tex/fontinst/latinmtx/latinsc.mtx
%{_texmfdistdir}/tex/fontinst/latinmtx/llbuild.mtx
%{_texmfdistdir}/tex/fontinst/latinmtx/lsbuild.mtx
%{_texmfdistdir}/tex/fontinst/latinmtx/lsfake.mtx
%{_texmfdistdir}/tex/fontinst/latinmtx/lsmisc.mtx
%{_texmfdistdir}/tex/fontinst/latinmtx/ltcmds.mtx
%{_texmfdistdir}/tex/fontinst/latinmtx/ltpunct.mtx
%{_texmfdistdir}/tex/fontinst/latinmtx/lubuild.mtx
%{_texmfdistdir}/tex/fontinst/latinmtx/newlatin.mtx
%{_texmfdistdir}/tex/fontinst/latinmtx/resetsc.mtx
%{_texmfdistdir}/tex/fontinst/latinmtx/unsetalf.mtx
%{_texmfdistdir}/tex/fontinst/mathetx/euex.etx
%{_texmfdistdir}/tex/fontinst/mathetx/eufrak.etx
%{_texmfdistdir}/tex/fontinst/mathetx/eurm.etx
%{_texmfdistdir}/tex/fontinst/mathetx/euscr.etx
%{_texmfdistdir}/tex/fontinst/mathetx/msam.etx
%{_texmfdistdir}/tex/fontinst/mathetx/msbm.etx
%{_texmfdistdir}/tex/fontinst/mathetx/oml.etx
%{_texmfdistdir}/tex/fontinst/mathetx/oms.etx
%{_texmfdistdir}/tex/fontinst/mathetx/omx.etx
%{_texmfdistdir}/tex/fontinst/mathetx/rsfs.etx
%{_texmfdistdir}/tex/fontinst/mathmtx/mathex.mtx
%{_texmfdistdir}/tex/fontinst/mathmtx/mathit.mtx
%{_texmfdistdir}/tex/fontinst/mathmtx/mathsy.mtx
%{_texmfdistdir}/tex/fontinst/misc/csc2x.tex
%{_texmfdistdir}/tex/fontinst/misc/csckrn2x.tex
%{_texmfdistdir}/tex/fontinst/misc/glyphbox.mtx
%{_texmfdistdir}/tex/fontinst/misc/glyphoff.mtx
%{_texmfdistdir}/tex/fontinst/misc/glyphon.mtx
%{_texmfdistdir}/tex/fontinst/misc/kernoff.mtx
%{_texmfdistdir}/tex/fontinst/misc/kernon.mtx
%{_texmfdistdir}/tex/fontinst/misc/osf2x.tex
%{_texmfdistdir}/tex/fontinst/smbletx/digit2.etx
%{_texmfdistdir}/tex/fontinst/smbletx/ts1.etx
%{_texmfdistdir}/tex/fontinst/smbletx/ts1i.etx
%{_texmfdistdir}/tex/fontinst/smbletx/ts1ij.etx
%{_texmfdistdir}/tex/fontinst/smbletx/ts1j.etx
%{_texmfdistdir}/tex/fontinst/smblmtx/resetosf.mtx
%{_texmfdistdir}/tex/fontinst/smblmtx/textcomp.mtx
%{_texmfdistdir}/tex/fontinst/smblmtx/unsetnum.mtx
%{_texmfdistdir}/tex/latex/fontinst/fontdoc.sty
%doc %{_texmfdistdir}/doc/fonts/fontinst/README
%doc %{_texmfdistdir}/doc/fonts/fontinst/encspecs/encspecs.tex
%doc %{_texmfdistdir}/doc/fonts/fontinst/encspecs/omxdraft.etx
%doc %{_texmfdistdir}/doc/fonts/fontinst/encspecs/ot1draft.etx
%doc %{_texmfdistdir}/doc/fonts/fontinst/encspecs/t1draft.etx
%doc %{_texmfdistdir}/doc/fonts/fontinst/examples/basic/basicex.tex
%doc %{_texmfdistdir}/doc/fonts/fontinst/examples/basic/basicex2.tex
%doc %{_texmfdistdir}/doc/fonts/fontinst/examples/eurofont/Makefile
%doc %{_texmfdistdir}/doc/fonts/fontinst/examples/eurofont/eurofont.map
%doc %{_texmfdistdir}/doc/fonts/fontinst/examples/eurofont/eurofont.tex
%doc %{_texmfdistdir}/doc/fonts/fontinst/examples/mathptm/Makefile
%doc %{_texmfdistdir}/doc/fonts/fontinst/examples/mathptm/fontptcm.tex
%doc %{_texmfdistdir}/doc/fonts/fontinst/examples/mathptm/mathtest.tex
%doc %{_texmfdistdir}/doc/fonts/fontinst/examples/mathptm/resetsy.mtx
%doc %{_texmfdistdir}/doc/fonts/fontinst/examples/mathptm/unsetmu.mtx
%doc %{_texmfdistdir}/doc/fonts/fontinst/examples/mathptm/zrhax.mtx
%doc %{_texmfdistdir}/doc/fonts/fontinst/examples/mathptm/zrmhax.mtx
%doc %{_texmfdistdir}/doc/fonts/fontinst/examples/mathptm/zrmkern.mtx
%doc %{_texmfdistdir}/doc/fonts/fontinst/examples/mathptm/zrvhax.mtx
%doc %{_texmfdistdir}/doc/fonts/fontinst/examples/mathptm/zryhax.mtx
%doc %{_texmfdistdir}/doc/fonts/fontinst/examples/mathptmx/Makefile
%doc %{_texmfdistdir}/doc/fonts/fontinst/examples/mathptmx/fontptcmx.tex
%doc %{_texmfdistdir}/doc/fonts/fontinst/examples/mathptmx/mathptmx.sty
%doc %{_texmfdistdir}/doc/fonts/fontinst/examples/mathptmx/mathtestx.tex
%doc %{_texmfdistdir}/doc/fonts/fontinst/examples/mathptmx/resetsy.mtx
%doc %{_texmfdistdir}/doc/fonts/fontinst/examples/mathptmx/unsetmu.mtx
%doc %{_texmfdistdir}/doc/fonts/fontinst/examples/mathptmx/zrhax.mtx
%doc %{_texmfdistdir}/doc/fonts/fontinst/examples/mathptmx/zrmhax.mtx
%doc %{_texmfdistdir}/doc/fonts/fontinst/examples/mathptmx/zrmkernx.mtx
%doc %{_texmfdistdir}/doc/fonts/fontinst/examples/mathptmx/zrvhax.mtx
%doc %{_texmfdistdir}/doc/fonts/fontinst/examples/mathptmx/zryhax.mtx
%doc %{_texmfdistdir}/doc/fonts/fontinst/examples/mathptmx/zrykernx.mtx
%doc %{_texmfdistdir}/doc/fonts/fontinst/manual/fontinst.pdf
%doc %{_texmfdistdir}/doc/fonts/fontinst/manual/fontinst.tex
%doc %{_texmfdistdir}/doc/fonts/fontinst/manual/intro98.pdf
%doc %{_texmfdistdir}/doc/fonts/fontinst/manual/intro98.tex
%doc %{_texmfdistdir}/doc/fonts/fontinst/manual/roadmap.eps
%doc %{_texmfdistdir}/doc/fonts/fontinst/talks/et99-font-tables.pdf
%doc %{_texmfdistdir}/doc/fonts/fontinst/talks/et99-font-tutorial.pdf
%doc %{_texmfdistdir}/doc/fonts/fontinst/test/cc-pl.enc
%doc %{_texmfdistdir}/doc/fonts/fontinst/test/comparemetrics.sty
%doc %{_texmfdistdir}/doc/fonts/fontinst/test/comparepls.tex
%doc %{_texmfdistdir}/doc/fonts/fontinst/test/fadrr.mtx
%doc %{_texmfdistdir}/doc/fonts/fontinst/test/multislot-test.tex
%doc %{_texmfdistdir}/doc/fonts/fontinst/test/multislot.etx
%doc %{_texmfdistdir}/doc/fonts/fontinst/test/omsdraft.etx
%doc %{_texmfdistdir}/doc/fonts/fontinst/test/testsc.tex
%doc %{_texmfdistdir}/doc/fonts/fontinst/test/v1901test.mtx
%doc %{_texmfdistdir}/doc/fonts/fontinst/test/v1901test.tex
%doc %{_texmfdistdir}/doc/fonts/fontinst/test/v1902test.tex
%doc %{_texmfdistdir}/doc/fonts/fontinst/test/v1905test.tex
%doc %{_texmfdistdir}/doc/fonts/fontinst/test/v1906test.etx
%doc %{_texmfdistdir}/doc/fonts/fontinst/test/v1906test.mtx
%doc %{_texmfdistdir}/doc/fonts/fontinst/test/v1906test.tex
%doc %{_texmfdistdir}/doc/fonts/fontinst/test/v1913test.tex
%doc %{_texmfdistdir}/doc/fonts/fontinst/test/v1914test.tex
%doc %{_texmfdistdir}/doc/fonts/fontinst/test/v1914testmap.tex
%doc %{_texmfdistdir}/doc/fonts/fontinst/test/v1914testshow.tex
%doc %{_texmfdistdir}/doc/fonts/fontinst/test/v1915test.tex
%doc %{_texmfdistdir}/doc/fonts/fontinst/test/v1915testmap.tex
%doc %{_texmfdistdir}/doc/fonts/fontinst/test/v1916test.mtx
%doc %{_texmfdistdir}/doc/fonts/fontinst/test/v1916test.tex
%doc %{_texmfdistdir}/doc/fonts/fontinst/test/v1916test2.tex
%doc %{_texmfdistdir}/doc/fonts/fontinst/test/v1923test.tex
%doc %{_texmfdistdir}/doc/fonts/fontinst/test/v1927test.tex
%doc %{_texmfdistdir}/doc/fonts/fontinst/test/v1928test.tex
%doc %{_texmfdistdir}/doc/fonts/fontinst/test/v1928test2.tex
%doc %{_texmfdistdir}/doc/fonts/fontinst/test/v1930test.tex
%doc %{_texmfdistdir}/doc/fonts/fontinst/test/v1931test0.tex
%doc %{_texmfdistdir}/doc/fonts/fontinst/test/v1931test1.tex
%doc %{_texmfdistdir}/doc/fonts/fontinst/test/v1931test2.tex
%doc %{_mandir}/man1/fontinst.1*
%doc %{_texmfdistdir}/doc/man/man1/fontinst.man1.pdf
#- source
%doc %{_texmfdistdir}/source/fontinst/base/CHANGES
%doc %{_texmfdistdir}/source/fontinst/base/fibasics.dtx
%doc %{_texmfdistdir}/source/fontinst/base/ficommon.dtx
%doc %{_texmfdistdir}/source/fontinst/base/ficonv.dtx
%doc %{_texmfdistdir}/source/fontinst/base/filtfam.dtx
%doc %{_texmfdistdir}/source/fontinst/base/fimain.dtx
%doc %{_texmfdistdir}/source/fontinst/base/fimapgen.dtx
%doc %{_texmfdistdir}/source/fontinst/base/fisource.dvi
%doc %{_texmfdistdir}/source/fontinst/base/fisource.ist
%doc %{_texmfdistdir}/source/fontinst/base/fisource.sty
%doc %{_texmfdistdir}/source/fontinst/base/fisource.tex
%doc %{_texmfdistdir}/source/fontinst/base/fitrig.dtx
%doc %{_texmfdistdir}/source/fontinst/base/fontinst.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_bindir}
pushd %{buildroot}%{_bindir}
    ln -sf %{_texmfdistdir}/scripts/texlive/fontinst.sh fontinst
popd
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf-dist %{buildroot}%{_datadir}
mkdir -p %{buildroot}%{_mandir}/man1
mv %{buildroot}%{_texmfdistdir}/doc/man/man1/*.1 %{buildroot}%{_mandir}/man1
