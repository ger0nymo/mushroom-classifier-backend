# Gombafelismerő témalabor-projekt

## Koncepció

Egy olyan telefonos alkalmazás, amely egy - a háztartás körül előforduló - gombát lefényképezve megmondja annak nevét és tulajdonságait.

## Felhasznált technológiák

* Gépi tanulás: **YOLOv8 osztályozó modell**, az adatok előkészítéséhez **Python**


* Backend: **Python (Flask)**


* Frontend: **Flutter**

## A megoldás menete

### Gépi tanulási megoldások kutatása

A feladat első lépéseként object detection/object classification témakörben kezdtem kutatni.

Mivel előtte nem foglalkoztam ilyennel, ezért hirtelen nem tudtam, hogy milyen modelleket érdemes használni, pontosan milyen formátumú adatokra van szükség, stb.

Szerencsére több modell is elérhető, illetve saját modell építéséhez is találni dokumentációkat.

Első próbálkozásként a Tensorflow keretrendszerben próbálkoztam modellépítéssel és tanítással, ami sikerült is Colabon keresztüli GPU hozzáféréssel,
azonban végeredményben a modell közel nem volt elég pontos (40%).

A pontosság drasztikus javítása érdekében végül már meglévő modellek között kezdtem keresgélni, itt több modell is szóba jött:
 * Detectron2
 * EfficientNetV2
 * YOLOv8

Elsőkörben a Detectron2-t próbáltam ki, azonban Colabon a függőségek verziókonfliktusai miatt nem tudtam érdemben haladni, viszont mivel csak itt fértem hozzá használható GPU-hoz, így ezt a megoldást el kellett vetnem.

Következő próbálkozásként az EfficientNetV2-t próbáltam, amelynek bár a tanítása jól sikerült, valós esetekben a modell nagyon pontatlan volt.
Mielőtt elkezdtem volna kinyomozni, hogy pontosan mi miatt lehetett ekkora eltérés a validációs és a tényleges pontosság között, úgy döntöttem, hogy kipróbálom a YOLOv8 osztályozásra készült modelljét is.
