#Guia
define guia = Character("???")
define guia2 = Character("Ulises", color="#00ff00")
image guia = "ulises.png"
image guia_camina = "ulises_caminando_por_detras.png"
image guia_pregunta = "ulises_preguntando.png"
image guia_saludo = "ulises_saludando.png"
image guia_apunta = "ulises_señalando.png"
image portada = "portada.jpg"
#intrada  
image Entrada_Afuera = "inicio.jpg"
image entrada_principal = "dentro_edi_principal.jpg"
#bilbioteca imagenes
image bibliote_entrad = "bibliote_entrad.jpg"
image seg_derecho = "seguir_derecho.jpg" 
image entrada_casino = "entrada_casino.jpg"
#edificio administrativo imagenes
image edificio_administrativo_entrad = "edificio_administrativo.jpg"
#casino imagenes 
image casino = "casino.jpg"
image casino_interior = "casino_interior.jpg"
image casino_arriba1 = "casino_arriba.jpg"
##laboratorio imagenes
image laboratorio = "laboratorio.jpg"
image escalera_lab = "escalera_lab.jpg"
#sala de materiales
##image sala_materiales: "entrada_sala_materiales.jpg"
#gym
image gym1 = "gym1.jpg"
image gym2 = "gym2.jpg"
#salas de profesores
image salaprofesores = "sala_profesores.jpg"
#videos 
image biblioteca_video = Movie(play="videos/video_biblioteca.webm", size=(1920,1080), loop=False, xalign=0.5, yalign=0.5)
image casino_arriba = Movie(play="videos/casino_arriba.webm", size=(1920,1080), loop=False, xalign=0.5, yalign=0.5)
image ir_videoconfe = Movie(play="videos/ir_a_videoconferencia.webm", size=(1920,1080), loop=False, xalign=0.5, yalign=0.5)
image ir_algym = Movie(play="videos/ir_a_gym.webm", size=(1920,1080), loop=False, xalign=0.5, yalign=0.5)
image subir_lab = Movie(play="videos/subir_a_laboratorio.webm", size=(1920,1080), loop=False, xalign=0.5, yalign=0.5)
image ir_edificio_principal = Movie(play="videos/ir_a_principal.webm", size=(1920,1080), loop=False, xalign=0.5, yalign=0.5)
image biblioteca_completa = Movie(play="videos/ir_a_bibloeteca_comple.webm", size=(1920,1080), loop=False, xalign=0.5, yalign=0.5)
image adentro_biblioteca = Movie(play="videos/entrada_bibleoteca.webm", size=(1920,1080), loop=False, xalign=0.5, yalign=0.5)
image dentro_biblio = "dentro_biblio.jpg"
image ir_a_administrativo = Movie(play="videos/ir_a_administrativo.webm", size=(1920,1080), loop=False, xalign=0.5, yalign=0.5)
image guia = "images/ulises.png"
image ir_videoconfe = Movie(play="videos/ir_a_videoconferencia.webm", size=(1920,1080), loop=False, xalign=0.5, yalign=0.5)
image sala_de_conferen = "images/sala_confe.jpg"
label start:
    scene Entrada_Afuera
    show guia
    with fade
    queue music "audio/1.mp3" volume 0.5 #Incio de la música 
    guia "¡Hola! Bienvenido al tour virtual de la Universidad de Los Lagos. Hoy te acompañaré a recorrer los lugares más importantes de nuestro campus Chinquihue. Así podrás conocerlos antes de venir y no te perderás."
    guia2 "Mi nombre es Ulises y hoy te acompañaré a conocer los espacios más importantes de nuestro campus Chinquihue. Sé que a veces es difícil ubicarse cuando uno es nuevo o viene de visita, por eso este recorrido"
    guia2 "te ayudará a reconocer los lugares antes de llegar. Aquí podrás ver imágenes reales y aprender para qué sirve cada espacio de la universidad."
    show guia at Position(xalign=1.0, yalign=1.0)

    menu:
        "¿A que lugar vamos para empezar?"
        "Ir la biblioteca":
            stop music fadeout 1.0
            scene black
            show biblioteca_completa
            $ renpy.pause(11.0, hard=True)
            jump biblioteca
        "Seguir derecho":
            jump derecho
        "Ir al edificio principal":
            stop music fadeout 1.0
            scene black
            show ir_edificio_principal
            $ renpy.pause(10.2, hard=True)
            jump edificio_principal
        "Salir del juego":
            jump volver_inicio

