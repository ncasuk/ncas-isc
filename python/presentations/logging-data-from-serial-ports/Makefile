#!/bin/sh
LANG=en_GB
AUTHORS=Dan Walker
PUBLISHER=National Centre for Atmospheric Science

%_Slides.pdf: %_Slides.tex 
	#LANG=${LANG} ebook-convert $< $(basename $@)-temp.pdf --page-breaks-before="//h:h1" --unit="millimeter" --custom-size=297x210 --extra-css="centred.css" --language=${LANG} --authors="${AUTHORS}" --publisher="${PUBLISHER}" --sr1-search='/attachments/download/[0-9]+/' --sr1-replace='' --sr2-search=' <sub>' --sr2-replace='<sub>'
	#pdftk $(basename $@)-temp.pdf multibackground ncas_ppt_template.pdf output $@
	xelatex --shell-escape $<
	xelatex --shell-escape $<

%.pdf: %.html handout.css
	LANG=${LANG} ebook-convert $< $(basename $@)-temp.pdf --page-breaks-before="//h:h1" --unit="millimeter" --custom-size=210x297 --extra-css="handout.css" --language=${LANG} --authors="${AUTHORS}" --publisher="${PUBLISHER}" --margin-left 28 --margin-right 28 --page-breaks-before='//*[@class="page"]' 
	pdftk $(basename $@)-temp.pdf multibackground NCAS-handouts-background.pdf output $@
