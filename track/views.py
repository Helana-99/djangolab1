from django.shortcuts import render

def track_list(request):
    tracks = [
        {"id": 1, "name": "os", "description": "Html, JS, Css"},
        {"id": 2, "name": "html", "description": "Ubuntu"},
        {"id": 3, "name": "java", "description": "Python, Django"},
    ]
    context = {"tracks": tracks}
    return render(request, "track/trackList.html", context)

def create_track(request):
    return render(request, "track/createTrack.html")

def update_track(request, id):
    context = {"id": id}
    return render(request, "track/updateTrack.html", context)

def delete_track(request, id):
    context = {"id": id}
    return render(request, "track/deleteTrack.html", context)

def track_detail(request, id):
    context = {"id": id}
    return render(request, "track/trackDetail.html", context)