label volver_inicio:
    menu:
        "¿Qué deseas hacer?"
        "Volver al principales":
            jump start
        "Finalizar el tour":
            jump despedida

label biblioteca:
    scene black
    with fade
    scene bibliote_entrad
    with dissolve
    show guia_camina
    with dissolve
    guia2 "!Entremos!"
    show adentro_biblioteca
    with dissolve
    $ renpy.pause(7.0, hard=True)
    hide adentro_biblioteca
    with dissolve
    scene dentro_biblio
    show guia_pregunta
    with dissolve
    guia2 "Esta es la biblioteca. Aquí puedes encontrar una gran variedad de libros, y recursos digitales para tus estudios. Además, la biblioteca cuenta con computadores disponibles para buscar información o realizar tus trabajos."
    guia2 "Si necesitas un lugar tranquilo para concentrarte, aquí encontrarás zonas de silencio total. Es importante que respetes las normas de silencio y cuidado de los libros para que todos puedan usarlos."
    jump dondequieresir

label dondequieresir:
    scene Entrada_Afuera
    show guia
    with fade
    queue music "audio/1.mp3" volume 0.5 #Incio de la música
    show guia at Position(xalign=1.0, yalign=1.0)

    menu:
        "Volver a la biblioteca":
            stop music fadeout 1.0
            scene black
            show biblioteca_completa
            $ renpy.pause(11.0, hard=True)
            jump biblioteca
        "Seguir derecho":
            jump derecho
        "Ir al edificio principal":
            stop music fadeout 1.0
            scene black
            show ir_edificio_principal
            $ renpy.pause(10.2, hard=True)
            jump edificio_principal
        "Salir del juego":
            jump volver_inicio


label derecho:
    scene seg_derecho
    with dissolve

    guia2 "¿A donde vamos ahora?"
    show guia at Position(xalign=1.0, yalign=1.0)

    menu:
        "Ir a la sala de videoconferencia":
            stop music fadeout 1.0
            show ir_videoconfe
            with dissolve
            $ renpy.pause(4.0, hard=True)
            jump sala_videoconferencia
        "Ir al edicio administrativo":
            stop music fadeout 1.0
            guia "Vamos al edificio administrativo."
            show ir_a_administrativo
            show guia_camina at right
            with dissolve
            $ renpy.pause(17.0, hard=True)
            jump edificio_administrativo_entrad
        "Volver al inicio":
            jump volver_inicio
        "Salir del juego":
            jump despedida

label sala_videoconferencia:
    scene sala_de_conferen
    show guia_camina
    with dissolve
    hide guia_camina
    show guia at Position(xalign=1.0, yalign=1.0)
    guia2 "Esta es la sala de videoconferencia. Aquí puedes realizar reuniones virtuales o asistir a clases en línea."
    hide guia
    show guia_pregunta at Position(xalign=1.0, yalign=1.0)
    jump dondequieresir2

label dondequieresir2:
    scene Entrada_Afuera
    show guia
    with fade
    queue music "audio/1.mp3" volume 0.5 #Incio de la música
    show guia at Position(xalign=1.0, yalign=1.0)

    menu:
        "Volver a la biblioteca":
            stop music fadeout 1.0
            scene black
            show biblioteca_completa
            $ renpy.pause(11.0, hard=True)
            jump biblioteca
        "Seguir derecho":
            jump derecho
        "Ir al edificio principal":
            stop music fadeout 1.0
            scene black
            show ir_edificio_principal
            $ renpy.pause(10.2, hard=True)
            jump edificio_principal
        "Salir del juego":
            jump volver_inicio

