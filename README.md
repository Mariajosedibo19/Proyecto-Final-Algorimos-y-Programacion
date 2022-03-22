# Proyecto Final Algoritmos y Programacion

Inicialmente se considera pertinente dar una breve descripción acerca de la importancia de aplicar los conocimientos obtenidos a lo largo de la unidad de estudio de , Algoritmos y programación , la cual (es una unidad de estudio impartida por docentes altamente calificados de la universidad EAN, para todos los estudiantes de la facultad de Ingeniería ).
Por lo tanto , al finalizar de esta misma (unidad de estudio), se pretende obtener como proyecto final realizado por los estudiantes ; tal y como lo es este ,en el cual se llevo a cabo la creación de un asistente de voz que funcionara a partir de la terminal de cualquier computador o sistema operativo que tenga preinstalado Python , como el lenguaje de programación fundamental que permitirá obtener o desarrollar unas acciones predeterminadas que se le soliciten a dicha asistente de voz para que por lo tanto estas se ejecuten de manera satisfactoria . 
Así mismo, es importante tener presente que todos estos conocimientos obtenidos en la unidad de estudio pudieron verse aplicadas y comprendidos de una mejor manera a lo largo de la realización tanto de los talleres como del proyecto final .


A continuación encontrara una breve descripción acerca de como fue la realización del proyecto final , en nuestro caso un asistente de voz el cual le permitira ejercutar una serie de operaciones matemáticas mediante un dictado por voz que usted puede ejecutar a partir de la terminal de un computador en el cual tenga instalado de manera apriori *Python* , el cual sera el lenguaje de programacion que permitira llevar a cabo dichas operaciones y que posteriormente le entregara tambien por voz el resultado de dicha operación ion matemática.


# Herramientas utilizadas
Las herramientas que necesitamos para realizar este proyecto son:
## •	Tener un editor de texto, en nuestro caso usamos Visual Studio Code junto con el lenguaje de programación, que en este caso es Python. Finalmente, y en adición a estas dos herramientas se deberán instalar los tres paquetes y/o librerías siguientes: (AVMSpeechMath 0.0.5, SpeechRecognition 3.8.1, pyttsx3 2.90) , sobre las cuales a continuación daremos una breve descripción acerca de la importancia de su uso para la creación de nuestra asistente de voz.
Paquetes y/o librerías utilizadas para la implementación del código 

# AVMSpeechMath 0.0.5
## Perform voice operations in Spanish with Python.
Resuelve operaciones matemáticamente por voz. Este paquete es el encargado de reconocer palabras claves (sin acentos/tildes) como son: “cuanto es”, “mas”, “menos”, “por”, “dividido”, hasta una operación más compleja como la es la “raíz”. Esta librería también está encargada de hacer múltiples operaciones a la vez para un único resultado, respetando la jerarquía de operaciones , fundamental para el desarrollo de las operaciones que puede realizar nuestra asistente de voz , mediante el reconocimiento de la misma (voz) al ser obtenida cuando una persona habla haciendo uso de los comandos anteriormente mencionados.

<img width="833" alt="Captura de Pantalla 2022-03-21 a la(s) 9 32 21 p m" src="https://user-images.githubusercontent.com/98360789/159396450-846f49a3-1aff-488f-8a15-4c0c4a3f7357.png">


# SpeechRecognition 3.8.1
## Library for performing speech recognition, with support for several engines and APIs, online and offline.
Este paquete es el encargado de reconocer la voz por micrófono, sin embargo, en esta tenemos que al ser un lenguaje predeterminado en ingles (frente a la manera de la configuración lingüística de las palabras) , optamos por crear una variable que permitirá reconocer la configuración idiomática del español. Por lo tanto, remplazamos los acentos de las vocales para que no haya confusión en la ecualización de la voz ya que en el reconocimiento se puede entender de una manera incorrecta una palabra , para lo que se coloco un .lower(),que permitirá transformar todo el reconocimiento por voz en minúsculas, para no tener errores frente al léxico , e interpretación de la lingüística mediante el reconocimiento por voz.

<img width="833" alt="Captura de Pantalla 2022-03-21 a la(s) 9 35 05 p m" src="https://user-images.githubusercontent.com/98360789/159396572-48818c1e-149d-4519-9d51-b08cee252b01.png">


# pyttsx3 2.90
## Text to Speech (TTS) library for Python 2 and 3. Works without internet connection or delay. Supports multiple TTS engines, including Sapi5, nsss, and espeak.
Este paquete funciona como la voz de Python , la cual es configurable ( frente a las posibles voces que se pueden seleccionar) , esta se generara para darle una respuesta fija o una respuesta variable mediante los altavoces del equipo desde el cual se ejecuta el código. En nuestro caso dará respuesta  frente a las operaciones matemáticas planteadas inicialmente por el usuario. E incluso este paquete es funcional tanto en diferentes idiomas , tanto en el  ingles ,español,etc.

<img width="833" alt="Captura de Pantalla 2022-03-21 a la(s) 9 35 13 p m" src="https://user-images.githubusercontent.com/98360789/159396600-60a92df4-478f-4161-8903-c7ba8ee165d1.png">


