# ds-aspacia
Repositorio con actividades y tareas del bootcamp data science de Talento Digital

### Distribucion normal estandar

Es una distribucion 'normal' de valores estandarizados llamados puntuaciones **Z** esta se mide en unidades de la desviacion tipica.

*Ejemplo*: Si tenemos una distribucion normal de media 5 y desviacion tipica de 2 entonces el valor de 11 se encuentra a 3 desviaciones tipicas sobre la media, el calculo es el sgte:

$x=\mu + (z)(\sigma) = 5 +(3)(2) = 11$

La puntuacion Z es igual a tres.

$Z=\frac{x-\mu}{\sigma}$

#### Regla empirica de la distribucion normal
**Para una destribucion normal**

- Aproximadamente el 68% de los valores de x se situan entre $-1\sigma$ y $+1\sigma$ de la media $\mu$.
- Aproximadamente el 95% de los valores de x se situan entre $-2\sigma$ y $+2\sigma$ de la media $\mu$.
- Aproximadamente el 99.7% de los valores de x se situan entre $-3\sigma$ y $+3\sigma$ de la media $\mu$.

**Recordar 68-95-99.7 $\sigma$ Equivalente a 1-2-3 Z**

### Teorema del limite central

El teorema del limite central indica que si se extraen muestras repetidamente de un tamaño determinado y se calculan sus medias estan tenderan a tener una distribucion normal en torno a la media poblacional y mientras mas muestras son utilizadas esta se aproxima mas a la normal. Asi la distribucion normal de medias tendria una media similar a la media poblacional y una desviacion tipica igual a la desviacion tipica dividida en la raiz cuadrada del tamaño del muestra.

Para sintetizar, si se extraen muestras aleatorias de tamaño n un numero determinado de veces y se calculan sus medias por separado, la distribucion de esta medias se denomina **distribucion muestral de la media**. De esto se desprednde que la distribucion de la variable aleatoria $\overline{x}$ tiene asociado una puntuacion **Z** diferente a la variable X:

<p align="center">
    $\Huge z=\frac{\overline{x}-\mu_x}{(\frac{\mu_x}{\sqrt{n}})}$
</p>

- $\mu_x es el promedio de X y $\overline{x}$

- $\mu\overline{x}$ = $\frac{\muX}{\sqrt{n}}$ = desviación típica de $\overline{x}$ y se denomina error estándar de la media.

### Prueba de hipotesis estadistica 

Es un procedimiento que busca tomar una desicion sobre el valor de verdad de una hipotesis estadistica.

**Ejemplo**

Supongamos que en una fabrica de galletas el peso impreso dice 500 gr pero en realidad el peso varia de forma aleatoria alrededor de ese peso impreso.
El fabricante afirma que la media de peso es de 500 gr $\mu=500$ con una desviacion estandar de 5 gr $\sigma=5$. Se quiere analizar si el peso real promedio es menor al anunciado por el fabricante.

La variable a analizar es X: peso en gramos de un paquete de galletas de dicha fabrica.

**La hipotesis**

- Hipotesis nula: La media de X es de 500: $\mu=500$}
- Hipotesis alternativa: La media de X es menor que 500: $\mu<500$

**Estimando el valor***

Tomamos ua muestra aleatoria de 100 valores $n=100$ y se toma su peso, asi obtenemos una muestra aleatoria de la variable $X$

$X1, X2, X3..., X100$

Como la media muestral $\overline{X}$ es un buen estimador de la media poblacional $\mu$ se calcula la media de los 100 paquetes para contrastar la hipotesis nula.

- Si obtenemos un valor de $\overline{X}$ muy inferior a 500 es decir una diferencia $\overline{x}-\mu$ muy grande, se rechaza la hipotesis.

- Si obtenemos un valor de $\overline{X}$ muy cercano a 500 es decir una diferencia $\overline{x}-\mu$ pequeña, no hay suficiente evidencia para rechazar la hipotesis nula.

**Abordaje formal**

Para establecer el punto de corte de manera formal se tiene que establecer primero algunos conceptos:

**Variable**

Es una caracteristica de interes de un objeto, sujeto o poblacion.

**Parametro**

En estadistica, es un valor constante asociado a la distribucion de probabilidades de una variable aleatoria. Algunos ejemplos de parametros son media, desviacion estandar, taza de exitos, etc.

**Estimador de parametro**

Es un estadistico (estadistico: variable aleatoria funcion de las observaciones muestrales) que toma **valores cercanos** al verdadero valor del parametro. De los cuales nos interesan:

- Media muestral $\overline{x}$ es un estimador de la media poblacional $\mu$
- Desvio estandar muestral $s$ es un estimador del desvio estandar poblacional $\sigma$
- Proporcion muestral $\hat{p}$

**Estadistico de prueba**

Es una variable aleatoria, de distribucion conocida y que vincula a un parametro de interes con un estimador de ese parametro.

