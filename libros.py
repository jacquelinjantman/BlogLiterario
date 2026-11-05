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
        "cover": "..\\portadas\\assistentevillano.jpg",
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
        "cover": "..\\portadas\\mejorquelaspeliculas.jpg",
        "summary": {
            "es": "Liz es una chica que siempre soño con vivir una historia de amor como las de sus peliculas romanticas favoritas. Wes, su vecino, es todo lo contrario al chico ideal que Liz imagina. Desde que se conoecn se llevan mal, pero cuan Michael, el antiguo vecino de Liz y Wes vuelve, ella decide pedirle ayudaa Wes para llamar su atencion. Entre planes y bromas, Liz va a descubrir si el amor de verdad se parece a las peliculas que tanto admira o mucho mejor.",
            "pt": "Liz é uma garota que sempre sonhou em viver uma história de amor como as de seus filmes românticos favoritos. Wes, seu vizinho, é o oposto do garoto ideal que Liz imagina. Desde que se conheceram, eles não se dão bem; mas, quando Michael — antigo vizinho de Liz e Wes — retorna, ela decide pedir ajuda a Wes para chamar a atenção dele. Entre planos e brincadeiras, Liz descobrirá se o amor de verdade se parece com os filmes que ela tanto admira, ou se é algo muito melhor.",
        },
        "review": {"es": "Una historia que te deja con una sonrisa y el corazon contento. La evolucion de Liz y Wes, los cliches romanticos, WES <3. Liz te hace perder un poco la paciencia en algunos momentos, pero eso no opaco el disfrute de la historia. Un romance juvenil, divertido, perfecto para quienes les gusta la comedia romantica.",   
                   "pt": "Uma história que te deixa com um sorriso no rosto e o coração contente. A evolução de Liz e Wes, os clichês românticos, WES <3. A Liz faz a gente perder um pouco a paciência em alguns momentos, mas isso não estragou o prazer de acompanhar a história. Um romance juvenil, divertido, perfeito para quem gosta de comédia romântica."},
    },
    {
        "id": "ThatsNotMyName",
        "title": "That's Not My Name",
        "author": "Elísabet Benavent",
        "genre": "thriller",
        "stars": 4,
        "cover": "..\\portadas\\esenoesminombre.jpg",
        "summary": {
            "es": "Te imaginas despertar en un lugar desconocido, sin recordar quien sos y sin tener la menor idea de como llegaste ahi?. Lo mas importantes es, Quien dice la verdad? Que pasa cuando ni siquiera podes confiar en tu propia identidad?",
            "pt": "Já imaginou acordar em um lugar desconhecido, sem se lembrar de quem você é e sem ter a menor ideia de como foi parar lá? O mais importante é: quem está dizendo a verdade? O que acontece quando você não consegue nem sequer confiar na sua própria identidade?",
        },
        "review": {"es": "Al principio me costo un poquito entrar en la historia. Sentia que necesitaba tiempo para comprender que estaba pasando y como se relacionaban todos los acontecimientos. Pero, a medida que avanzaba, las piezas empezaban a encajar y la lectura se volvia mas atrapante. Habia situaciones que no me terminaban de convencer. El ritmo puede sentirse un poco lento en algunos momentos, pero creo que esa construccion es necesaria para comprender la trama y conectar las distintas piezas del misterio. El final? una de las cosas que hizo que me gustara este libro. Te mantiene intrigada, intentando descubrir que estaba pasando y cuestionando constantemente lo que creia saber,",
                   "pt": "No início, tive um pouco de dificuldade para entrar na história. Sentia que precisava de tempo para entender o que estava acontecendo e como todos os acontecimentos se relacionavam. Mas, à medida que avançava, as peças começavam a se encaixar e a leitura tornava-se cada vez mais envolvente. Havia situações que não me convenciam totalmente. O ritmo pode parecer um pouco lento em alguns momentos, mas acredito que essa construção seja necessária para compreender a trama e conectar as diferentes peças do mistério. O final? Foi um dos pontos que me fez gostar deste livro. Ele te mantém intrigada, tentando descobrir o que estava acontecendo e questionando constantemente aquilo que você achava que sabia."},
    },
   
]