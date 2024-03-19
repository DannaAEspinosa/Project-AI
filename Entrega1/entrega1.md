# **Primera entrega: Propuesta de proyecto** 

## **Información y datos:** 
 **Problema seleccionado:** Clasificación de géneros de canciones - Classify song genres. 
 
 **Base de datos a usar:**  [classify-song-genres-from-audio-data](https://www.kaggle.com/code/ashishkumarak/classify-song-genres-from-audio-data)

## **Introducción:**
En la era actual de la música digital, los servicios de transmisión de música han revolucionado la forma en que las personas descubren y disfrutan de la música. Sin embargo, la gran cantidad de música disponible puede resultar abrumadora para los usuarios que buscan descubrir nuevos artistas y géneros musicales. Por ello, los servicios de streaming han adoptado enfoques innovadores, como la clasificación automática de canciones en géneros musicales, para proporcionar recomendaciones personalizadas a los usuarios. En este proyecto, nos enfocaremos en desarrollar un sistema de clasificación automatizada de géneros musicales, utilizando técnicas de inteligencia artificial.

## **Preguntas de interés sobre el problema a resolver:** 

 Las preguntas de interés que buscamos resolver con el desarrollo de este proyecto son: 

 ¿Cómo podemos clasificar automáticamente géneros de canciones sin escucharlas?
 ¿Cuál es la mejor aproximación para procesar y analizar grandes conjuntos de datos de audio?
 ¿Qué modelos de aprendizaje automático son más efectivos para clasificar géneros musicales?
 ¿Cómo podemos mejorar la precisión de la clasificación utilizando técnicas de reducción de características?

## **Sobre el problema**

 **Tipo de problema:** Clasificación de Múltiples Clases (Hip-Hop vs. Rock).
 **Datos relevantes:** El proyecto utilizará datos extraídos de archivos de audio de canciones, incluyendo características como tempo, nivel de acústica, danceability, entre otros, para entrenar modelos de aprendizaje automático en la clasificación de géneros musicales.


 ### **Metodología:**

Para abordar este proyecto, adoptaremos la metodología CRISP-DM (Cross-Industry Standard Process for Data Mining). Esta metodología nos proporciona una estructura sólida para guiar el desarrollo de nuestro proyecto. Adaptaremos cada fase de CRISP-DM a nuestras necesidades específicas:  

- **Comprensión del negocio:** Exploraremos detalladamente el contexto de nuestro proyecto. Esto nos permitirá establecer una sólida base de conocimientos sobre la industria musical, los servicios de streaming y las necesidades de los usuarios.

- **Comprensión de los datos:** Analizaremos el conjunto de datos disponible y exploraremos sus características, su calidad y su relevancia para nuestro proyecto. Esta etapa nos brindará una visión clara de los recursos con los que contamos y nos ayudará a identificar posibles desafíos y oportunidades.

- **Preparación de los datos:** Limpiaremos y transformaremos los datos según sea necesario, asegurándonos de que estén en el formato adecuado y sean aptos para su análisis posterior. Esta fase es crucial para garantizar la calidad y la integridad de nuestros datos.

- **Modelado:** Aplicaremos técnicas de aprendizaje automático para entrenar y evaluar modelos predictivos de clasificación de géneros musicales. Utilizaremos diversas técnicas y algoritmos, como SVM y gradient boosting, explorando su rendimiento y ajustando sus hiperparámetros para obtener los mejores resultados posibles.

- **Evaluación:** Mediremos el rendimiento de los modelos construidos utilizando métricas como precisión, recall y F1-score. Esta etapa nos ayudará a comprender la efectividad de nuestros modelos y a identificar áreas de mejora potencial.

- **Despliegue:** Implementaremos nuestros modelos e

 ### **Métricas de evaluación:**

Utilizaremos un conjunto de métricas para realizar una evaluación completa del rendimiento de nuestros modelos de clasificación. Estas métricas incluyen:

- **Precisión:** Indica la proporción de predicciones correctas de géneros musicales realizadas por nuestro modelo en comparación con todas las predicciones realizadas. Una alta precisión significa que nuestro modelo hace menos predicciones incorrectas.

- **Recall:** Muestra la capacidad de nuestro modelo para encontrar todas las instancias relevantes de cada clase de género musical. Un alto recall indica que nuestro modelo logra identificar la mayoría de las instancias de cada género musical.

- **F1-score:** Proporciona una evaluación más equilibrada del rendimiento del modelo y es útil para medir cualquier desequilibrio entre las clases de géneros musicales en el conjunto de datos.

- **Matriz de confusión:** Brinda una visión detallada de cómo nuestro modelo clasifica las instancias de cada clase de género musical. Nos permite identificar posibles áreas de mejora y evaluar errores en la clasificación de géneros musicales, como la confusión entre géneros similares.


 ### **Datos recolectados o base de datos utilizados:**

Para llevar a cabo nuestro proyecto de clasificación de géneros musicales, nos basaremos en un conjunto de datos proporcionado por The Echo Nest. Esta base de datos contiene características extraídas de archivos de audio de canciones. Las características incluyen aspectos como el tempo, la acústica, la capacidad de baile y algunos más, que son fundamentales para comprender y clasificar diferentes géneros musicales de manera automatizada.

Además de utilizar el conjunto de datos proporcionado por The Echo Nest, también exploraremos otras fuentes de datos de música para aumentar nuestra comprensión y mejorar la precisión de nuestro modelo de clasificación. Estas fuentes adicionales incluiran datos de servicios de streaming de música, bases de datos públicas de música y otras fuentes disponibles en línea.

 ### **Análisis exploratorio de los datos:**

Realizaremos un análisis exploratorio de los datos para comprender la distribución de las características, identificar posibles problemas de calidad de datos y entender la relación entre las características y las etiquetas de género musical.Para lograr esto, realizaremos una serie de actividades como:

#### 1. Analizar Tipos de Datos

Examinaremos los tipos de datos presentes en nuestro conjunto de datos. Esto nos permitirá entender la naturaleza de las características con las que estamos trabajando y cómo podrían influir en nuestra capacidad para clasificar los géneros musicales.

#### 2. Explorar Variables o Características Categóricas

Identificaremos las variables categóricas en nuestro conjunto de datos, como el género musical de las canciones. Analizaremos la distribución de estas variables para comprender la prevalencia de cada género y si hay desequilibrios en la distribución que puedan afectar nuestra capacidad para clasificar con precisión.

#### 3. Explorar Variables o Características Numéricas

Exploraremos las características numéricas que describen las propiedades de las canciones, como el tempo, la energía y la acústica. Calcularemos estadísticas descriptivas, como la media, la mediana y la desviación estándar, para entender la distribución de estas características y detectar posibles valores atípicos.

#### 4. Explorar datos faltantes

Investigaremos si hay datos faltantes en nuestro conjunto de datos y determinaremos cómo manejarlos, ya que, la presencia de datos faltantes puede afectar la calidad de nuestros modelos de clasificación, por lo que es importante abordar este problema de manera adecuada.

#### 5. Análisis Bivariante

Realizaremos un análisis bivariante para explorar las relaciones entre las características y las etiquetas de género musical. Esto nos ayudará a identificar patrones o correlaciones que podrían ser útiles para la clasificación de géneros musicales.

#### 6. Valores Atípicos o Fuera de Rango o Outliers

Examinaremos la presencia de valores atípicos o fuera de rango en nuestras características numéricas. Ya que, los valores atípicos pueden sesgar nuestros modelos de clasificación, por lo que es importante identificarlos y determinar si deben ser tratados o excluidos del análisis.

Este análisis exploratorio de datos nos proporcionará una buena comprensión de nuestro conjunto de datos y nos ayudará a preparar los datos de manera adecuada para la construcción de  los modelos de clasificación.


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






