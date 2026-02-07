# gestion_ordenadores
Módulo Gestión Ordenadores 

Permite administrar el ciclo de vida de los ordenadores corporativos y sus componentes. 

Arquitectura de Datos (Modelos) 

1. Componentes (gestion.componente) 

Tabla maestra de hardware. 

Campos: Nombre técnico, Especificaciones, Precio y Moneda. 

2. Etiquetas S.O. (gestion.sistema_operativo) 

Clasificación visual. 

Campos: Nombre del sistema y Color de etiqueta. 

3. Ordenadores (gestion.ordenador) 

Ficha principal del activo. 

Identificación: Número de equipo (Único/Requerido). 

Asignación: Usuario responsable (res.users). 

Hardware: Lista de componentes instalados (Relación Many2many). 

Control Temporal: Fecha de última modificación (Manual con validación). 

Valoración: Precio total calculado automáticamente (campo Computed). 

Lógica Programada 

Automatización: Función  

_compute_total que agrega los costes de los componentes vinculados. 

Integridad: Función  

_comprobar_fecha que valida (vía Python Constraint) que las fechas introducidas no sean futuras. 

Interfaz (Vistas) 

Uso de vistas de Lista y Formulario para todos los modelos. 

Implementación de widgets de etiquetas para una gestión visual de los Sistemas Operativos. 

 
