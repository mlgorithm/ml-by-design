LATEXMK = latexmk -cd -pdf -interaction=nonstopmode -halt-on-error -outdir=..

.PHONY: all book cover full-cover

all: book cover full-cover

book:
	$(LATEXMK) tex/book.tex
	cp book.pdf ml-by-design.pdf

cover:
	$(LATEXMK) tex/cover.tex

full-cover:
	$(LATEXMK) tex/full-cover.tex
