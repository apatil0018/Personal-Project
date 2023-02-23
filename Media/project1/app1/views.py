from django.shortcuts import render,redirect
from app1.forms import StudentForm
from app1.models import Student
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


# Create your views here.
def StudentView(request):
    form = StudentForm()
    template_name = 'app1/student.html'
    context = {'form': form}
    if request.method == "POST":
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('ss_url')
    return render(request, template_name, context)

def ShowStudentView(request):
    data = Student.objects.all()
    template_name = 'app1/showstudent.html'
    context = {'data': data}
    return render(request, template_name, context)

def indexView(request):
    posts = Student.objects.all()  # fetching all post objects from database
    p = Paginator(posts, 1)  # creating a paginator object
    # getting the desired page number from url
    page_number = request.GET.get('page')
    try:
        page_obj = p.get_page(page_number)  # returns the desired page object
    except PageNotAnInteger:
        # if page_number is not an integer then assign the first page
        page_obj = p.page(1)
    except EmptyPage:
        # if page is empty then return last page
        page_obj = p.page(p.num_pages)
    context = {'page_obj': page_obj}
    # sending the page object to index.html
    return render(request, 'app1/index.html', context)



