from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import UserProfile,Project, WorkExperience, Education, Certification
from .forms import UserProfileForm,ProjectForm, WorkExperienceForm, EducationForm, CertificationForm
from django.shortcuts import get_object_or_404


@login_required
def profile(request):
    try:
        
        user_profile = UserProfile.objects.get(user=request.user)
    except UserProfile.DoesNotExist:
        
        return redirect('create_profile')

    context = {
        'user_profile': user_profile,
    }
    return render(request, 'portfolio/profile.html', context)
def edit_profile(request):
    try:
        
        user_profile = UserProfile.objects.get(user=request.user)
    except UserProfile.DoesNotExist:
        user_profile = None

    
    if request.method == 'POST':
        form = UserProfileForm(request.POST,request.FILES, instance=user_profile)
        if form.is_valid():
            form.save()
            return redirect('profile')  
    else:
        form = UserProfileForm(instance=user_profile)

    return render(request, 'portfolio/edit_profile.html', {'form': form,'user_profile': user_profile})

@login_required
def create_profile(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST,request.FILES)
        if form.is_valid():
            user_profile = form.save(commit=False)
            user_profile.user = request.user 
            user_profile.save()  
            return redirect('profile')  
    else:
        form = UserProfileForm() 
    return render(request, 'accounts/profile_creation.html', {'form': form})




def portfolio_setup(request):
    user = request.user
    projects = Project.objects.filter(user=user)
    work_experience = WorkExperience.objects.filter(user=user)
    education = Education.objects.filter(user=user)
    certifications = Certification.objects.filter(user=user)

    return render(request, 'portfolio/portfolio_setup.html', {
        'projects': projects,
        'work_experience': work_experience,
        'education': education,
        'certifications': certifications,
    })

def create_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.user = request.user
            project.save()
            return redirect('project_list')
    else:
        form = ProjectForm()
    return render(request, 'portfolio/create_project.html', {'form': form})

def edit_project(request, project_id):
    project = get_object_or_404(Project, id=project_id, user=request.user)
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            return redirect('project_detail', project_id=project.id)
    else:
        form = ProjectForm(instance=project)
    return render(request, 'portfolio/edit_project.html', {'form': form ,'project': project})

def delete_project(request, project_id):
    project = get_object_or_404(Project, id=project_id, user=request.user)
    if request.method == 'POST':
        project.delete()
        return redirect('portfolio_setup')
    return render(request, 'portfolio/delete_project.html', {'project': project})

def index(request):
    return render(request,'index.html')

def project_list(request):
    project = Project.objects.filter(user=request.user)
    return render(request, 'portfolio/project_list.html', {'project': project})

def project_detail(request, project_id):
    project = get_object_or_404(Project, id=project_id,user=request.user)
    return render(request, 'portfolio/project_details.html', {'project': project})


def work_experience_list(request):
    work_experiences = WorkExperience.objects.filter(user=request.user)
    return render(request, 'portfolio/work_experience_list.html', {'work_experiences': work_experiences})

def create_work_experience(request):
    if request.method == 'POST':
        form = WorkExperienceForm(request.POST)
        if form.is_valid():
            work_experience = form.save(commit=False)
            work_experience.user = request.user  
            work_experience.save()
            return redirect('work_experience_list')
    else:
        form = WorkExperienceForm()
    return render(request, 'portfolio/create_work_experience.html', {'form': form})

def edit_work_experience(request, pk):
    work_experience = get_object_or_404(WorkExperience, pk=pk, user=request.user)
    if request.method == 'POST':
        form = WorkExperienceForm(request.POST, instance=work_experience)
        if form.is_valid():
            form.save()
            return redirect('work_experience_list')
    else:
        form = WorkExperienceForm(instance=work_experience)
    return render(request, 'portfolio/edit_work_experience.html', {'form': form, 'work_experience': work_experience})

def delete_work_experience(request, pk):
    work_experience = get_object_or_404(WorkExperience, pk=pk, user=request.user)
    if request.method == 'POST':
        work_experience.delete()
        return redirect('work_experience_list')
    return render(request, 'portfolio/delete_work_experience.html', {'work_experience': work_experience})



def certification_list(request):
    certifications = Certification.objects.filter(user=request.user)
    return render(request, 'portfolio/certification_list.html', {'certifications': certifications})

def add_certification(request):
    if request.method == 'POST':
        form = CertificationForm(request.POST)
        if form.is_valid():
            certification = form.save(commit=False)
            certification.user = request.user  # Set the current user
            certification.save()
            return redirect('certification_list')  # Redirect to the certification list
    else:
        form = CertificationForm()
    return render(request, 'portfolio/add_certification.html', {'form': form})

def delete_certification(request, pk):
    certification = get_object_or_404(Certification, pk=pk, user=request.user)
    if request.method == 'POST':
        certification.delete()
        return redirect('certification_list')
    return render(request, 'portfolio/confirm_delete.html', {'certification': certification})



def education_list(request):
    education_entries = Education.objects.filter(user=request.user)
    return render(request, 'portfolio/education_list.html', {'education_entries': education_entries})

def add_education(request):
    if request.method == 'POST':
        form = EducationForm(request.POST)
        if form.is_valid():
            education = form.save(commit=False)
            education.user = request.user  # Set the current user
            education.save()
            return redirect('education_list')  # Redirect to the education list
    else:
        form = EducationForm()
    return render(request, 'portfolio/add_education.html', {'form': form})

def edit_education(request, pk):
    education = get_object_or_404(Education, pk=pk, user=request.user)
    if request.method == 'POST':
        form = EducationForm(request.POST, instance=education)
        if form.is_valid():
            form.save()
            return redirect('education_list')
    else:
        form = EducationForm(instance=education)
    return render(request, 'portfolio/edit_education.html', {'form': form})

def delete_education(request, pk):
    education = get_object_or_404(Education, pk=pk, user=request.user)
    if request.method == 'POST':
        education.delete()
        return redirect('education_list')
    return render(request, 'portfolio/confirm_deleteeducation.html', {'education': education})