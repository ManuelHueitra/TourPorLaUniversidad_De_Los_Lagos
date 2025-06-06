# Definimos el personaje guía
define guia = Character("Guía")

# Cargamos las imágenes disponibles
image campus_day = ""
image biblioteca = ""

label start:

    scene campus_day
    with fade

    guia "Hola bienvenido al tour sobre todos los lugares de la Universidad de Los Lagos"
    guia "Soy tu guía. Hoy visitaremos uno de los lugares más importantes del campus."


label escena_biblioteca:
    scene biblioteca
    with dissolve

    guia ""
    guia ""

    jump despedida

label despedida:
    scene campus_day
    with fade

    guia ""
    guia ""

    return
