#Guia
define guia = Character("Guía")

image Entrada_Afuera = "inicio.jpg"
image bibliote_1 = "bibliote_entrad.jpg"
image seg_derecho = "seguir_derecho.jpg" 

label start:
    scene Entrada_Afuera
    with fade
    queue music "audio/1.mp3"
    guia "Hola, bienvenido al tour sobre todos los lugares de la Universidad de Los Lagos."
    guia "Hoy vamos a visitar todos los lugares del campus de Chinquihue."

    menu:
        "¿A que lugar vamos para empezar?" # Esta línea es opcional, es el prompt del menú.
        "Vamos a la biblioteca":
            jump biblioteca
        "Seguir derecho":
            jump derecho
        "Salir del juego":
            jump despedida

label biblioteca:
    scene bibliote_1
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
        # "Ir al casino":
        #     jump casino

label despedida:
    scene black
    with fade

    guia "Gracias por acompañarme en este recorrido por todos los rincones de nuestra universidad."
    guia "Espero que hayas disfrutado este tour virtual y que pronto puedas venir a conocerlo todo en persona."

    return
