.PHONY: all clean graph

all: raport.pdf 

# MAIN LATEXMK RULE
#
# # -pdf tells latexmk to generate PDF directly (instead of DVI).
# # -pdflatex="" tells latexmk to call a specific backend with specific options.
# # -use-make tells latexmk to call make for generating missing files.
#
# # -interactive=nonstopmode keeps the pdflatex backend from stopping at a
# # missing file reference and interactively asking you for an alternative.

raport.pdf: raport.tex graph
	latexmk -quiet -f -pdf -pdflatex="pdflatex -interactive=nonstopmode" -use-make raport.tex

graph/%.pdf: graph/%.dot
	neato $< -Tpdf -o $@
		
clean:
	latexmk -CA;
	make --directory=graph clean;

