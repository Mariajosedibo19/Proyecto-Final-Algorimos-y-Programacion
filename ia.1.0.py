import speech_recognition as reconocimiento
import pyttsx3
import AVMSpeechMath as matematicas
nombre="cortana"
listener= reconocimiento.Recognizer()
habla=pyttsx3.init()
tra="termina"
def hablar(text):
    habla.say(text)
    habla.runAndWait()
while True:
    try:
        with reconocimiento.Microphone() as lectura:
            print("escuchando...")
            escuchar=listener.listen(lectura)
            grabacion=listener.recognize_google(escuchar, language="es-ES").lower()
            grabacion=grabacion.replace("á","a")
            grabacion=grabacion.replace("é","e")
            grabacion=grabacion.replace("í","i")
            grabacion=grabacion.replace("ó","o")
            grabacion=grabacion.replace("ú","u")
            if nombre in grabacion:
                grabacion=grabacion.replace(nombre, "")
                print(grabacion)
                resultado=matematicas.getResult(grabacion)
                hablar(resultado)
            if tra in grabacion:
                break
    except:
        pass