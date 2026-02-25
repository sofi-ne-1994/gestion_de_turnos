# API REST – Gestión de Turnos Médicos

## Descripción

API REST desarrollada con Python 3, Flask y MySQL para gestionar turnos de una clínica médica. Permite listar médicos, consultar la agenda de un profesional y reservar turnos con validación de disponibilidad.

El proyecto está organizado en capas: routes, controllers, services y repositories, separando responsabilidades y acceso a base de datos.

## Base de Datos

### Deploy:
Para el desarrollo se uso XAMPP para la base de detos y luego se hosteo la db en (https://www.freesqldatabase.com/)
El deploy del proyecto se realizo en Render.

#### Link al deploy:
https://gestion-de-turnos-eeh1.onrender.com/

Base de datos: `clinica`
```python
CREATE  TABLE medicos (  
 id INT AUTO_INCREMENT PRIMARY  KEY,  
 nombre VARCHAR(100),  
 especialidad VARCHAR(100)  
);  
  
CREATE  TABLE turnos (  
 id INT AUTO_INCREMENT PRIMARY  KEY,  
 fecha_hora DATETIME,  
 nombre_paciente VARCHAR(100),  
 medico_id INT,  
  FOREIGN  KEY (medico_id) REFERENCES medicos(id)  
);  
  
INSERT  INTO medicos (nombre, especialidad)  
VALUES    
('Dr. House', 'Diagnóstico'),  
('Dra. Grey', 'Cirugía');
```
## Requisitos

-   Python 3
    
-   Flask
    
-   mysql-connector-python
    
-   MySQL
    

Instalación:

pip install -r requirements.txt

## Endpoints

### GET /medicos

Devuelve la lista de médicos.

Respuesta:
```python
[  
 {  
 "id": 1,  
 "nombre": "Dr. House",  
 "especialidad": "Diagnóstico"  
 }  
]
```
### GET /turnos/<medico_id>

Devuelve los turnos del médico indicado.

Ejemplo:

GET /turnos/1

### POST /turnos

Reserva un turno.

Body requerido:
```python
{  
 "medico_id": 1,  
 "fecha_hora": "2024-12-15 10:00:00",  
 "paciente": "Ana Gomez"  
}
```
Lógica aplicada:

-   Si ya existe un turno en ese horario → HTTP 400 y mensaje "Turno no disponible".
    
-   Si no existe → se guarda el turno y devuelve HTTP 201 con mensaje "Turno confirmado".
    

## Objetivo

Proyecto desarrollado como examen final de la materia Aplicaciones Híbridas, cumpliendo con los requisitos solicitados: API REST con Flask, persistencia en MySQL y validación de lógica de negocio.