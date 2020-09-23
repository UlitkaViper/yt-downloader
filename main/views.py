from django.shortcuts import render, redirect
from django.views import View
from .models import URL
from .encodeURL import encode
from .forms import UrlField
import re
import requests
from bs4 import BeautifulSoup as bs
import datetime
from .yt_downloader import get_preview, download_video
from django.http import HttpResponse
# Create your views here.


class MainPageView(View):
    def get(self, request):
        template_name = 'main/home.html'
        form = UrlField()
        context = {'form': form}
        return render(request, template_name, context)


class Download(View):
    def post(self, request):
        yt_link = request.POST.get('YT_link')
        # if 'Download_button' in request.POST:

        # yt_link_id = re.findall(
        #     'https://www\.youtube\.com/watch\?v=(\w+)&', yt_link)

        # thumbnail_link = f'http://img.youtube.com/vi/{yt_link_id[0]}/maxresdefault.jpg'
        # print(yt_lhtml_dataid, thumbnail_link)
        # html = requests.get(yt_link, stream=True).text
        # seconds_length = int(re.findall(
        #     '\\"lengthSeconds\\"html_data(\d+)\\"', html)[0])
        # video_duration = str(datetime.timedelta(seconds=seconds_length))
        preview_data = get_preview(yt_link)
        template_name = 'main/download_page.html'
        form = UrlField()
        context = preview_data
        context['video_url'] = yt_link
        return render(request, template_name, context)


class SendFile(View):
    def post(self, request):
        # file_name = download_video(request.POST.get(
        #     'YT_link'), request.POST.get('yt_itag'))
        # yt_file = open(file_name, 'rb')
        yt_file = open('video.mp4', 'rb')
        response = HttpResponse(
            yt_file.read(), content_type='application/force-download')
        response['Content-Disposition'] = 'attachment; filename="video.mp4"'
        return render(None, 'main/home.html', response)
        # return response
