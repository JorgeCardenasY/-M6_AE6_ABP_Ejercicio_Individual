# Proyecto Tienda Online

## 🚀 Descripción General del Proyecto

Este proyecto corresponde a una aplicación web de una tienda online, desarrollada con el framework Django. Su propósito principal es simular un comercio electrónico básico, permitiendo a los usuarios explorar productos, agregarlos a un carrito de compras y finalizar un proceso de pedido. Se ha puesto énfasis en la implementación de las funcionalidades esenciales que se encuentran en la mayoría de las plataformas de e-commerce, buscando una experiencia de usuario intuitiva y un backend robusto para la gestión de la información.

## ✨ Características y Requerimientos Cumplidos

A continuación, se detallan las características implementadas en el proyecto y cómo cada una de ellas aborda los requerimientos iniciales:

### 🛍️ Listado de Productos

La plataforma presenta un listado completo de los productos disponibles. Cada producto se muestra con su nombre, una breve descripción y su precio.

*   **Implementación:** Se utiliza un modelo `Producto` en `gestion/models.py` para almacenar la información de cada artículo. La vista `gestion/views.py` se encarga de recuperar todos los productos de la base de datos y pasarlos a una plantilla HTML que los renderiza de forma dinámica.

### 🔍 Detalle de Producto

Al seleccionar un producto del listado, el usuario puede acceder a una página dedicada que muestra información más detallada del artículo, incluyendo imágenes adicionales (si las hubiera), una descripción extendida y opciones para agregarlo al carrito.

*   **Implementación:** Una vista específica en `gestion/views.py` recibe el ID del producto como parámetro, consulta la base de datos para obtener sus detalles y los presenta en una plantilla HTML diseñada para este fin.

### 🛒 Carrito de Compras

Los usuarios tienen la posibilidad de agregar productos a un carrito de compras virtual. Este carrito permite visualizar los artículos seleccionados, ajustar las cantidades y eliminar productos antes de proceder con la compra.

*   **Implementación:** Se gestiona el carrito de compras a través de sesiones de Django. Cada vez que un usuario agrega un producto, se actualiza la información en la sesión, manteniendo un registro de los productos y sus cantidades.

### 💳 Proceso de Compra

Una vez que el usuario ha finalizado la selección de productos en su carrito, puede iniciar el proceso de compra. Este flujo incluye la confirmación de los artículos, la introducción de datos de envío y la simulación de un pago.

*   **Implementación:** Se han desarrollado vistas y formularios específicos para guiar al usuario a través de los pasos del checkout. La información del pedido se guarda en un modelo `Pedido` en la base de datos una vez que el proceso se completa.

### 👤 Autenticación de Usuarios

La aplicación incorpora un sistema de autenticación que permite a los usuarios registrarse, iniciar sesión y cerrar sesión. Esto es fundamental para personalizar la experiencia y asociar los pedidos a un usuario específico.

*   **Implementación:** Se utilizan las funcionalidades de autenticación de usuarios que Django provee por defecto, incluyendo vistas para registro, login y logout, y la gestión de usuarios a través del modelo `User` integrado.

### ⚙️ Panel de Administración

Existe un panel de administración robusto que permite a los administradores gestionar productos, usuarios, pedidos y otras configuraciones de la tienda.

*   **Implementación:** Django Admin se utiliza para proporcionar una interfaz de administración completa. Los modelos `Producto`, `Pedido`, `Usuario` (si se extiende el modelo User) se registran en `gestion/admin.py` para ser gestionados desde este panel.

## 🛠️ Tecnologías Utilizadas

*   **Backend:** Python 3.x, Django 5.x
*   **Base de Datos:** SQLite (para desarrollo, configurable para producción)
*   **Frontend:** HTML5, CSS3, JavaScript (básico)

## 🚀 Instalación y Configuración

Para poner en marcha este proyecto en tu entorno local, sigue los siguientes pasos:

1.  **Clonar el repositorio:**
    ```bash
    git clone <URL_DEL_REPOSITORIO>
    cd tienda
    ```
2.  **Crear un entorno virtual e instalar dependencias:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # En Windows: venv\Scripts\activate
    pip install -r requirements.txt # Asumiendo que existe un archivo requirements.txt
    ```
    Si no existe `requirements.txt`, puedes instalar Django manualmente:
    ```bash
    pip install Django
    ```
3.  **Realizar migraciones de la base de datos:**
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```
4.  **Crear un superusuario (administrador):**
    ```bash
    python manage.py createsuperuser
    ```
    Sigue las instrucciones en pantalla para crear el usuario administrador.

5.  **Ejecutar el servidor de desarrollo:**
    ```bash
    python manage.py runserver
    ```
    La aplicación estará disponible en `http://127.0.0.1:8000/`.

## 🌐 Uso de la Aplicación

Una vez que el servidor esté en funcionamiento, se puede acceder a la tienda a través del navegador. Los usuarios pueden navegar por los productos, agregarlos al carrito y simular el proceso de compra.

## 🔒 Acceso al Panel de Administración

Para acceder al panel de administración de Django, se debe navegar a `http://1127.0.0.1:8000/admin/`.

**Credenciales de Acceso (Ejemplo):**

*   **Usuario:** `root`
*   **Contraseña:** `admin`

**¡Importante!** Se recomienda encarecidamente cambiar estas credenciales por defecto en un entorno de producción para garantizar la seguridad de la aplicación.

## 📝 Consideraciones Adicionales

Este proyecto sirve como una base para una tienda online. Se pueden añadir funcionalidades adicionales como un landing page, pasarelas de pago, gestión de inventario más avanzada, sistemas de recomendación, entre otros, para expandir sus capacidades.