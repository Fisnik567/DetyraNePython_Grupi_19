# DetyraNePython_Grupi_19

## AES - Advanced Encryption Standard

AES eshte nje block cipher simetrik, i perdorur nga qeveria Amerikane per te mbrojtur informacione te klasifikuara. Block cipher eshte nje metode enkriptimi qe perdor nje algoritem te caktuar, i cili perdor nje celes simetrik per te enkriptuar nje bllok teksti. AES, enkripton 128 bit blloqe me nje celes, me gjatesi te paracaktuar: 128, 192 apo 256 bita. Kemi tre menyra per enkriptim me AES: AES-128, AES-192 and AES-256. <br/>

AES-128 perdor 128-bit gjatesi te celesit, AES-192 perdor 192 bit, derisa AES-256 perdor 256 bit. Te dhenat enkriptohen ne blloqe 128 biteshe, duke perdorur celesa kryptografik te gjatesive 128, 192 dhe 256 bit. AES eshte algoritem simetrik. Kjo do te thote se ky algoritem perdor te njejtin celes sekret si per enkriptim, ashtu edhe per dekriptim. Jane 10 raunde per 128-bit celesat, 12 raunde per 192-bit celesat dhe 14 raunde per 256-bit celesat. Nje raund konsiston ne disa hapa procesues si, substitution, transposition dhe procese tjera, ne menyre qe plainteksti te transformohet ne ciphertekst. AES nuk eshte thyer ndonjehere deri me tani, pra eshte i sigurt ndaj cfaredo sulmi brute-force. Sidoqofte, madhesia e qelesit i cili perdoret per enkriptim duhet te jete mjaftueshem i gjate qe te mos mund te thyhet(crack) edhe nga super kompjuteret qe mund te gjenden sot. 


**Kemi mode te ndryshme te enkriptimit me algoritmin AES, disa prej tyre jane:** 
 * __*ECB*__ : Electronic Code Book mode
 * __*CBC*__ : Cipher Block Chaining mode.
 * __*CFB*__ : Cipher FeedBack mode.
 * __*OFB*__ : Output FeedBack mode.
 * __*CTR*__ : Counter mode.

   

Aplikacioni yne eshte zhvilluar ne gjuhen programuese __*Python*__, dhe eshte punuar si __*GUI(Graphical User Interface)*__ duke perdorur modulin __*tkinter*__.
Kodi burimor gjendet ne fajllin aes_gui.py – ku edhe jane shqyrtuar rastet e enkriptimit me AES. Pershkrimi i punes dhe ekzekutimi i ketyre enkriptimeve eshte bere me poshte. 

**Modet qe ne kemi shqyrtuar dhe implementuar jane ECB Mode dhe CFB Mode.**

__*Electronic Code Book*__ përdor tekniken me te thjeshte, duke e bërë atë një nga algoritmat më të lehtë dhe më të shpejtë për t’u zbatuar. Teksti i hyrjes(plaintext) ndahet në një numër blloqesh dhe secili enkriptohet individualisht duke përdorur çelësin. Enkriptimi i të njëjtit bllok dy herë do të rezultojë në kthimin e të njëjtit tekst dales(ciphertext) dy herë.

__*Cipher FeedBack*__ eshte nje nga metodat e enkriptimit te ciles i nevojitet nje vektor inicializues(IV) per te kryer procesin e enkriptimit. Së pari, CFB do të enkriptojë IV, pastaj do të xor me bllokun e pare te teksit hyres(plaintext) për të marrë tekstin e enkriptuar. Ky rezultat I enkriptimit behet perseri  xor me bllokun e dyte te plaintext. Kjo mënyrë do te vazhdoje derisa te perfshihet i gjithe teksti hyres. Eshte metode me e sigurte se EBC sepse sulmuesit nuk mund ti krahasojne ciphertext-et. <br/> <br/>

Ne vazhdim jane paraqitur rezultatet e enkriptimit me AES, si dhe forma e implementimit.<br/><br/>
__*Enkriptimi me gjatesi te celesit 128 bit:*__<br/><br/>
<img src="Images/128bit_encryption.PNG" width="650">
<br/> <br/>
__*Enkriptimi me gjatesi te celesit 192 bit:*__<br/><br/>
<img src="Images/192bit_encryption.PNG" width="650">


<br/> <br/>
__*Enkriptimi me gjatesi te celesit 256 bit:*__<br/><br/>
<img src="Images/256bit_encryption.PNG" width="650">

<br/><br/>
Ne vazhdim jane paraqitur rastet, kur nuk eshte dhene si input gjatesia e duhur e celesit.<br/><br/>

__*Rasti 1:*__<br/><br/>
<img src="Images/128bit_encryptionProblem.PNG" width="650">
<br/> <br/>
__*Rasti 2:*__<br/><br/>
<img src="Images/192bit_encryptionProblem.PNG" width="650">


<br/> <br/>
__*Rasti 3:*__<br/><br/>
<img src="Images/256bit_encryptionProblem.PNG" width="650">

<br/><br/>

## Konkluzion
Si konkluzion, mund te themi se AES eshte nje algoritem mjaft i perdorur ne ditet e sotme. AES eshte i implementuar ne software dhe hardware ne tere boten, per te enkriptuar dhe mbrojtur te dhena sensitive. Eshte algoritem esencial per sigurine e kompjutereve te qeverive, cybersecurity dhe mbrojtjen e te dhenave elektronike.



