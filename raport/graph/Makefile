%.png: %.dot
	dot $< -Tpng -o $@

all:
	$(addsuffix .png, $(basename $(wildcard *.dot)))

clean:
	rm -fv *.pdf
