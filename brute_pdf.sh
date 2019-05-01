crunch 6 10 -f /usr/share/crunch/charset.lst mixalpha-numeric | while read -r L; do
	qpdf --password=$L --decrypt Anima-Arcana.pdf Anima-Arcana2.pdf && echo $L > pass.txt
done;