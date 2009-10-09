from imdb import IMDb


s = """
Whiteout (2009)
Glitter (2001)
Cheaper By the Dozen 2 (2005)
Boat Trip (2003)
All About Steve (2009)
Lost Souls (2000)
The New Guy (2002)
A Sound of Thunder (2005)
Babylon A.D. (2008)
Surviving Christmas (2004)
Dragonfly (2002)
Basic Instinct 2 (2006)
Kaena: The Prophecy (2004)
Testosterone (2003)
Pavilion of Women (2001)
Larry the Cable Guy: Health Inspector (2006)
Thr3e (2007)
Doogal (2006)
Supercross: The Movie (2005)
Extreme Ops (2002)
Big Momma's House 2 (2006)
The Adventures of Pluto Nash (2002)
Deck the Halls (2006)
Date Movie (2006)
Johnson Family Vacation (2004)
Son of the Mask (2005)
Envy (2004)
Gigli (2003)
Broken Bridges (2006)
College (2008)
New Best Friend (2002)
The Cookout (2004)
Yu-Gi-Oh: The Movie (2004)
The Hottie & the Nottie (2008)
The Fog (2005)
Swept Away (2002)
Corky Romano (2001)
Yours, Mine, & Ours (2005)
Serving Sara (2002)
Good Luck Chuck (2007)
The Perfect Man (2005)
88 Minutes (2008)
Christmas with the Kranks (2004)
Godsend (2004)
Because I Said So (2007)
The Celestine Prophecy (2006)
Harry And Max (2005)
Modigliani (2005)
The Bridge of San Luis Rey (2005)
Fascination (2005)
Dirty Love (2005)
In the Name of the King: A Dungeon Siege Tale (2008)
BloodRayne (2006)
Soul Survivors (2001)
Material Girls (2006)
My Baby's Daddy (2004)
Street Fighter: The Legend of Chun-Li (2009)
Darkness (2003)
House of the Dead (2003)
Zoom (2006)
Down to You (2000)
Miss March (2009)
Happily N'Ever After (2007)
Code Name: The Cleaner (2007)
The Whole Ten Yards (2004)
Deal (2008)
The Haunting of Molly Hartley (2008)
Delta Farce (2007)
Deuces Wild (2002)
The Covenant (2006)
Fear Dot Com (2002)
Bless the Child (2000)
Rollerball (2002)
Battlefield Earth (2000)
Kickin' It Old Skool (2007)
Meet the Spartans (2008)
Texas Rangers (2001)
The In Crowd (2000)
Disaster Movie (2008)
Epic Movie (2007)
Crossover (2006)
Half Past Dead (2002)
The Master of Disguise (2002)
Twisted (2004)
Daddy Day Camp (2007)
Alone in the Dark (2005)
Beyond a Reasonable Doubt (2009)
Constellation (2007)
Killing Me Softly (2002)
Merci Docteur Rey! (2002)
Witless Protection (2008)
Redline (2007)
3 Strikes (2000)
Strange Wilderness (2008)
Superbabies: Baby Geniuses 2 (2004)
National Lampoon's Gold Diggers (2004)
King's Ransom (2005)
Pinocchio (2002)
One Missed Call (2008)
Ballistic: Ecks vs. Sever (2002)
"""
movies = [ss.strip() for ss in s.split("\n") if len(ss.strip())]


ia = IMDb()
import collections
d = collections.defaultdict(set)
people = {}
for movie in movies:
	movie_list = ia.search_movie(movie)
	mid = movie_list[0]
	print movie, ":", mid
	m = ia.get_movie(mid.movieID)
 	try:
		for p in m['cast']:
			d[p.personID].add(m)
			people[p.personID] = p
	except Exception, exc:
		print exc

from operator import itemgetter
def bad_movie_sorter(d):
	s = d[1]
	return len(s)

bad_actor_list = sorted(d.items(), key=bad_movie_sorter, reverse=True)
for actor_info in bad_actor_list[:10]:
	actor_id = actor_info[0]
	print people[actor_id]['name']
	films = sorted(actor_info[1])
	for film in films:
		print "\t%s" % film


