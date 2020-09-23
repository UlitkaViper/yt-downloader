from pytube import YouTube
import moviepy.editor as mp
import datetime
import io
import eyed3
import re
import requests


def get_preview(url):
    # streams = YouTube(url).streams.all()
    # for stream in streams:
    #     print(stream)
    # print(len(streams)
    # vI64_JtEPFQ&ab_channel=cpol
    html_data = requests.get(url).text
    video_id = re.findall('v=(.+)&', url)[0]
    thumbnail_link = f'https://img.youtube.com/vi/{video_id}/maxresdefault.jpg'
    video_title, video_duration = re.findall(
        'title\\":\\"(.+?)\\"\S+lengthSeconds\S+"(\d+)\\"', html_data)[0]
    video_duration = datetime.timedelta(seconds=int(video_duration))
    preview_data = {'title': video_title,
                    'duration': video_duration,
                    'thumbnail': thumbnail_link}
    # video = YouTube(url)
    # preview_data = {'thumbnail': video.thumbnail_url,
    #                 'title': video.title,
    #                 'duration': str(datetime.timedelta(seconds=video.length))
    #                 }
    all_itags_and_res = re.findall(
        '"itag.*?:(\d+),\\\\"url\S+"video\\\\\/(?!webm).*?qualityLabel.*?"(\w+)', html_data)
    res = []
    uniq_itags_res = []
    for el in all_itags_and_res:
        if el[1] not in res:
            res.append(el[1])
            uniq_itags_res.append(el)
    del res, all_itags_and_res
    uniq_itags_res = sorted(
        uniq_itags_res, key=lambda x: -int(x[1].split('p')[0]))
    preview_data['streams'] = uniq_itags_res
    print(uniq_itags_res)
    return preview_data


def download_video(url, itag):
    # Download video
    # video = YouTube(url).streams.filter(only_audio=True).first().download()
    # streams = YouTube(url).streams.all()
    print(itag)
    video = YouTube(url).streams.get_by_itag(itag).first().download()
    print(video)
    # s = ','.join([str(el) for el in streams])
    # f = re.findall('res="(\w+)"', s)
    # # resolutions = [str(stream)[47:51] for stream in streams]
    # # print(resolutions)
    # print(f)
    # Convert to mp3
    # clip = mp.AudioFileClip(video)
    # clip.write_audiofile('audio.mp3')

    # Without download
    # chunk = io.BytesIO()
    # YouTube(url).streams.filter(
    #     only_audio=True).first().stream_to_buffer(chunk)
    # with open('main/tmp/audio.mp3', 'wb') as f:
    #     f.write(chunk.getbuffer())

    # Add Title to mp3
    # song = eyed3.load('audio.mp3')
    # song.tag.title = 'Hazuki - Legend of Millenium'
    # song.tag.save()
    return video


# get_preview(
#     'https://www.youtube.com/watch?v=vI64_JtEPFQ&ab_channel=cpol')

# download_video(
#     'https://www.youtube.com/watch?v=vI64_JtEPFQ&ab_channel=cpol', '10')
