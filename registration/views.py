from django.shortcuts import render, redirect, get_object_or_404
from .models import course, student, enrollment


# ================= AUTH / GENERAL =================
def login_page(request):
    error = None
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        if username == "admin" and password == "soft":
            request.session['logged_in'] = True
            return redirect("home")
        else:
            error = "Invalid username or password, try again."
            return render(request, "login.html", {"error": error})
    return render(request, "login.html")


def logout_page(request):
    request.session.flush()
    return redirect("login")


def home(request):
    return render(request, "home.html")


def about(request):
    return render(request, "about.html")


# ================= COURSE =================
def course_show(request):
    courses = course.objects.all()
    return render(request, "course_show.html", {"courses": courses})


def course_create(request):
    if request.method == "POST":
        course.objects.create(
            course_name=request.POST.get("course_name"),
            student_name=request.POST.get("student_name"),
            duration=request.POST.get("duration"),
            fees=request.POST.get("fees"),
        )
        return redirect("course_show")

    students = student.objects.all()
    return render(request, "course_create.html", {"students": students})


def course_update(request, cid):
    c = get_object_or_404(course, course_id=cid)
    if request.method == "POST":
        c.course_name = request.POST.get("course_name")
        c.student_name = request.POST.get("student_name")
        c.duration = request.POST.get("duration")
        c.fees = request.POST.get("fees")
        c.save()
        return redirect("course_show")

    students = student.objects.all()
    return render(request, "course_update.html", {
        "course": c,
        "students": students,
    })


def course_delete(request, cid):
    c = get_object_or_404(course, course_id=cid)
    c.delete()
    return redirect("course_show")


# ================= STUDENT =================
def student_show(request):
    students = student.objects.all()
    return render(request, "student_show.html", {"students": students})


def student_create(request):
    if request.method == "POST":
        student.objects.create(
            student_name=request.POST.get("student_name"),
            course_name=request.POST.get("course_name"),
            email=request.POST.get("email"),
            ph=request.POST.get("ph"),
        )
        return redirect("student_show")

    courses = course.objects.all()
    return render(request, "student_create.html", {"courses": courses})


def student_update(request, sid):
    s = get_object_or_404(student, student_id=sid)
    if request.method == "POST":
        s.student_name = request.POST.get("student_name")
        s.course_name = request.POST.get("course_name")
        s.email = request.POST.get("email")
        s.ph = request.POST.get("ph")
        s.save()
        return redirect("student_show")

    courses = course.objects.all()
    return render(request, "student_update.html", {
        "student": s,
        "courses": courses,
    })


def student_delete(request, sid):
    s = get_object_or_404(student, student_id=sid)
    s.delete()
    return redirect("student_show")


# ================= ENROLLMENT =================
def enrollment_show(request):
    enrollments = enrollment.objects.all()
    return render(request, "enrollment_show.html", {"enrollments": enrollments})


def enrollment_create(request):
    if request.method == "POST":
        enrollment.objects.create(
            student_name=request.POST.get("student_name"),
            course_name=request.POST.get("course_name"),
            date=request.POST.get("date"),
        )
        return redirect("enrollment_show")

    students = student.objects.all()
    courses = course.objects.all()
    return render(request, "enrollment_create.html", {
        "students": students,
        "courses": courses,
    })


def enrollment_update(request, eid):
    e = get_object_or_404(enrollment, enrollment_id=eid)
    if request.method == "POST":
        e.student_name = request.POST.get("student_name")
        e.course_name = request.POST.get("course_name")
        e.date = request.POST.get("date")
        e.save()
        return redirect("enrollment_show")

    students = student.objects.all()
    courses = course.objects.all()
    return render(request, "enrollment_update.html", {
        "enrollment": e,
        "students": students,
        "courses": courses,
    })


def enrollment_delete(request, eid):
    e = get_object_or_404(enrollment, enrollment_id=eid)
    e.delete()
    return redirect("enrollment_show")