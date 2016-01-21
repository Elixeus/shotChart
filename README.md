# shotChart
I've created this script to visualize the players' shot charts for Houston Rockets as a demo.

The program contains 5 files. They should kept in the same directory. Run make_roster_shelve.py first. It creates a python shelve file in the local directory containing the link between player name and player id. Then run the retrieve.py file to finish the program.The other files are objects that support the script.

The idea is inspired by [Greg Reda](http://www.gregreda.com/2015/02/15/web-scraping-finding-the-api/)'s intro on how to use client-side API to search for NBA player stats. The court.py is taken from Sawas Tjortjoglou's [draw_court function](http://savvastjortjoglou.com/nba-shot-sharts.html). Thanks to these two guys!
