## Este archivo contiene opciones que pueden cambiarse para personalizar el
## juego.
##
## Las líneas que empiezan con doble '#' son comentarios, no deben ser
## descomentadas. Las líneas que empiezan con simple '#' son código comentado,
## puedes descomentarlas si es apropiado.


## Básico ######################################################################

## Nombre del juego en forma legible. Usado en el título de la ventana del
## juego, en la interfaz y en los informes de error.
##
## El _() que rodea la cadena de texto la señala como traducible.

define config.name = _("Tour por la Universidad de Los Lagos")



## Determina si el título dado más arriba se muestra en el menú principal.
## Ajústalo a 'False' para ocultar el título.

define gui.show_name = False
define config.version = "2.0"


## Texto situado en la pantalla 'Acerca de' del juego. Sitúa el texto entre
## comillas triples y deja una línea en blanco entre párrafos.

define gui.about = _p("""Tour en la Universidad de Los Lagos
Este juego interactivo fue desarrollado como parte del Taller de Introducción a la Ingeniería Informática de la Universidad de Los Lagos. Su propósito es ayudar a los estudiantes nuevos, visitantes y personas interesadas en conocer el campus Chinquihue de forma entretenida y educativa.
A través de este tour virtual, los usuarios podrán recorrer distintos espacios importantes de la universidad, como la biblioteca, las salas de clases y otros lugares comunes, con el objetivo de familiarizarse con el entorno y moverse con mayor confianza en su vida universitaria diaria.
El juego está diseñado como una novela visual utilizando Ren’Py, permitiendo presentar imágenes, diálogos y decisiones para una experiencia sencilla y accesible, tanto en computador como en dispositivos móviles.
Este proyecto fue realizado de manera individual, combinando conocimientos de programación, diseño de interfaces y análisis de problemáticas reales en la región, con el fin de aportar una solución digital innovadora al proceso de orientación de estudiantes en la Universidad de Los Lagos.
Gracias por probar esta aplicación educativa y ser parte de esta experiencia de aprendizaje. """)


## Nombre breve del juego para ejecutables y directorios en la distribución.
## Debe contener solo carácteres ASCII, sin espacios, comas o puntos y coma.

define build.name = "Tour"


## Sonidos y música ############################################################

## Estas tres variables controlan, entre otras cosas, qué mezcladores se
## muestran al reproductor de forma predeterminada. Establecer uno de estos en
## False ocultará el mezclador apropiado. 

define config.has_sound = True
define config.has_music = True
define config.has_voice = True


define config.enter_transition = dissolve
define config.exit_transition = dissolve


## Entre pantallas del menú del juego.

define config.intra_transition = dissolve


## Transición tras la carga de una partida.

define config.after_load_transition = None


## Transición de acceso al menú principal tras finalizar el juego.

define config.end_game_transition = None


define config.window = "auto"


## Transiciones usadas para mostrar o esconder la ventana de diálogo

define config.window_show_transition = Dissolve(.2)
define config.window_hide_transition = Dissolve(.2)


## Preferencias por defecto ####################################################

## Controla la velocidad del texto por defecto. El valor por defecto 0 indica
## infinito; cualquier otro número indica el número de caracteres por segundo
## que se mostrarán.

default preferences.text_cps = 30


## El retraso por defecto del auto-avance. Números más grandes indican esperas
## mayores. El rango válido es 0-30.

default preferences.afm_time = 15


## Directorio de guardado ######################################################
##
## Controla el lugar en el que Ren'Py colocará los archivos de guardado,
## dependiendo de la plataforma.
##
## Windows: %APPDATA\RenPy\<config.save_directory>
##
## Macintosh: $HOME/Library/RenPy/<config.save_directory>
##
## Linux: $HOME/.renpy/<config.save_directory>
##
## Normalmente, este valor no debe ser modificado. Si lo es, debe ser siempre
## una cadena literal y no una expresión.

define config.save_directory = "proyec-1748965297"


## Icono #######################################################################
##
## El icono mostrado en la barra de tareas.

define config.window_icon = "gui/window_icon.png"


## Configuración de 'Build' ####################################################
##
## Esta sección contrla cómo Ren'Py convierte el proyecto en archivos para la
## distribución.

init python:
    style.say_dialogue.color = "#ffffff"  # Color del diálogo
    style.say_label.color = "#000000"     # Color del nombre
    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)
    build.documentation('*.html')
    build.documentation('*.txt')