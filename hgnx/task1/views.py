from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from django.views.decorators.http import require_GET
import datetime

@require_GET
def endpoint_view(request):
    slack_name = request.GET.get('slack_name', 'example_name')
    track = request.GET.get('track', 'backend')

    # Get current day of the week
    current_day = datetime.datetime.now().strftime("%A")

    # Get current UTC time
    current_utc_time = datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")

    # Replace 'username', 'repo', and 'file_name.ext' with your actual GitHub details
    github_file_url = "https://github.com/username/repo/blob/main/file_name.ext"
    github_repo_url = "https://github.com/username/repo"

    response_data = {
        "slack_name": slack_name,
        "current_day": current_day,
        "utc_time": current_utc_time,
        "track": track,
        "github_file_url": github_file_url,
        "github_repo_url": github_repo_url,
        "status_code": 200
    }

    return JsonResponse(response_data)
