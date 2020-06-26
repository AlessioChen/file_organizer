# FILE ORFANIZER 

### STEP_1
Semplice progetto che inizia creando, in un notebook, uno script Python che iteri in ordine alfabetico sui file della cartella files e, a seconda del tipo (audio, documento, immagine), li sposti nella relativa sottocartella.
Se la sottocartella non esiste, lo script lo crea automaticamente.

Durante il ciclo, lo script stampa le informazioni dei file: nome, tipo e dimensione in byte. Questo è l'output desiderato:
bw type:image size:94926B
ciao type:doc size:12B
daffodil type:image size:24657B
pippo type:doc size:8299B
song1 type:audio size:1087849B
song2 type:audio size:764176B
trump type:image size:10195B

Oltre a stamparne le informazioni via via che li sposto, tengo traccia dei file creando un documento *recap.csv* con le stesse informazioni.

La struttura finale della cartella files dovrà essere:

        - files            
            - audio
                - song1.mp3
                - song2.mp3
            - docs
                - ciao.txt
                - pippo.odt
            - images
                - bw.png
                - daffodil.jpg
                - trump.jpeg    
            - recap.csv
### STEP_3
Una immagine in scala di grigio ha un solo livello di colore, una RGB ne ha 3, una RGBA 4 (l'ultimo è detto canale *alpha*).

Il modulo *Image* della libreria *PIL* permette di caricare un'immagine, che può essere trasformata in un array NumPy attraverso la funzione *np.array*. A partire da tale array, è possibile capire se l'immagine caricata è in scala di grigio, RGB o RGBA.

Lo scirt itera sulla sottocartella *images* e costruisce una tabella riassuntiva (prodotta con la libreria *tabulate*): 
Oltre al nome del file, la tabella riporta:

- altezza dell'immagine, in pixel
- larghezza dell'immagine, in pixel
- se l'immagine è in scala di grigio, la colonna grayscale indica la media dei valori dell'unico livello di colore
- se l'immagine è a colori, le altre colonne indicano la media dei valori di ogni livello di colore.