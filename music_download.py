from __future__ import unicode_literals
import bs4,requests
import youtube_dl


def get_link(query):
	UrL = "https://www.youtube.com/results?search_query="+query
	#UrL = "https://www.youtube.com/results?search_query=Joe+Sent+Me+Vanessa+Daou+Joe+Sent+Me"

	handle = requests.get(UrL).content

	#print handle
	soup = bs4.BeautifulSoup(handle,"lxml")
	selector = "div.yt-lockup-dismissable.yt-uix-tile > div.yt-lockup-thumbnail.contains-addto > a"
	elems = soup.select(selector)
	helper = "https://www.youtube.com" + elems[0].get('href')
	print(helper)
	return helper


def return_list_of_songs(filename):
	with open(filename) as f:
		list_of_songs = f.readlines()
	list_of_songs = [x.strip() for x in list_of_songs]
	return list_of_songs


"""ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '320',
    }],
}
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download(['http://www.youtube.com/watch?v=BaW_jenozKc'])
"""


def get_list_of_links(list_of_songs):
	list_of_youtube_urls = []
	for song in list_of_songs:
		link_of_song = get_link(song)
		list_of_youtube_urls.append(link_of_song)

	return list_of_youtube_urls

def download_songs_all(all_links):
	ydl_opts = {
	    'format': 'bestaudio/best',
	    'outtmpl':'%(title)s.%(ext)s',
	    'postprocessors': [{
	        'key': 'FFmpegExtractAudio',
	        'preferredcodec': 'mp3',
	        'preferredquality': '320',
	    }],
	}
	for link_of_the_song in all_links:
		with youtube_dl.YoutubeDL(ydl_opts) as ydl:
			ydl.download([link_of_the_song])


def main():
	filename = "playlist.txt"
	list_of_songs = return_list_of_songs(filename)
	list_of_youtube_urls = get_list_of_links(list_of_songs)
	download_songs_all(list_of_youtube_urls)

main()