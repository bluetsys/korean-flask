import platform
import sys

from django.http import HttpResponse

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