label edificio_administrativo: 
    scene edificio_administrativo
    with dissolve

    guia2 "Este es el edificio administrativo. Aquí puedes encontrar las oficinas de la administración de la universidad."
    guia2 "Si necesitas ayuda con algo relacionado con tu matrícula, horarios o cualquier otro tema administrativo, este es el lugar al que debes acudir."
    jump edificio_administrativo_entrad

label edificio_administrativo_entrad:
    scene edificio_administrativo_entrad
    with dissolve
    show guia at Position(xalign=1.0, yalign=1.0)

    guia2 "Esta es la entrada del edificio administrativo. Aquí puedes encontrar información sobre la universidad y sus servicios."
    jump dondequieresir2

label edificio_principal:
    scene entrada_principal
    show guia_camina
    with dissolve
    guia2 "Este es el edificio principal de la universidad. Aquí puedes encontrar las aulas, laboratorios y oficinas de los profesores."
    hide guia_camina
    show guia at Position(xalign=1.0, yalign=1.0)

    menu:
        "¿A donde vamos ahora?"
        "Ir a la sala de profesores":
            jump sala_profesores
        "Ir al casino":
            jump casino
        "Salir del juego":
            jump despedida
        "seguir derecho":
            jump recto2


label casino:
    scene entrada_casino
    with dissolve

    guia2 "Aquí estamos en el casino. Este es un lugar donde los estudiantes pueden relajarse y disfrutar de un buen rato."
    jump casino_interior

label casino_interior:
    scene casino_interior
    with dissolve

    guia2 "Este es el interior del casino. Aquí puedes encontrar mesas para almorzar y para calentar los almuerzos."
    guia2 "Tambien puedes compra alimentos y bebidas en la cafetería."
    jump casino_arriba

label casino_arriba:
    scene casino_arriba
    with dissolve

    guia2 "En la parte de arriba del casino, puedes encontrar un lugar para descansar y relajarte."
    guia2 "También hay mesas para almorzar y micro ondas."
    show guia at Position(xalign=1.0, yalign=1.0)
    scene casino_arriba1
    menu:
        "¿A donde vamos ahora?"
        "Volver al inicio":
            jump volver_inicio
        "Salir del juego":
            jump despedida
label escalera_lab:
    scene escalera_lab 
    with dissolve   
    guia2 "Esta es la escalera que lleva al laboratorio, vamos a ver los laboratorios."    
    jump laboratorio

label laboratorio:
    scene laboratorio
    with dissolve

    guia2 "Aquí estamos en el laboratorio. Este es un lugar donde los estudiantes pueden realizar experimentos y trabajos prácticos."
    show guia at Position(xalign=1.0, yalign=1.0)

    menu:
        "¿A donde vamos ahora?"
        "Volver al inicio":
            jump volver_inicio
        "Salir del juego":
            jump despedida

label recto:
    guia2 "Aquí irías derecho por el pasillo principal."
    jump volver_inicio

label aulas:
    guia2 "Estas son las salas de clases."
    jump volver_inicio

label sala_profesores:
    scene salaprofesores
    guia2 "Esta es la sala de los profesores donde los puedes encontrar si tienes una duda."
    call edificio_principal

label despedida:
    scene portada
    show guia_saludo
    with fade

    guia2 "Gracias por acompañarme en este recorrido por todos los rincones de nuestra universidad."
    guia2 "Espero que hayas disfrutado este tour virtual y que pronto puedas venir a conocerlo todo en persona."
    show guia_saludo at Position(xalign=1.0, yalign=1.0)

    return

label splashscreen:
    scene black
    show image "images/portada.jpg"
    with dissolve
    return

label before_main_menu:
    call splashscreen
    return
