# DetyraNePython_Grupi_19

## AES

AES eshte nje block cipher simetrik, i perdorur nga qeveria Amerikane per te mbrojtur informacione te klasifikuara. Block cipher eshte nje metode enkriptimi qe perdor nje algoritem te caktuar, i cili perdor nje celes simetrik per te enkriptuar nje bllok teksti.AES, enkripton 128 bit blloqe me nje celes, me gjatesi te paracaktuar: 128, 192 apo 256 bita. Kemi tre menyre per enkriptim me AES: AES-128, AES-192 and AES-256. <br/>

AES-128 perdor 128-bit gjatesi te celesit, AES-192 perdor 192 bit, derisa AES-256 perdor 256 bit. Te dhenat enkriptohen ne blloqe 128 biteshe, duke perdorur celesa kryptografik te gjatesive 128, 192 dhe 256 bit.AES eshte algoritem simetrik. Kjo do te thote se ky algoritem perdor te njejtin celes sekret si per enkriptim, ashtu edhe per dekriptim. Jane 10 raunde per 128-bit celesat, 12 raunde per 192-bit celesat dhe 14 raunde per 256-bit celesat.Nje raund konsiston ne disa hapa procesues si, substitution, transposition dhe procese tjera, ne menyre qe plainteksti te transformohet ne ciphertekst. AES nuk eshte thyer ndonjehere deri me tani , pra eshte i sigurt ndaj qfaredo sulmi brute-force.Sidoqofte , madhesia e qelesit i cili perdoret per enkriptim duhet te jete mjaftueshem i gjate qe te mos mund te thyhet(crack) edhe nga super kompjuteret qe mund te gjenden sot. 


**Kemi mode te ndryshme te enkriptimit me algoritmin AES, disa prej tyre jane:** 
 * __*ECB*__ : Electronic Code Book mode
 * __*CBC*__ : Cipher Block Chaining mode.
 * __*CFB*__ : Cipher FeedBack mode.
 * __*OFB*__ : Output FeedBack mode.
 * __*CTR*__ : Counter mode.

   

Aplikacioni yne eshte zhvilluar ne gjuhen programuese __*Python*__, dhe eshte punuar si __*GUI(Graphical User Interface)*__ duke perdorur modulin __*tkinter*__.
Kodi burimor gjendet ne fajllin aes_gui.py – ku edhe jane shqyrtuar rastet e enkriptimit me AES. Pershkrimi i punes dhe ekzkutimi i ketyre enkriptimeve eshte bere me poshte. 
