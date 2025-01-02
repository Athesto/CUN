# **Actividad de Construcción Aplicada (ACA)**

## **Documento para descargar**
[Link a Google Drive](https://docs.google.com/document/d/1Zvc7S0pE46XbeI_AzB634Ag42bVbHRhuoOwTgJTJ2dw/edit?usp=sharing)

## **Autores**
- **Gustavo Adolfo Mejía Sánchez**
- **Pedro Pérez**

## **Asignatura**
- **Fundamentos de Programación / 56615 / Primer Bloque / 24V06**

## **Docente**
- **Camilo Augusto Cardona Patiño**

## **Institución**
**Corporación Unificada Nacional de Educación Superior (CUN)**  
**Programa Técnico Profesional en Soporte de Sistemas e Informática - Jornada Única**  
**Diciembre 30 del 2024, Bogotá, Colombia**

---

## **Contenido**
Este repositorio contiene las soluciones a los ejercicios planteados en la actividad de construcción aplicada (ACA). Cada solución incluye:  
1. Una cita del ejercicio solicitado.  
2. Un enlace permanente al repositorio de GitHub.  
3. Una imagen del código de la solución.  
4. Un análisis detallado del código.  
5. Un enlace con el código ejecutándose en un ambiente preestablecido usando pruebas unitarias.  

---

### **Ejercicios Resueltos**

#### **Ejercicio 3a: Clasificar un número como positivo, negativo o cero**
- **Descripción:** Programa que clasifica un número ingresado por el usuario utilizando condicionales `if`, `elif`, y `else`.  
- **[Link Permanente al Código](#)**  
- **Análisis:**  
  La función `solution_3a` utiliza la función `input` para capturar un número del usuario, lo convierte a entero y evalúa si es mayor, menor o igual a 0 para retornar "positive", "negative" o "zero".

---

#### **Ejercicio 3b: Calcular el IMC**
- **Descripción:** Programa que calcula el Índice de Masa Corporal (IMC) y clasifica el resultado según las categorías de la OMS.  
- **[Link Permanente al Código](#)**  
- **Análisis:**  
  El código captura el peso y la altura del usuario, calcula el IMC utilizando la fórmula estándar y clasifica el resultado en "Bajo peso", "Peso normal", "Sobrepeso", u "Obesidad".

---

#### **Ejercicio 3c: Calcular el factorial de un número**
- **Descripción:** Programa que calcula el factorial de un número utilizando un ciclo `for`.  
- **[Link Permanente al Código](#)**  
- **Análisis:**  
  La función recibe un número, maneja el caso especial para 0, y utiliza un ciclo `for` con acumulador para calcular el factorial.

---

#### **Ejercicio 4c: Generar tabla de multiplicar**
- **Descripción:** Programa que genera la tabla de multiplicar (del 1 al 10) de un número ingresado, utilizando un ciclo `while`.  
- **[Link Permanente al Código](#)**  
- **Análisis:**  
  Se utilizan dos ciclos `while` para iterar sobre multiplicadores y multiplicandos, imprimiendo los resultados formateados.

---

### **Notas Adicionales**

#### **Pruebas Unitarias**
Se incluyeron pruebas unitarias para validar cada solución:
- Se utilizó `unittest` y el decorador `patch` para simular entradas del usuario.
- Se probaron diferentes escenarios para garantizar la correcta ejecución de las funciones.
- **[Link Permanente a las Pruebas](#)**  

---

#### **Validación en un Ambiente Controlado**
El programa también se ejecuta en un ambiente preestablecido usando PyScript, lo que permite observar los resultados de manera interactiva.  
**[Enlace a la Validación en PyScript](https://pyscript.com/@athesto/fundamentos-aca/)**  

---

## **Repositorio del Código**
**[GitHub: Repositorio del Proyecto](https://github.com/Athesto/CUN/blob/main/cursos/fundamentos-de-programacion/README.md)**  
