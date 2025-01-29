## LittleLemon API

A Django-based Back-End Project implementing Menu and Booking APIs with authentication and unit testing.

---

### Features
- **Menu API:** CRUD operations for menu items.
- **Booking API:** Manage table reservations.
- **Authentication:** User registration, login, and token-based authentication via Djoser.
- **Unit Testing:** Automated tests for models and views.
- **Django Admin:** Superuser access for managing users and database.

---

### Setup Instructions
**Clone the Repository**
   ```sh
   git clone https://github.com/ii5ii/Capstone-project.git
   cd Capstone-project
   ```


**Create a virtual environment**
  ```sh
  python -m venv myenv
  ```

**Activate the virtual environment**
  - On Windows:
    ```sh
    myenv\Scripts\activate
    ```
  - On macOS and Linux:
    ```sh
    source myenv/bin/activate
    ```

**Install dependencies**
  ```sh
  pip install -r requirements.txt
  ```


**Create a superuser**
  ```sh
  python manage.py createsuperuser
  ```

**Start the development server**
  ```sh
  python manage.py runserver
  ```


**Access the admin interface**
  ```sh
  http://127.0.0.1:8000/admin/
  ```
---
### API Endpoints

#### Authentication (Djoser)

- **User registration**
  ```http
  POST /auth/users/
  ```

- **Obtain token**
  ```http
  POST /auth/token/login/
  ```

- **Logout**
  ```http
  POST /auth/token/logout/
  ```

#### Menu API

- **List all menu items**:
    ```http
    GET /restaurant/menu/
    ```

- **Create new menu item (Admin only)**
    ```http
    POST /restaurant/menu/
    ```

- **Retrieve single menu item**
    ```http
    GET /restaurant/menu/{id}/
    ```

- **Update menu item (Admin only)**
    ```http
    PUT /restaurant/menu/{id}/
    ```

- **Delete menu item (Admin only)**
    ```http
    DELETE /restaurant/menu/{id}/
    ```
