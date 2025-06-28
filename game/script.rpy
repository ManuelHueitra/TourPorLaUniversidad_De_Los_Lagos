#Guia
define guia = Character("Guía")
image guia = "ulises.png"
image guia_camina = "ulises_caminando_por_detras.png"
image guia_pregunta = "ulises_pregun.png"
image guia_saludo = "ulises_saludando.png"
image guia_apunta = "ulises_señalando.png"

#intrada  
image Entrada_Afuera = "inicio.jpg"
#bilbioteca imagenes
image bibliote_entrad = "bibliote_entrad.jpg"
image seg_derecho = "seguir_derecho.jpg" 
image entrada_casino = "entrada_casino.jpg"
#edificio administrativo imagenes
image edificio_administrativo_entrad = "edificio_admin_afuera.jpg"
image edificio_administrativo = "edificio_administrativo.jpg"

#casino imagenes 
image casino = "casino.jpg"
image casino_interior = "casino_interior.jpg"
image casino_arriba = "casino_arriba.jpg"
##laboratorio imagenes
image laboratorio = "laboratorio.jpg"
image escalera_lab = "escalera_lab.jpg"
#sala de materiales
##image sala_materiales: "entrada_sala_materiales.jpg"
#gym
image gym1 = "gym1.jpg"
image gym2 = "gym2.jpg"
#salas de profesores
image salaprofesores = "sala_de_profesores.jpg"

label start:
    scene Entrada_Afuera
    show guia_saludo
    with fade
    queue music "audio/1.mp3" volume 0.5 #Incio de la música 
    guia "Hola, bienvenido al tour sobre todos los lugares de la Universidad de Los Lagos."
    guia "Hoy vamos a visitar todos los lugares del campus de Chinquihue."
    menu:
        "¿A que lugar vamos para empezar?"
        "Ir la biblioteca":
            jump bibliote_entrad
        "Seguir derecho":
            jump derecho
        "Salir del juego":
            jump despedida

#    stop music fadeout 1.0
#    scene black
#    play movie "videos/video_biblioteca.mp4" 
#    
#    $ renpy.pause(11.0, hard=True) # Duración exacta del video    
#    stop movie
#    hide movie    
#    jump biblioteca

label biblioteca:
    scene bibliote_entrad
    with dissolve
    guia "Aquí estamos en la biblioteca. Este lugar es ideal para estudiar, leer o trabajar en grupo."
    menu:
        "¿Donde quieres ir ahora?"
        "Volver al inicio":
            jump start
        "Salir del juego":
            jump despedida

label derecho:
    scene seg_derecho
    with dissolve

    guia "¿A donde vamos ahora?"

    menu:
        "Volver al inicio":
            jump start
        "Salir del juego":
            jump despedida
        "Ir al casino":
            jump casino

label edificio_administrativo: 
    scene edificio_administrativo
    with dissolve

    guia "Este es el edificio administrativo. Aquí puedes encontrar las oficinas de la administración de la universidad."
    guia "Si necesitas ayuda con algo relacionado con tu matrícula, horarios o cualquier otro tema administrativo, este es el lugar al que debes acudir."
    jump edificio_administrativo_entrad

label edificio_administrativo_entrad:
    scene edificio_administrativo_entrad
    with dissolve

    guia "Esta es la entrada del edificio administrativo. Aquí puedes encontrar información sobre la universidad y sus servicios."
    menu:
        "¿A donde vamos ahora?"
        "Volver al inicio":
            jump start
        "Salir del juego":
            jump despedida

label casino:
    scene entrada_casino
    with dissolve

    guia "Aquí estamos en el casino. Este es un lugar donde los estudiantes pueden relajarse y disfrutar de un buen rato."
    jump casino_interior

label casino_interior:
    scene casino_interior
    with dissolve

    guia "Este es el interior del casino. Aquí puedes encontrar mesas para almorzar y para calentar los almuerzos."
    guia "Tambien puedes compra alimentos y bebidas en la cafetería."
    jump casino_arriba

label casino_arriba:
    scene casino_arriba
    with dissolve

    guia "En la parte de arriba del casino, puedes encontrar un lugar para descansar y relajarte."
    guia "También hay mesas para almorzar y micro ondas."
    menu:
        "¿A donde vamos ahora?"
        "Volver al inicio":
            jump start
        "Salir del juego":
            jump despedida

label sala_materiales:
    scene sala_materiales
    with dissolve

    guia "Esta es la sala de materiales. Aquí puedes encontrar todo lo que necesitas para tus proyectos y trabajos."

    menu:
        "¿A donde vamos ahora?"
        "Volver al inicio":
            jump start
        "Salir del juego":
            jump despedida

label escalera_lab:
    scene escalera_lab 
    with dissolve   
    guia "Esta es la escalera que lleva al laboratorio, vamos a ver los laboratorios."    
    jump laboratorio

label laboratorio:
    scene laboratorio
    with dissolve

    guia "Aquí estamos en el laboratorio. Este es un lugar donde los estudiantes pueden realizar experimentos y trabajos prácticos."

    menu:
        "¿A donde vamos ahora?"
        "Volver al inicio":
            jump start
        "Salir del juego":
            jump despedida



label despedida:
    scene black
    with fade

    guia "Gracias por acompañarme en este recorrido por todos los rincones de nuestra universidad."
    guia "Espero que hayas disfrutado este tour virtual y que pronto puedas venir a conocerlo todo en persona."

    return
