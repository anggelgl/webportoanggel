from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from .models import Profile, Experience


def home(request):
    profile     = Profile.objects.first()
    experiences = Experience.objects.all()

    if request.method == 'POST':
        name    = request.POST.get('name', '').strip()
        email   = request.POST.get('email', '').strip()
        message = request.POST.get('message', '').strip()

        if name and email and message:
            send_mail(
                subject=f'[Portfolio] Pesan dari {name}',
                message=f'Dari  : {name}\nEmail : {email}\n\nPesan:\n{message}',
                from_email=email,
                recipient_list=[profile.email if profile else 'anggel@example.com'],
                fail_silently=True,
            )
            messages.success(request, 'Pesan berhasil dikirim! Terima kasih.')
        else:
            messages.error(request, 'Semua field harus diisi.')

        return redirect('home')

    return render(request, 'portofolio/home.html', {
        'profile'    : profile,
        'experiences': experiences,
    })