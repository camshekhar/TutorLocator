from django.shortcuts import render
from .models import FacultyDetail

# Create your views here.
courses = ['python','dbms','maths','java','physics','chemistry','c++','javascript', 'geography', 'gs', 'history']
cities = ['pune','nagpur','mumbai']
    
def home(request):
    faculties = FacultyDetail.objects.all()
    context = {
        'faculties': faculties,
        'cities': cities,
        'courses':courses
    }
   
    return render(request, 'index.html', context=context)

def filterFaculty(request):
    filter_city = request.GET['city']
    filter_course = request.GET['course']

    faculties = FacultyDetail.objects.filter(city=filter_city)
    filter_faculties = []
    
    for faculty in faculties:
        i=0
        # print(faculty.courses.split(',')[0].lstrip())
        if faculty.courses.split(',')[i].lstrip().lower() == filter_course.lower():
            filter_faculties.append(faculty)
            i = i+1

    context = {
        'faculties': filter_faculties,
        'cities': cities,
        'courses':courses,
        'filter_city':filter_city,
        'filter_course':filter_course
    }
    # print(filter_faculties)
    return render(request, 'index.html', context=context)