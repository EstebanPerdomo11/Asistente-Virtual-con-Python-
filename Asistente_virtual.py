# Librerias
import speech_recognition as sr #Esta libreria sirve basicamente es tomar todo lo que le digamos a la computadora por medio del microfono y convertirlo a texto (string) y por último le damos un nombre para no escribir el nombre tan largo de la libreria original.
import pyttsx3, pywhatkit #El pyttsx3 sirve para que nuestra computadora empiece a hablar, pero necesitamos otra libreria la cuál sirve que python comience a hablar y la liberia es Pyaudio, la otra libreria pywhatkit esta libreria sirve para cuando se crea el asistente virtual le de un cierto "poder", para ser más claro lo que haría es que cuando le digamos que reproduzca una canción lo que va hacer es entrar a youtube a reproducir la música que le dijimos.

import wikipedia, datetime, keyboard
# from pygame import* 

name = "alexa" #Le damos un nombre al asistente virtual
listener = sr.Recognizer() #Creamos una variable y la igualamos con el nombre de la libreria. recognizer() para que empiece a reconocer.
engine = pyttsx3.init()#Luego creamos otra variable a la cual será igual a la inicialización de la libreria pyttsx3.

voices = engine.getProperty('voices') #Declaramos otra variable a la cuál se le asigna la variable anterior (engine) con una función llamada getProperty y entre parentesis y comillas simples la variable a la cuál se le está igualando y lo que está haciendo es que la variable engine y obtener la propiedades de voices, porque quizas cuando sea la primera vez use la libreria probablemente la voz que saldrá de la computadora no sea del gusto.
engine.setProperty('voices', voices[0].id) #Aquí se vuelve a tomar la variable engine con una función llamada setProperty la cuál se volverá a usar el String voices en comillas simple y luego se pone una , y se vuelve a usar el String voices y entre [] se pone 0 y luego .id la cuál hará es asignarle una voz al asistente ya que viene por determinar 2 voces una en español y otra en inglés y la de español es 0 y la de inglés es 1.

#Creación de funciones para las acciones del asistente virtual

# Primera función, llamada talk con un parametro llamado text entr los parentesis, esta función lo que hará es que la computadora hable,en esta función solo se necesita 2 lineas de códigos, la primera es engine.say(text) --> esta lo que hará es que todo lo que se ponga dentro del parentesis con el método say la computadora va hablarlo osea pasa de ser letras (String) a voz, pero para que eso funcine entra en juego la siguiente linea que es engine.runAndWait() --> esta lo que hará es que corra y espere.
                                                                                   
def talk(text):
    engine.say(text)
    engine.runAndWait()

# Segunda función, llamada listen esta función lo que hará es que la computadora escuche lo que le digamos, para eso hay que crear un try and except, esto sirve para comprobar que todo vaya bien al momento de ejecutar el asistente virtual y para comprobarlo se va a poner dentro del try lo siguiente with sr.Microphone() as source, aquí estamos diciendole que tome nuestro micrófono como fuente para escuchar cosas y para saber que si está escuchando se pone un print, luego de eso se declara una variable en este caso pc que será igual a listener.listen(source) a la cuál es la variable de al principio la cuál hará es escuchar  desde la funete osea el microfono, pero faltaría algo para que empiece a reconocer nuestra voz y lo transforme en texto. para eso se le declara una variable la cuál se llamó rec que es igual alistener.reconize_google(pc), estamos diciendole a listener que utilice los servicios de reconocimiento de google y que listener escuche desde pc.

# Luego lo que haremos es que debemos que hacer es que la computadora sepa que le estamos hablandole a ella  a través del nombre que se le declaró al principio y para eso decimos rec = rec.lower() lo cuál permite pasar el texto a minúscula y luego por medio de un if decimos if name in rec osea estamos diciendo que si el nombre está dentro de ese texto que haga lo siguiente, primero se reemplaza el nombre por un String vacio para cuando ella hable no repita su nombre y para eso se hace rec = rec.replace('name', '') y si el caso tal que el try falla entonces que salte a except y se le agrega pass que significa que no haga nada y por último un print. por último haremos un return que retoner la variable rec y se imprima.
def listen():
    try:
        with sr.Microphone() as source: 
            print("Escuchando...")
            talk("Dime")
            pc = listener.listen(source)
            rec = listener.recognize_google(pc, language = "es")
            rec = rec.lower()
            if name in rec:
                rec = rec.replace(name, '')
    except:
        pass
        print("Ups, algo malo ocurrió")
    return rec

# Tercera función, es llamada como Run_alexa() la cuál se declara una variable llamada rec que sea igual a la función listen, aquí estamos diciendo que la computadora debe reconocer lo que estamos diciendo y en este caso queremos reproducir música, para eso se hace una condición if 'reproduce' in rec estamos diciendo si en rec se haya dicho reproduce entonces quiero que haga lo siguiente, declaramos una variable que se iguale a rec.replace('reproduce', ''), aquí decimos que reemplace la palabra reproduce por unString vacio para cuando hable la asistente no repita reproduce, luego imprimimos en pantalla ("Reproduciendo", + music), ósea aquí decimo que se imprima la palabra reproduciendo + el texto que haya obtenido por rec y luego hacemos que la computadora hable con un método llamado talk y ponemos lo mismo que se haya imprimido por último para que la computadora pueda entrar a youtube y ponga la música que dijimos usamos la función pywhatkit.playonyt(music) aquí le decimos es que se dirija a youtube e inicie la música que dijimos.
def Run_alexa():
    rec = listen()
    if 'reproduce' in rec:
        music = rec.replace('reproduce', '')
        print("Reproduciendo" + music)
        talk("Reproduciendo" + music)
        pywhatkit.playonyt(music)
    
    elif 'busca' in rec:
        buscador = rec.replace('busca', '')
        wikipedia.set_lang("es")
        wiki = wikipedia.summary(buscador, 2)
        print(buscador + ": " + wiki)
        talk(wiki)

if __name__ == '__main__':
    Run_alexa() 