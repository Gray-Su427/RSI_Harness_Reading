# =====================================================================
# Makefile — LaTeX 报告编译
#
# 需要 latexmk (TeX Live / MiKTeX 自带)。
# Windows 用户若无 make，请直接用 build.bat。
#
#   make          编译
#   make clean    清理中间文件
#   make view     编译并打开 PDF
# =====================================================================

LATEXMK ?= latexmk
MAIN    ?= main

.DEFAULT_GOAL := all

.PHONY: all clean view distclean bib

all: $(MAIN).pdf

$(MAIN).pdf: $(MAIN).tex preamble.tex
	$(LATEXMK) -pdf -interaction=nonstopmode -file-line-error $(MAIN).tex

# 仅重跑 bibtex + 两遍 pdflatex（main.tex 改动后不需要）
bib: $(MAIN).bbl

$(MAIN).bbl: ../refs/refs.bib $(MAIN).tex
	cd $(CURDIR) && bibtex $(MAIN) || true
	$(LATEXMK) -pdf -interaction=nonstopmode -file-line-error $(MAIN).tex

view: $(MAIN).pdf
	@echo "open $(MAIN).pdf"

clean:
	-$(LATEXMK) -c $(MAIN).tex

distclean:
	-$(LATEXMK) -C $(MAIN).tex
