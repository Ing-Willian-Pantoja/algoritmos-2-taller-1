Experimento y resultados
al comparar listas y arrays, note que los arrays de numpy fueron mas rapidos al realizar operaciones matematicas sobre grandes volumenes de datos Las listas tambien funcionan, pero tardan mas porque estan diseñadas para ser mas flexibles y almacenar diferentes tipos de informacion.

diferencias en tiempo de ejecucion
el tiempo de ejecucion con arrays fue menor, esto se debe a que numpy esta optimizado en C y maneja los datos de forma mas compacta en memoria, mientras que las listas de python son mas generales y requieren más pasos internos para procesar cada elemento.

influencia de la memoria
las listas guardan cada elemento como un objeto independiente, lo que ocupa mas espacio y hace que las operaciones sean más lentas, Los arrays, en cambio, almacenan los datos de manera continua en memoria, lo que permite que las operaciones matematicas se ejecuten mas rapido.

eleccion para grandes volumenes de datos
si tuviera que elegir, usaría arrays de numpy porque son mas eficientes para calculos nuericos y permiten trabajar con grandes cantidades de datos sin que el programa se vuelva lento, Las listas las dejaria para casos donde necesito almacenar diferentes tipos de informacion, no solo numeros.