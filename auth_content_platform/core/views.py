from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages  # Uso de messages
from django.contrib.sessions.models import Session  # Uso de sessions
from django.contrib.contenttypes.models import ContentType
from .models import ContentItem

# Login usando django.contrib.auth
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            messages.success(request, "Login exitoso")
            return redirect('dashboard')
        else:
            messages.error(request, "Credenciales inválidas")

    return render(request, 'core/login.html')


@login_required
def logout_view(request):
    logout(request)
    messages.info(request, "Sesión cerrada")
    return redirect('login')


# Dashboard con inspección de apps preinstaladas
@login_required
def dashboard(request):
    total_users = User.objects.count()  # auth
    total_sessions = Session.objects.count()  # sessions
    total_content_types = ContentType.objects.count()  # contenttypes

    context = {
        'total_users': total_users,
        'total_sessions': total_sessions,
        'total_content_types': total_content_types,
    }

    return render(request, 'core/dashboard.html', context)


# CRUD simple apoyado en auth
@login_required
def content_list(request):
    contents = ContentItem.objects.all()
    return render(request, 'core/content_list.html', {'contents': contents})


@login_required
def content_create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        body = request.POST.get('body')

        ContentItem.objects.create(
            title=title,
            body=body,
            created_by=request.user
        )

        messages.success(request, "Contenido creado")
        return redirect('content_list')

    return render(request, 'core/content_list.html')


# Vista para inspeccionar modelos internos
@login_required
def model_inspection(request):
    user_fields = [field.name for field in User._meta.get_fields()]
    session_fields = [field.name for field in Session._meta.get_fields()]
    contenttype_fields = [field.name for field in ContentType._meta.get_fields()]

    context = {
        'user_fields': user_fields,
        'session_fields': session_fields,
        'contenttype_fields': contenttype_fields,
    }

    return render(request, 'core/model_inspection.html', context)