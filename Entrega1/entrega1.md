# **Primera entrega: Propuesta de proyecto** 


## **Información y datos:** 
 **Problema seleccionado:** Clasificación de géneros de canciones - Classify song genres.  

 **Base de datos a usar:**  [classify-song-genres-from-audio-data](https://www.kaggle.com/code/ashishkumarak/classify-song-genres-from-audio-data)


## **Preguntas de interés sobre el problema a resolver:** 

 Las preguntas de interés que buscamos resolver con el desarrollo de este proyecto son: 

 ¿Cómo podemos clasificar automáticamente géneros de canciones sin escucharlas?
 ¿Cuál es la mejor aproximación para procesar y analizar grandes conjuntos de datos de audio?
 ¿Qué modelos de aprendizaje automático son más efectivos para clasificar géneros musicales?
 ¿Cómo podemos mejorar la precisión de la clasificación utilizando técnicas de reducción de características?

## **Sobre el problema**

 **Tipo de problema:** Clasificación de Múltiples Clases (Hip-Hop vs. Rock).


 ### **Metodología:**

 Nos basaremos en la metodología CRISP-DM (Cross-Industry Standard Process for Data Mining) para guiar nuestro proyecto. Adaptaremos cada fase de CRISP-DM a nuestras necesidades específicas, incluyendo la comprensión del negocio, comprensión de los datos, preparación de los datos, modelado, evaluación y despliegue.

 ### **Métricas de evaluación:**

 Utilizaremos métricas como precisión, recall, F1-score y matriz de confusión para evaluar el rendimiento de nuestros modelos de clasificación.

 ### **Datos recolectados o base de datos utilizados:**

 Utilizaremos el conjunto de datos proporcionado por The Echo Nest, que contiene características extraídas de archivos de audio de canciones. También exploraremos fuentes adicionales de datos de música.

 ### **Análisis exploratorio de los datos:**

 Realizaremos un análisis exploratorio de los datos para comprender la distribución de las características, identificar posibles problemas de calidad de datos y entender la relación entre las características y las etiquetas de género musical.

 ### **Próximos pasos:**


 Limpieza y Preprocesamiento de Datos:
   - Eliminar valores atípicos y duplicados.
   - Manejar datos desconocidos mediante imputación o eliminación de registros.
   - Normalizar las características para que tengan una escala común.
   
  Implementar Modelos de Clasificación:
   - Utilizar el modelo SVM para la clasificación de géneros musicales.

 Ajuste de Hiperparámetros y Comparación de Rendimiento:
   - Ajustar los hiperparámetros de los modelos seleccionados.
   - Comparar el rendimiento de los modelos utilizando validación cruzada y métricas de evaluación como precisión, recall y F1-score.

 Investigar Técnicas de Reducción de Características:
   - Explorar técnicas como PCA (Análisis de Componentes Principales) para reducir la dimensionalidad del conjunto de datos y mejorar la eficiencia computacional y la precisión del modelo de clasificación.

 ### **Aspectos éticos:** 

 **Equidad y sesgo algorítmico:** Los algoritmos de clasificación pueden estar sujetos a sesgos inherentes en los datos de entrenamiento, lo que puede resultar en decisiones discriminatorias o injustas. Es importante realizar una evaluación cuidadosa para identificar y mitigar cualquier sesgo en el modelo que pueda afectar desproporcionadamente a ciertos grupos de personas.


 **Transparencia y explicabilidad:** Los modelos de clasificación deben ser transparentes y explicables para que los usuarios puedan entender cómo se toman las decisiones y por qué se clasifican las canciones en determinados géneros. Esto ayuda a fomentar la confianza y la comprensión del sistema.


 **Impacto en la diversidad musical:** Los modelos de clasificación de géneros musicales pueden influir en la forma en que se promocionan y recomiendan ciertos tipos de música sobre otros. Es importante tener en cuenta el impacto que esto puede tener en la diversidad musical y asegurarse de que se promueva una amplia gama de géneros musicales.






