# Proyecto Final Algoritmos y Programación

## Proyecto Realizado por : Jaider Andres Garcia , Ricardo Prieto y Maria Jose Diaz. - Estudiantes de Ingenieria de Sistemas en la Universidad Ean. 📚

Inicialmente se considera pertinente dar una breve descripción acerca de la importancia de aplicar los conocimientos obtenidos a lo largo de la unidad de estudio de , Algoritmos y programación , la cual (es una unidad de estudio impartida por docentes altamente calificados de la universidad EAN, para todos los estudiantes de la facultad de Ingeniería ).
Por lo tanto , al finalizar de esta misma (unidad de estudio), se pretende obtener como proyecto final realizado por los estudiantes ; tal y como lo es este ,en el cual se llevo a cabo la creación de un asistente de voz que funcionara a partir de la terminal de cualquier computador o sistema operativo que tenga preinstalado Python , como el lenguaje de programación fundamental que permitirá obtener o desarrollar unas acciones predeterminadas que se le soliciten a dicha asistente de voz para que por lo tanto estas se ejecuten de manera satisfactoria . 
Así mismo, es importante tener presente que todos estos conocimientos obtenidos en la unidad de estudio pudieron verse aplicadas y comprendidos de una mejor manera a lo largo de la realización tanto de los talleres como del proyecto final .

![microphone_ui_animation-1](https://user-images.githubusercontent.com/98360789/159489079-49e6467a-bd19-497c-9384-9b2dc7db4b84.gif)


A continuación encontrara una breve descripción acerca de como fue la realización del proyecto final , en nuestro caso una asistente de voz , la cual le permitira ejercutar una serie de operaciones matemáticas mediante un dictado por voz que usted puede ejecutar a partir de la terminal de un computador en el cual tenga instalado de manera apriori *Python* , el cual sera el lenguaje de programacion que permitira llevar a cabo dichas operaciones y que posteriormente le entregara tambien por voz el resultado de dicha operación matemática. De igual manera es importante mencionar que para que el el programa funcione de una manera eficiente se recomienda una buena pronunciacion y el uso de los comandos para solicitarle a la asistende de voz el resultado.


# Herramientas utilizadas
Las herramientas que necesitamos para realizar este proyecto son:
Tener un editor de texto, en nuestro caso usamos Visual Studio Code junto con el lenguaje de programación, que en este caso es Python. Finalmente, y en adición a estas dos herramientas se deberán instalar los tres paquetes y/o librerías siguientes: (AVMSpeechMath 0.0.5, SpeechRecognition 3.8.1, pyttsx3 2.90) , sobre las cuales a continuación daremos una breve descripción acerca de la importancia de su uso para la creación de nuestra asistente de voz.

# Como llevar acabo el proceso de instalación de los paquetes utilizados.
Para comenzar el proceso de instalacion de los paquetes debe ir a la barra de busqueda de su computador , la cual normalmente la encontrara en su escritorio . Alli debera escribir "simbolo del sistema (cmd) " en sistemas operativos como el de windows y para mac OS, tendra que dirigirse a  spotlight, buscar "Terminal" y con esto podra acceder facilmente a ella. Una vez este en la terminal o "cmd" debera escribir "pip.install" seguido de el nombre del paquete, como son 3 paquetes tendremos que hacer la instalacion por cada uno de ellos. O simplemente ir a las pagina en donde se encuentra la informacio de dichas librerias, en donde podra copiar el codigo facilmente y pegarlo en la terminal o cmd para que posterior al enter de su teclado , esta empiece el proceso de instalación.

![xd](https://user-images.githubusercontent.com/98360348/159516284-0e7f2519-453c-4c12-ad0d-a8f82c31bd02.png)


# Paquetes y/o librerías utilizadas para la implementación del código. 

# AVMSpeechMath 0.0.5
## Perform voice operations in Spanish with Python.
Resuelve operaciones matemáticamente por voz. Este paquete es el encargado de reconocer palabras claves (sin acentos/tildes) como son: “cuanto es”, “mas”, “menos”, “por”, “dividido”, hasta una operación más compleja como la es la “raíz”. Esta librería también está encargada de hacer múltiples operaciones a la vez para un único resultado, respetando la jerarquía de operaciones , fundamental para el desarrollo de las operaciones que puede realizar nuestra asistente de voz , mediante el reconocimiento de la misma (voz) al ser obtenida cuando una persona habla haciendo uso de los comandos anteriormente mencionados.

# Proceso de instalación
![AVMSpeechMath](https://user-images.githubusercontent.com/98360348/159507687-d0883280-353d-4311-ad8b-4ad3d9aebde4.png)

<img width="833" alt="Captura de Pantalla 2022-03-21 a la(s) 9 32 21 p m" src="https://user-images.githubusercontent.com/98360789/159396450-846f49a3-1aff-488f-8a15-4c0c4a3f7357.png">

 Link para más informacion :https://pypi.org/project/AVMSpeechMath/ 


# SpeechRecognition 3.8.1
## Library for performing speech recognition, with support for several engines and APIs, online and offline.
Este paquete es el encargado de reconocer la voz por micrófono, sin embargo, en esta tenemos que al ser un lenguaje predeterminado en ingles (frente a la manera de la configuración lingüística de las palabras) , optamos por crear una variable que permitirá reconocer la configuración idiomática del español. Por lo tanto, remplazamos los acentos de las vocales para que no haya confusión en la ecualización de la voz ya que en el reconocimiento se puede entender de una manera incorrecta una palabra , para lo que se coloco un .lower(),que permitirá transformar todo el reconocimiento por voz en minúsculas, para no tener errores frente al léxico , e interpretación de la lingüística mediante el reconocimiento por voz.

# Proceso de instalación
![SpeechRecognition](https://user-images.githubusercontent.com/98360348/159507791-385d31eb-ab0e-4207-b780-8842ea112ad4.png)

<img width="833" alt="Captura de Pantalla 2022-03-21 a la(s) 9 35 05 p m" src="https://user-images.githubusercontent.com/98360789/159396572-48818c1e-149d-4519-9d51-b08cee252b01.png">

Link para más informacion :https://pypi.org/project/SpeechRecognition/ 


# pyttsx3 2.90
## Text to Speech (TTS) library for Python 2 and 3. Works without internet connection or delay. Supports multiple TTS engines, including Sapi5, nsss, and espeak.
Este paquete funciona como la voz de Python , la cual es configurable ( frente a las posibles voces que se pueden seleccionar) , esta se generara para darle una respuesta fija o una respuesta variable mediante los altavoces del equipo desde el cual se ejecuta el código. En nuestro caso dará respuesta  frente a las operaciones matemáticas planteadas inicialmente por el usuario. E incluso este paquete es funcional tanto en diferentes idiomas , tanto en el  ingles ,español,etc.

# Proceso de instalación
![pyttsx3](https://user-images.githubusercontent.com/98360348/159507859-a09cd2bb-5996-405f-b7e8-03d5ea341c62.png)

<img width="833" alt="Captura de Pantalla 2022-03-21 a la(s) 9 35 13 p m" src="https://user-images.githubusercontent.com/98360789/159396600-60a92df4-478f-4161-8903-c7ba8ee165d1.png">

Link para más informacion :https://pypi.org/project/pyttsx3/ 
