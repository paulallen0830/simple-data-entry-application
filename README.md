# Task Manager Web Application

This is a simple and efficient Task Manager web application built using Django and Firebase Realtime Database. The application allows users to add, update, and delete tasks.

## Features

- Add tasks with a name, description (optional), and due date.  
- Toggle task status (Completed/Not Completed) with a single click.  
- Delete tasks from the list.  
- Data persistence using Firebase Realtime Database.  
- Clean and responsive user interface with Tailwind CSS.  

## Technologies Used

- **Backend**: Django, Firebase Admin SDK  
- **Frontend**: HTML, Tailwind CSS
- **Database**: Firebase Realtime Database  

## Installation and Setup

### Prerequisites
Ensure you have Python and Pipenv installed on your system.

### Steps to Set Up the Project

1. **Clone the repository**  
   ```sh
   git clone https://github.com/paulallen0830/simple-task-manager.git
   cd simple-task-manager
   ```

2. **Set up a virtual environment**  
   ```sh
   pipenv install
   pipenv shell
   ```

3. **Install dependencies**  
   ```sh
   pipenv install django firebase-admin
   ```

4. **Configure Firebase**  
   - Download the Firebase Admin SDK JSON file from the Firebase console.  
   - Place it inside the project folder and update `views.py` with the correct file path.  

5. **Run the Django server**  
   ```sh
   python manage.py runserver
   ```

6. **Access the application**  
   Open a web browser and go to: [http://127.0.0.1:8000](http://127.0.0.1:8000)

## Screenshots



## Contributing

Contributions are welcome. If you would like to contribute, please fork the repository and submit a pull request.  
