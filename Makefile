.PHONY: teoria.pdf all clean

all: teoria.pdf 

# MAIN LATEXMK RULE
#
# # -pdf tells latexmk to generate PDF directly (instead of DVI).
# # -pdflatex="" tells latexmk to call a specific backend with specific options.
# # -use-make tells latexmk to call make for generating missing files.
#
# # -interactive=nonstopmode keeps the pdflatex backend from stopping at a
# # missing file reference and interactively asking you for an alternative.

teoria.pdf: ./docs/teoria.tex
	cd docs; latexmk -f -pdf -pdflatex="pdflatex -interactive=nonstopmode" -use-make teoria.tex

clean:
	cd docs; latexmk -CA

