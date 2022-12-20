import platform
import sys
import zlib

import mecab

from django.conf import settings
from django.urls import path
from django.http import HttpResponse

settings.configure(
	DEBUG=True,  # For debugging
	#SECRET_KEY="a-bad-secret",  # Insecure! change this
	ROOT_URLCONF=__name__,
)


def home(request):
	return HttpResponse(platform.node())

urlpatterns = [
	path("", home),
	path("health", home),
]

if __name__ == "__main__":
	from django.core.management import execute_from_command_line

	execute_from_command_line(sys.argv)