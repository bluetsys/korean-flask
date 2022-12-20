import platform
import sys
import zlib

import mecab

from django.conf import settings
from django.urls import path
from django.http import HttpResponse

settings.configure(
	DEBUG=False,  # For debugging
	ALLOWED_HOSTS=["*"],  # For debugging
	#SECRET_KEY="a-bad-secret",  # Insecure! change this
	ROOT_URLCONF=__name__,
)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'root': {
        'handlers': [],
        'level': 'CRITICAL',
    },
}

def home(request):
	return HttpResponse("Hello World")

def health(request):
	return HttpResponse(platform.node())

urlpatterns = [
	path("", home),
	path("health", health),
]

if __name__ == "__main__":
	from django.core.management import execute_from_command_line

	execute_from_command_line(sys.argv)