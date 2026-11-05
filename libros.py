"""Tus libros y géneros. Este es el archivo que editás cada vez que leés algo nuevo."""

GENRES = {
    "romantasy": {"es": "Romantasy", "pt": "Romantasy"},
    "fantasy": {"es": "Fantasía", "pt": "Fantasia"},
    "romance": {"es": "Romance", "pt": "Romance"},
    "thriller": {"es": "Thriller", "pt": "Suspense"},
}
# Playlist general del inicio: pegá el link de Spotify entre las comillas ("" = no se muestra)
PLAYLIST_GENERAL = "https://open.spotify.com/playlist/6bxWTEcz78pzw1xcrRBtRD?si=d99c20575d80457e"
# Tus libros. "id" es el nombre que aparece en el link (sin espacios ni tildes).
# "cover" es la portada: una ruta como "portadas/fourth-wing.jpg" o None si todavía no la tenés.
BOOKS = [
    {
        "id": "AssistenteVillano",
        "title": "Assistant to the Villain",
        "author": "Hanna Nicole Maehrer",
        "genre": "romantasy",
        "stars": 5,
        "cover": "C:\\Users\\jacqu\\Blog-Book\\portadas\\assistentedelvillano.jpg",
        "summary": {
            "es": "Que pasaria si conseguir trabajo con el villano mas temido del reino terminara siendo la mejor decision de tu vida?",
            "pt": "E se conseguir um emprego com o vilão mais temido do reino acabasse sendo a melhor decisão da sua vida?",
        },
        "review": {
            "es": "El libro que me saco del bloqueo de lectura. LEAN TODO, del primer libro hasta el ultimo, no se van a repentir. Evie es un protagonista que me conquisto, su personalidad, su forma de ser, todas las situaciones en las que termina metida hicieron que disfrutara muchisimo de la lectura. El, simplemente es EL, nada mas que decir. La dinamica entre ellos es explosiva. Es una lectura divertida, romantica, magica y con personajesque se ganan un lugarcito en tu mente. Lo leeria nuevamente?, no lo dudaria jamas.",
            "pt": "O livro que me tirou da ressaca literária. LEIAM TUDO, do primeiro ao último livro; vocês não vão se arrepender. A Evie é uma protagonista que me conquistou — sua personalidade, seu jeito de ser e todas as situações em que ela acaba se metendo fizeram com que eu aproveitasse muito a leitura. Ele... bom, ele é simplesmente ELE; não há mais o que dizer. A dinâmica entre os dois é explosiva. É uma leitura divertida, romântica, mágica e com personagens que conquistam um espacinho na sua mente. Se eu leria de novo? Com ​​certeza, sem dúvida alguma!",
        },
    },
    {
        "id": "MejorQueLasPeliculas",
        "title": "Better Than The Movies",
        "author": "Lynn Painter",
        "genre": "romantasy",
        "stars": 4.5,
        "cover": "C:\\Users\\jacqu\\Blog-Book\\portadas\\mejorquelaspeliculas.jpg",
        "summary": {
            "es": "Un cuento de La Bella y la Bestia en el mundo de las hadas.",
            "pt": "Uma releitura de A Bela e a Fera no mundo das fadas.",
        },
        "review": {"es": "Escribí acá tu opinión.", "pt": "Escreva aqui a sua opinião."},
    },
    {
        "id": "beach-read",
        "title": "Beach Read",
        "author": "Emily Henry",
        "genre": "romance",
        "stars": 4,
        "cover": None,
        "summary": {
            "es": "Dos escritores rivales, un verano y un desafío.",
            "pt": "Dois escritores rivais, um verão e um desafio.",
        },
        "review": {"es": "Escribí acá tu opinión.", "pt": "Escreva aqui a sua opinião."},
    },
    {
        "id": "silent-patient",
        "title": "The Silent Patient",
        "author": "Alex Michaelides",
        "genre": "thriller",
        "stars": 3,
        "cover": None,
        "summary": {
            "es": "Una mujer que dejó de hablar tras un crimen.",
            "pt": "Uma mulher que parou de falar após um crime.",
        },
        "review": {"es": "Escribí acá tu opinión.", "pt": "Escreva aqui a sua opinião."},
    },
]