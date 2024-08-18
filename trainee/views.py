from django.shortcuts import render

def trainees_list(request):
    trainees = [
        {"id": 1, "name": "Helana", "age": 22, "email": "helana.nabil@hotmail.com", "department": "OS"},
        {"id": 2, "name": "Marina", "age": 24, "email": "marina@gmail.com", "department": "HTML"},
        {"id": 3, "name": "Sara", "age": 25, "email": "sara.nabil@gmail.com", "department": "Java"},
    ]
    context = {"trainees": trainees}
    return render(request, "trainee/traineesList.html", context)

def create_trainee(request):
    return render(request, "trainee/createTrainee.html")

def update_trainee(request, id):
    context = {"id": id}
    return render(request, "trainee/updateTrainee.html", context)

def delete_trainee(request, id):
    context = {"id": id}
    return render(request, "trainee/deleteTrainee.html", context)

def trainees_details(request, id):
    context = {"id": id}
    return render(request, "trainee/traineeDetails.html", context)
