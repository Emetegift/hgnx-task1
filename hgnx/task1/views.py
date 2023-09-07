from django.shortcuts import render
from rest_framework.response import Response
# from django.forms.models import model_to_dict
# from post.models import Post
from rest_framework.decorators import api_view
from django.http import JsonResponse
from django.views.decorators.http import require_GET
import datetime

@require_GET
def endpoint_view(request):
    slack_name = request.GET.get('slack_name', 'Gift Emete')
    track = request.GET.get('track', 'backend')

    # Get current day of the week
    current_day = datetime.datetime.now().strftime("%A")

    # Get current UTC time
    current_utc_time = datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")

    # Replace 'username', 'repo', and 'file_name.ext' with your actual GitHub details
    github_file_url = "https://github.com/Emetegift/repo/blob/main/hgnx-task1.ext"
    github_repo_url = "git remote add origin https://github.com/Emetegift/hgnx-task1.git"

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
