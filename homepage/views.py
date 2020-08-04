from django.shortcuts import render
from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse, HttpResponseRedirect


# Define method to handle request to index
def index(request):
    return render(request, 'homepage/index.html', {})


def about(request):
    return render(request, 'homepage/about.html', {})


def services(request):
    return render(request, 'homepage/services.html', {})


def pricing(request):
    return render(request, 'homepage/pricing.html', {})


def contact(request):
    # Check whether the form is get or posted
    if request.method != 'POST':
        return render(request, 'homepage/contact.html', {})

    else:
        # Get post data
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        context = {
            'name': name
        }

        # Send email with posted data
        if subject and message and email:
            try:
                send_mail(subject, message, email, ['franklinokech@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return render(request, 'homepage/contact_thank_you.html', context)
        else:
            # In reality we'd use a form class
            # to get proper validation errors.
            return HttpResponse('Make sure all fields are entered and valid.')


def newsletter(request):
    my_email = request.POST['email']
    subject = 'new subscriber'
    message = 'We have a new subscriber'

    context = {
        'email': my_email
    }

    # Send email with posted data
    if my_email:
        try:
            send_mail(subject, message, my_email, ['franklinokech@gmail.com'])
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
        return render(request, 'homepage/thank_subscriber.html', context)
    else:
        # In reality we'd use a form class
        # to get proper validation errors.
        return HttpResponse('Make sure all fields are entered and valid.')
    return render(request, 'homepage/newsletter.html', {})
