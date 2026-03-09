# parcial1_lp2026-juanlozano


### 1. AFD Movimientos de Ajedrez

Valida notación algebraica de ajedrez.

```bash
python3 AFDajedrez-punto1.py

```

### 2. AFD Identificadores (IDs)

Valida identificadores usando una lista de pruebas externa.

```bash
# Requiere el archivo pruebas_id.txt en la carpeta
python3 AFDidentificadores-punto2.py

```

### 3. Calculadora de Raíz Cuadrada (Flex & Bison)

Implementación del método **Newton-Raphson** para cálculo de raíces.

```bash
# 1. Generar código C
bison -d calc.y
flex calc.l
# 2. Compilar (incluyendo librería matemática -lm)
gcc calc.tab.c lex.yy.c -o calculadora -lm
# 3. Ejecutar con archivo de entrada
./calculadora < entrada.txt

```

### 4. Benchmark de Rendimiento (C vs Python)

Comparativa de velocidad calculando Fibonacci(40) de forma recursiva.

```bash
# Compilar C con optimización máxima
gcc -O3 bench.c -o bench_c
./bench_c

# Ejecutar Python
python3 bench.py

```

### 5. Secuencia Fibonacci (ANTLR4 + Python)

Gramática para procesar el comando `FIBO(n)` y devolver la secuencia.

```bash
# 1. Generar archivos base desde el JAR (Respetar mayúscula de Fibo.g4)
java -jar antlr-4.13.1-complete.jar -Dlanguage=Python3 -no-listener -visitor Fibo.g4

# 2. Ejecutar el programa (Bucle infinito con manejo de errores)
python3 fibologica.py

```

### NOTA: Para poder correr el 5, toca escribir la abreviatura de FIBO mas un numero, ejemplo. FIBO(20)  Sino dara un error.
