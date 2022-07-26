# OpenGate_WhenYouRecognizelicenseplate_withRPI
Raspberry Pi: apertura cancello su riconoscimento targa

Materiale da utilizzare

Raspberry Pi
* Raspberry Pi Camera
* SG90

Per chi utilizzasse per la prima volta la Raspberry Pi Camera leggendo questo articolo sarete in grado di configurarla da zero: Come installare e configurare la Raspberry Pi Camera

TI invito a leggere anche l’articolo precedente sul [bot e sul riconoscimento di targhe](https://github.com/SimoneMoreWare/LettoreTarghe_bot_and_raspberry):

Ecco un pinout del sg90

![alt text](https://i0.wp.com/www.moreware.org/wp/wp-content/uploads/2022/02/fa19a830e604aaa2ac71ea4005534440.jpg?w=631&ssl=1)

Ecco un diagramma di collegamento

![alt text](https://i0.wp.com/www.moreware.org/wp/wp-content/uploads/2022/02/GPIOWiringDiagram.png?w=584&ssl=1)

# Installazione

Dobbiamo installare poi varie librerie tra cui:

* open cv
* Tesseract 
* imutils

Ci sono tre passaggi logici fondamentali

* Rilevamento targa
* Segmentazione dei caratteri una volta rilevata la targa
* Riconoscimento dei caratteri con OCR
* Installazioni librerie

Aggiorniamo il Raspberry digitando il seguente comando nel terminale:

`sudo apt-get update`

Usa i seguenti comandi per installare le dipendenze necessarie per l’installazione di OpenCV sul tuo Raspberry Pi.

`sudo apt install libhdf5-dev -y 
sudo apt install libhdf5-serial-dev –y 
sudo apt install libatlas-base-dev –y 
sudo apt install libjasper-dev -y 
sudo apt install libqtgui4 –y 
sudo apt install libqt4-test –y`

Successivamente, usa il comando seguente per installare OpenCV sul tuo Raspberry Pi.

`pip3 install opencv-contrib-python==4.1.0.25`

Per installare Tesseract OCR (Optical Character Recognition) utilizzando l’opzione apt:

`sudo apt install tesseract-ocr`

installa pytesseract con il comando:

`pip3 install pytesseract`

imutils viene utilizzato per semplificare le funzioni di elaborazione delle immagini essenziali come traduzione, rotazione, ridimensionamento e visualizzazione di immagini Matplotlib con OpenCV. Utilizzare il comando seguente per installare imutils:

`pip3 install imutils`

# [Codice](https://github.com/SimoneMoreWare/OpenGate_WhenYouRecognizelicenseplate_withRPI/blob/main/script.py)

Avvia il codice, se la targa letta è uguale a quella di riferimento il servomotore si muove

I risultati di questo metodo non saranno accurati . La precisione dipende dalla chiarezza dell’immagine, dall’orientamento, dall’esposizione alla luce e così via.

Video

https://www.youtube.com/watch?v=EtdBzivfbr8

