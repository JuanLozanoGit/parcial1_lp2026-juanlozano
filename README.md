# parcial1_lp2026-juanlozano


### 1. AFD Movimientos de Ajedrez

```bash
python3 AFDajedrez-punto1.py

```

### 2. AFD Identificadores (IDs)

```bash
python3 AFDidentificadores-punto2.py

```

### 3. Calculadora de Raíz Cuadrada (Flex & Bison)

```bash

bison -d calc.y
flex calc.l
gcc calc.tab.c lex.yy.c -o calculadora -lm
./calculadora < entrada.txt

```

### 4. Benchmark de Rendimiento (C vs Python)


```bash

gcc -O3 bench.c -o bench_c
./bench_c
python3 bench.py

```

### 5. Secuencia Fibonacci (ANTLR4 + Python)

```bash

java -jar antlr-4.13.1-complete.jar -Dlanguage=Python3 -no-listener -visitor Fibo.g4
python3 fibologica.py

```

### NOTA: Para poder correr el 5, toca escribir la abreviatura de FIBO mas un numero, ejemplo. FIBO(20)  Sino dara un error.




### SOLUCIONES:

Puntos 1 y 2 (Autómatas finitos deterministas): Fueron implementados mediante lógica de transiciones de estados en Python, permitiendo validar cadenas complejas (notación ajedrecística) y procesar lotes de identificadores desde archivos externos.

Punto 3 (Flex & Bison): Fueron utilizados un analizador léxico (Flex) para tokenizar la función SQRT y un analizador gramatical (Bison) para procesar la expresión gramatical. La lógica de cálculo basa en el método de Newton-Raphson en C para garantizar la precisión matemática.

Punto 4 (Benchmark): La comparación confirma que C (optimizado con -O3) trae rendimientos mejores que Python en el uso de algoritmos recursivos debido a la gestión lineal de la memoria y la no presencia del sobrecoste del intérprete, con tiempos hasta 50 veces menores.

Punto 5 (ANTLR4): Se definió una gramática formal en el archivo Fibo.g4, que fue integrado con Python mediante el patrón Visitor, permitiendo que el script fibologica.py recorra el árbol de sintaxis, valide la instrucción FIBO(n) y genere la secuencia numérica solicitada con garantías.
