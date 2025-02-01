from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
import firebase_admin
from firebase_admin import credentials, db

# Initialize Firebase
cred = credentials.Certificate("E:/Projects/simple-data-entry-application/demo/credentials.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': '' # Add URL to Firebase Database
})

def home(request):
    ref = db.reference('tasks')
    tasks = ref.get() or {}
    task_list = [{"id": task_id, **task_data} for task_id, task_data in tasks.items()]  
    return render(request, "home.html", {"tasks": task_list})


def add_task(request):
    if request.method == "POST":
        task_name = request.POST.get("task")
        description = request.POST.get("description", "")
        due_date = request.POST.get("due_date")
        status = False
        
        ref = db.reference('tasks')
        new_task = ref.push()
        new_task.set({
            "name": task_name,
            "description": description,
            "due_date": due_date,
            "status": status
        })
        
        return redirect('home')
    return HttpResponse("Invalid Request", status=400)


def toggle_status(request, task_id):
    ref = db.reference(f'tasks/{task_id}')
    task = ref.get()
    if task:
        ref.update({"status": not task["status"]})
    return redirect('home')


def delete_task(request, task_id):
    ref = db.reference(f'tasks/{task_id}')
    ref.delete()
    return redirect('home')
