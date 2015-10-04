from splinter.browser import Browser

import re
import time
import sys
import os
import pafy 


SongName=raw_input("enter song ")
br=Browser('chrome')

br.driver.set_window_size(10,10)

br.visit("http://www.youtube.com")

time.sleep(5)

searchbar=br.find_by_id("masthead-search-terms").first.find_by_tag("input")[0]

searchbar.fill(SongName)

br.execute_script("document.getElementById('masthead-search').submit();")

URLfirst=br.find_by_id("results").first.find_by_tag("a")

for i in range(1,50):
	print i

	if (URLfirst[i]['href'].find("watch")!=-1 and len(URLfirst[i]['href'])< 50):
		YoutubeURL=URLfirst[i]['href']
		break


br.quit()

mp3 = pafy.new(YoutubeURL)
bestaudio = mp3.getbestaudio()

bestaudio.download()

