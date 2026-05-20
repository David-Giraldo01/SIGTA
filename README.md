📚 SIGTA
Sistema Inteligente de Gestión de Tareas Académicas
📌 Introducción

SIGTA es un proyecto desarrollado en Python que busca dar solución a una problemática común entre estudiantes universitarios: la dificultad para gestionar adecuadamente tareas académicas, fechas de entrega y prioridades dentro de múltiples asignaturas.                                                                     

Actualmente, muchos estudiantes administran sus actividades mediante agendas físicas, aplicaciones dispersas o recordatorios poco organizados, generando olvidos, incumplimientos y dificultades para priorizar responsabilidades académicas.                                                                                      

 
Esta situación puede afectar el rendimiento estudiantil, especialmente en periodos con alta carga académica, donde existen múltiples entregas simultáneas, parciales y proyectos.


En respuesta a esta necesidad, SIGTA propone un sistema inteligente para la gestión de tareas académicas que permite registrar actividades, calcular prioridades según fechas de entrega, generar alertas, administrar estados de tareas y facilitar el seguimiento de compromisos académicos mediante una interfaz gráfica amigable.


El sistema incorpora inicio de sesión, gestión centralizada de tareas y herramientas orientadas a mejorar la organización estudiantil.


Este proyecto fue desarrollado aplicando el paradigma de Programación Orientada a Objetos (POO), permitiendo modelar estructuradamente componentes del sistema como usuarios, tareas, gestores y priorizadores.


🚀 Características

🔐 Sistema de inicio de sesión (Login)

📝 Registro de tareas académicas

📅 Gestión de fechas de entrega

⚡ Priorización automática de tareas según tiempo restante

✅ Cambio de estado (Pendiente / Completada)

🗑️ Eliminación de tareas

📊 Gestión centralizada de actividades académicas

🚨 Sistema de alertas para tareas próximas a vencer

🖥️ Interfaz gráfica amigable mediante Tkinter

📚 Organización por materias académicas

🧠 Tecnologías utilizadas

Python 🐍

Programación Orientada a Objetos (POO)

Tkinter (Interfaz gráfica)

Git & GitHub (Control de versiones)

PyCharm (Entorno de desarrollo)

🏗️ Estructura del proyecto

El sistema está basado en clases principales como:

Modelo

Usuario

Gestiona credenciales e inicio de sesión.

Tarea

Representa cada actividad académica.
Contiene información como:
Nombre
Materia
Fecha de entrega
Estado
Prioridad

Priorizador

Calcula automáticamente la prioridad:
Alta
Media
Baja
Vencida

GestorTareas

Administra:
Creación
Listado
Eliminación
Actualización
Alertas
Interfaz

Login

Maneja autenticación de usuario.

VentanaPrincipal

Gestiona interacción con el usuario mediante interfaz gráfica.

▶️ Ejecución del proyecto
Clonar el repositorio:
git clone URL_DEL_REPOSITORIO
Ingresar al proyecto:
cd SIGTA
Ejecutar:
python main.py
👨‍💻 Autores

Desarrollado por:

Yeisner David Giraldo
Jean Paul Arteaga

Proyecto académico — Programación Orientada a Objetos (POO)
