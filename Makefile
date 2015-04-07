.PHONY: docs all clean

all: docs 

docs: 
	$(MAKE) -C docs
clean:
	$(MAKE) --directory=docs clean;

