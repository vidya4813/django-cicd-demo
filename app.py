from django.http import HttpResponse
from django.urls import path
from django.core.management import execute_from_command_line
import sys
from django.conf import settings

settings.configure(
    DEBUG=True,
    ROOT_URLCONF=__name__,
    SECRET_KEY='demo-secret',
    ALLOWED_HOSTS=['*'],
)

def home(request):
    html = """
    <html>
        <head>
            <title>CI/CD Demo</title>
        </head>
        <body style="background-color:#f0f8ff; text-align:center; font-family:Arial;">
            <h1 style="color:green;">🚀 Hello CI/CD</h1>
            <p style="color:blue; font-size:20px;">
                This is a simple Django web page for GitHub Actions demo
            </p>
            <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcReFonU1eFqPkrPY7fVFGJg_BFVNFg05sHiRg&s"
                 alt="Demo Image"
                 style="margin-top:20px; border-radius:10px;">
            <p style="color:gray; margin-top:30px;">
                Pipeline Ready ✔
            </p>
        </body>
    </html>
    """
    return HttpResponse(html)

urlpatterns = [
    path('', home),
]

if __name__ == '__main__':
    execute_from_command_line([sys.argv[0], 'runserver', '0.0.0.0:8000'])