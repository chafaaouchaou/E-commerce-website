**Project Name:** E-commerce Website

**Description:**

This is a full-stack e-commerce website built using Django and React. The backend (API) utilizes Django REST Framework for robust API development. The frontend leverages React for a dynamic and user-friendly shopping experience.

**Technologies:**

* **Backend:**
    * Python 
    * Django 
    * Django REST Framework 
* **Frontend:**
    * React 
    * React Router 
    * Axios

**Prerequisites:**

* **Python:** Ensure you have Python installed. You can download it from [https://www.python.org/downloads/](https://www.python.org/downloads/).
* **Node.js and npm:** Install Node.js from [https://nodejs.org/en](https://nodejs.org/en). npm (Node Package Manager) comes bundled with Node.js.

**Installation:**

1. **Backend (Django):**
   * Clone this repository: `git clonehttps://github.com/chafaaouchaou/E-commerce-website.git` 
   * Navigate to the project directory: 
   * Create a virtual environment (recommended): `python -m venv venv`
   * Activate the virtual environment: `source venv/bin/activate` (Windows: `venv\Scripts\activate`)
   * Install required dependencies: `pip install -r ecom/requirements.txt`
   * Apply database migrations (create tables): `python manage.py makemigrations` followed by `python manage.py migrate`
   * Run the development server: `python manage.py runserver` (This will typically start the server at https://ecomapi.chafaaouchaou.online/)

2. **Frontend (React):**
   * Open a separate terminal/command prompt.
   * Navigate to the frontend directory
   * Install project dependencies: `npm install`
   * Start the development server: `npm run dev` 

**Running the Application:**

1. **Development:**
   * With both backend and frontend servers running, you can access your application in the browser at the URLs mentioned in the installation step.
   * Make changes to the codebase and the servers will automatically reload, reflecting your updates.

2. **Production:**
   * Refer to Django and React documentation for deployment instructions specific to your chosen hosting platform. This typically involves configuring production settings, potentially building static assets for the frontend, and deploying to a web server.

**Additional Notes:**

* This README is a basic guide. Refer to Django and React documentation for more in-depth setup and configuration options:
   * Django: [https://docs.djangoproject.com/en/5.0/](https://docs.djangoproject.com/en/5.0/)
   * React: [https://legacy.reactjs.org/docs/getting-started.html](https://legacy.reactjs.org/docs/getting-started.html)

**Contribution:**

* Feel free to create pull requests for improvements or bug fixes.
