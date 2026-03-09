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
