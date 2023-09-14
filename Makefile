DIR2WEBSITE := $(HOME)/projets/perso/strayMat.gitlab.io/source/_static/files/

.PHONY: cp-thesis
cp-thesis:
	cp thesis.pdf $(DIR2WEBSITE)

.PHONY: zip-thesis
zip-thesis:
	zip -r thesis_zipped img/ references.bib thesis.tex

?PHONY: extract-french
extract-french:
	 pdftk thesis.pdf cat 26-29 output materials/resume_francais.pdf