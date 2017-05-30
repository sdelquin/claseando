# UT2-A5: Utilizando funciones

La actividad consiste en hacer un programa *python* que gestione las calificaciones de un alumno/a en las actividades de una asignatura.

Habrá que mostrar un menú con las siguientes opciones:

1. Añadir calificación `add_mark(marks, mark)`
2. Mostrar las calificaciones `show_marks(marks)`
3. Calcular la media de las calificaciones `get_avg(marks)`
4. Calcular el número de actividades aprobadas `get_passed_assignments(marks)`
5. Mostrar las actividades con mejor calificación `show_best_assignments(marks)`
5. Mostrar las actividades con peor calificación `show_worst_assignments(marks)`
6. Mostrar las actividades con calificación superior a la media `show_above_avg_assignments(marks)`
7. Consultar la nota de una actividad determinada `get_assignment_mark(marks, assignment_id)`
8. Modificar la nota de una actividad determinada `modify_mark(marks, assignment_id, mark)`
8. FINALIZAR LA EJECUCIÓN DEL PROGRAMA.

**NOTAS**:
- Las actividades se identificarán por su número, empezando en 0.
- Las funciones que empiezan por:
  - `show` tendrán `print` en su cuerpo.
  - `get` devuelven un valor.
- Las calificaciones se guardarán en la variable `marks` que estará definida en la función `menu`.
- En el apartado de la media de las calificaciones, se permite el uso de la *built-in function* `sum`.
- En los apartados de mejor y peor calificación, se permite el uso de las *built-in functions* `min` y `max`.

## Ficheros a entregar

Se deberán subir 2 ficheros:

1. `<fichero>.py` con el código de tu programa.
2. `<fichero>.pdf` con el código fuente de tus programas.


