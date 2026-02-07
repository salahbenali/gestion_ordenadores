# Documentación: Gestión de Equipos


## Estructura de Archivos
El módulo se organiza en las carpetas estándar de Odoo:
*   `models/`: Contiene la lógica en Python (Clases y funciones).
*   `views/`: Contiene la interfaz en XML (Formularios y listas).
*   `security/`: Define quién puede acceder (listas de control de acceso).

## Explicación del Código (Modelos)

### 1. Modelo de Ordenadores (`models/computer.py`)
Es la clase principal `gestion.ordenador`. Sus funcionalidades clave son:

*   **Cálculo Automático de Precio (`_compute_total`)**:
    *   **Funcionamiento**: Esta función recorre la lista de componentes asignados al ordenador, suma sus precios y actualiza el campo `precio`.
    *   **Disparador**: Se ejecuta automáticamente cada vez que se modifica la lista de componentes (gracias al decorador `@api.depends`).

*   **Validación de Fechas (`_comprobar_fecha`)**:
    *   **Funcionamiento**: Compara la fecha de "Última modificación" (introducida manualmente) con la fecha actual del servidor.
    *   **Restricción**: Si la fecha es futura, lanza un error (`ValidationError`) e impide guardar el registro.

### 2. Modelo de Componentes (`models/component.py`)
Clase simple `gestion.componente` que actúa como maestro de datos. Almacena el nombre y precio base de cada pieza.

## Explicación de la Interfaz (Vistas)
Las vistas se han diseñado en XML (`views/computer_views.xml`) utilizando etiquetas `<notebook>` y `<page>` para organizar la información en pestañas, mejorando la usabilidad.

## Instrucciones de Uso
1.  **Componentes**: Ir al menú y crear las piezas (Hardware).
2.  **Ordenadores**: Crear un nuevo equipo, asignar un usuario y añadir componentes.
3.  **Verificación**: Comprobar que el "Precio Total" se calcula solo al guardar.
