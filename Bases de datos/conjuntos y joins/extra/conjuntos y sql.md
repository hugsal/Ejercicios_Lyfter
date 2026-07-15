## Explicación cruzada entre conjuntos y SQL

All = {1,2,3,4,5,6,7,8,9,10}

Odd = {1,3,5,7,9}

Analice la operación de conjuntos All - Odd.

Explique cómo una operación similar se puede representar en SQL con JOINs.

Se peude representar con JOINS debido a que SQL hace una comparacion entre las tablas y dependiendo de la condicion nos va a devovler los elementos que cumplan con la condicion. 

¿Qué tipo de JOIN usaría?

se usaria un LEFT JOIN. Al usar un LEFT JOIN estamos selecionando todos los elementos de la tabla izquierda(All) y los elementos de la tabla derecha(Odd) que cumplan con la condicion. 

