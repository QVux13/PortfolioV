
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages
from django.conf import settings as django_settings
from django.http import FileResponse, Http404
import os

# Hardcode profile data
PROFILE = {
    'name': 'Nguyen Quang Vu',
    'title': 'Backend Developer',
    'bio': 'I am a backend developer with a passion for creating efficient and scalable web applications. I enjoy learning new technologies and continuously improving my skills to deliver quality solutions.',
    'location': 'Ha Tinh, Viet Nam',
    'email': 'quangvunguyen1605@gmail.com',
    'github': 'https://github.com/QVux13',
    'linkedin': 'https://www.linkedin.com/in/quangvu13/',
    'facebook': 'https://www.facebook.com/quang.vu.232368/',
    'instagram': 'https://www.instagram.com/qvux03/',
    'stackoverflow': 'https://stackoverflow.com/',
    'avatar': '/media/profile/avatar.jpg',
    'phone': '+84 349641705',
}


CODING_SKILLS = [
    {'name': 'Python', 'percentage': 90},
    {'name': 'Django', 'percentage': 85},
    {'name': 'FastAPI', 'percentage': 90},
    {'name': 'JavaScript', 'percentage': 70},
    {'name': 'Node.js (Express)', 'percentage': 80},
    {'name': 'HTML / CSS', 'percentage': 80},
    {'name': 'ReactJS', 'percentage': 65},
]

EDUCATION = [
    {
        'degree': 'Computer Science',
        'school': 'Hanoi University of Industry',
        'year': '2021 - 2025',
        'description': 'Studying computer science with a solid foundation in algorithms, data structures, computer networks, and software development'
    },
]

EXPERIENCE = [
    {
        'position': 'Python Developer',
        'company': 'Newwave Solutions Joint Stock Company',
        'year': 'Dec 2024 - Jul 2025',
        'description': '• Analysis of requirements\n• Japanese web application development\n• Write code using Python with Django, Flask, FastAPI frameworks'
    },
    {
        'position': 'Junior Backend Developer',
        'company': 'Tumiki',
        'year': 'Jul 2025 - Jan 2026',
        'description': '• Analysis of requirements\n• Geospatial web application development\n• Build HRM system using FastAPI and Dart\n• Develop Inuka Education Service backend using FastAPI and PostgreSQL'
    },
]

PROJECTS = [
    {
        'title': 'E-commerce Platform',
        'description': 'Full-stack e-commerce platform built with Django and PostgreSQL. Features include product management, shopping cart, and payment integration.',
        'category': 'Web App',
        'tech_stack': 'Django, PostgreSQL, Redis',
        'image': None,
        'github_link': 'https://github.com/yourusername/ecommerce',
        'live_demo': '',
    },
    {
        'title': 'Task Management API',
        'description': 'RESTful API for task management built with FastAPI. Includes user authentication, real-time notifications, and advanced filtering.',
        'category': 'API',
        'tech_stack': 'FastAPI, MongoDB, JWT',
        'image': None,
        'github_link': 'https://github.com/yourusername/task-api',
        'live_demo': 'https://task-api.example.com',
    },
    {
        'title': 'Portfolio Website',
        'description': 'Personal portfolio website showcasing projects and skills. Built with Django and deployed on Vercel.',
        'category': 'Website',
        'tech_stack': 'Django, Tailwind CSS',
        'image': None,
        'github_link': 'https://github.com/yourusername/portfolio',
        'live_demo': '',
    },
]

def home(request):
    return render(request, 'core/home.html', {'profile': PROFILE})

def about(request):
    return render(request, 'core/about.html', {'profile': PROFILE})

def resume(request):
    return render(request, 'core/resume.html', {
        'profile': PROFILE,
        'coding_skills': CODING_SKILLS,
        'education': EDUCATION,
        'experience': EXPERIENCE
    })

def portfolio(request):
    return render(request, 'core/portfolio.html', {'profile': PROFILE, 'projects': PROJECTS})

def contact(request):
    success = False
    error = False

    if request.method == 'POST':
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        subject = request.POST.get('subject', 'No Subject')
        message = request.POST.get('message', '')

        if name and email and message:
            try:
                full_message = f"From: {name} <{email}>\n\n{message}"
                send_mail(
                    subject=f'[Portfolio] {subject}',
                    message=full_message,
                    from_email=django_settings.DEFAULT_FROM_EMAIL,
                    recipient_list=[PROFILE['email']],
                    fail_silently=False,
                )
                success = True
            except Exception:
                error = True
        else:
            error = True

    return render(request, 'core/contact.html', {
        'profile': PROFILE,
        'success': success,
        'error': error,
    })

def download_cv(request):
    file_path = os.path.join(django_settings.MEDIA_ROOT, 'resume', 'NguyenQuangVu_CV_Backend.pdf')
    if not os.path.exists(file_path):
        raise Http404('CV not found')
    return FileResponse(
        open(file_path, 'rb'),
        content_type='application/pdf',
        as_attachment=True,
        filename='NguyenQuangVu_CV_Backend.pdf',
    )