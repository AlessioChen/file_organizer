#FILE ORFANIZER 

###STEP_1
Semplice progetto che Inizia creando, in un notebook, uno script Python che iteri in ordine alfabetico sui file della cartella files e, a seconda del tipo (audio, documento, immagine), li sposti nella relativa sottocartella (qui sotto trovi un esempio). Se la sottocartella non esiste, il tuo script dovrà crearla automaticamente.

Durante il ciclo, lo script deve stampare le informazioni dei file: nome, tipo e dimensione in byte. Questo è l'output desiderato:
bw type:image size:94926B
ciao type:doc size:12B
daffodil type:image size:24657B
pippo type:doc size:8299B
song1 type:audio size:1087849B
song2 type:audio size:764176B
trump type:image size:10195B

Oltre a stamparne le informazioni via via che li sposti, tieni traccia dei file creando un documento *recap.csv* con le stesse informazioni. Trovi un esempio in questa cartella.

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
###STEP_3
Una immagine in scala di grigio ha un solo livello di colore, una RGB ne ha 3, una RGBA 4 (l'ultimo è detto canale *alpha*).

Il modulo *Image* della libreria *PIL* permette di caricare un'immagine, che può essere trasformata in un array NumPy attraverso la funzione *np.array*. A partire da tale array, è possibile capire se l'immagine caricata è in scala di grigio, RGB o RGBA.

Aggiungi al notebook dello Step 1 uno script che iteri sulla sottocartella *images* e costruisca una tabella riassuntiva come questa (prodotta con la libreria *tabulate*):
 ╒══════════╤══════════╤═════════╤═════════════╤════════╤═══════╤═══════╤═════════╕
│ name     │   height │   width │   grayscale │      R │     G │     B │   ALPHA │
╞══════════╪══════════╪═════════╪═════════════╪════════╪═══════╪═══════╪═════════╡
│ bw       │      512 │     512 │       21.48 │   0.00 │  0.00 │  0.00 │       0 │
├──────────┼──────────┼─────────┼─────────────┼────────┼───────┼───────┼─────────┤
│ daffodil │      500 │     335 │        0.00 │ 109.25 │ 85.56 │  4.97 │       0 │
├──────────┼──────────┼─────────┼─────────────┼────────┼───────┼───────┼─────────┤
│ trump    │      183 │     275 │        0.00 │  97.01 │ 98.99 │ 90.92 │       0 │
╘══════════╧══════════╧═════════╧═════════════╧════════╧═══════╧═══════╧═════════╛               
Oltre al nome del file, la tabella riporta:

- altezza dell'immagine, in pixel
- larghezza dell'immagine, in pixel
- se l'immagine è in scala di grigio, la colonna grayscale indica la media dei valori dell'unico livello di colore
- se l'immagine è a colori, le altre colonne indicano la media dei valori di ogni livello di colore.