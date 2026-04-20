BUILD_DIR = build
BOOK_SRC = tex/book.tex
BOOK_BUILD_PDF = tex/book.pdf
BOOK_ROOT_PDF = ml-by-design.pdf
LATEXMK = latexmk -norc -cd -pdf -interaction=nonstopmode
BUILD_AUX = tex/book.aux tex/book.bbl tex/book.blg tex/book.fdb_latexmk tex/book.fls tex/book.log tex/book.out tex/book.toc

.PHONY: all book clean distclean

all: book

book:
	mkdir -p $(BUILD_DIR)
	$(LATEXMK) $(BOOK_SRC)
	cp -f $(BOOK_BUILD_PDF) $(BOOK_ROOT_PDF)
	rm -f $(BUILD_AUX) $(BOOK_BUILD_PDF)

clean:
	rm -f $(BUILD_AUX)
	rm -f book.aux book.bbl book.blg book.fdb_latexmk book.fls book.log book.out book.toc
	rm -f book.pdf tex/book.pdf
	rm -f tex/book.aux tex/book.bbl tex/book.blg tex/book.fdb_latexmk tex/book.fls tex/book.log tex/book.out tex/book.toc
	rm -f test-bib.tex test-bib.pdf test-bib.log
	rm -f ch03.log ch11.log
	rm -f tmp*.tmp *.backup
	rm -f .bbl-setup .~lock*

distclean: clean
	rm -f $(BOOK_ROOT_PDF) $(BOOK_BUILD_PDF) book.pdf
