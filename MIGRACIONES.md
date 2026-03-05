# Guía de Migraciones con Flask-Migrate

Esta aplicación usa **Flask-Migrate** para gestionar cambios en la base de datos de forma segura y versionada.

## Comandos Principales

### 1. Inicializar migraciones (primera vez)
```bash
flask db init
```
Crea la carpeta `migrations/` con la configuración necesaria.

### 2. Crear una nueva migración después de cambios en modelos
```bash
flask db migrate -m "Descripción del cambio"
```
**Ejemplo:**
```bash
flask db migrate -m "Agregar campo email a usuarios"
```
Esto genera un archivo Python en `migrations/versions/` con los cambios detectados.

### 3. Aplicar migraciones a la base de datos
```bash
flask db upgrade
```
Ejecuta todas las migraciones pendientes y actualiza la base de datos.

### 4. Deshacer la última migración
```bash
flask db downgrade
```

### 5. Ver estado actual de las migraciones
```bash
flask db current
```

### 6. Ver historial de migraciones
```bash
flask db history
```

## Flujo de Trabajo típico

1. **Modificar un modelo** en `app/models.py`
   ```python
   class Producto(db.Model):
       id = db.Column(db.Integer, primary_key=True)
       nombre = db.Column(db.String(100), nullable=False)
       precio_venta = db.Column(db.Float, nullable=False)
       # Nuevo campo
       descripcion = db.Column(db.String(500))
   ```

2. **Generar migración**
   ```bash
   flask db migrate -m "Agregar campo descripción a productos"
   ```

3. **Revisar el archivo generado** en `migrations/versions/`
   - Asegúrate de que los cambios sean correctos

4. **Aplicar migración**
   ```bash
   flask db upgrade
   ```

## Estructura actual

- **Tabla Users**: Creada inicialmente con `db.create_all()`
- **Tabla Productos**: Creada con migración `001_init`
  - Campo `id` (Integer, Primary Key)
  - Campo `nombre` (String 100, no nullable)
  - Campo `precio_venta` (Float, no nullable)

## Recursos
- [Flask-Migrate Documentation](https://flask-migrate.readthedocs.io/)
- [Alembic Documentation](https://alembic.sqlalchemy.org/)
