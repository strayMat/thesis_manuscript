DIR2WEBSITE := $(HOME)/projets/perso/strayMat.gitlab.io/source/_static/files/

.PHONY: cp-thesis
cp-thesis:
	cp thesis.pdf $(DIR2WEBSITE)

.PHONY: zip-thesis
zip-thesis:
	zip -r thesis_zipped img/ references.bib thesis.tex

