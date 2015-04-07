%.pdf: %.dot
	neato $< -Tpdf -o $@

all: 
	$(addsuffix .pdf, $(basename $(wildcard *.dot)))

clean:
	rm -v *.pdf
