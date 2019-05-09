import random

epTitles = {
            (1,1) : "The Gang Gets Racist",(1,2) : "Charlie Wants an Abortion",(1,3) : "Underage Drinking: A National Concern",(1,4) : "Charlie Has Cancer",
            (1,5) : "Gun Fever",(1,6) : "The Gang Finds a Dead Guy",(1,7) : "Charlie Got Molested",
            (2,1) : "Charlie Gets Crippled",(2,2) : "The Gang Goes Jihad",(2,3) :"Dennis and Dee Go on Welfare",(2,4) : "Mac Bangs Dennis' Mom"	,(2,5):"Hundred Dollar Baby",
            (2,6) : "The Gang Gives Back",(2,7) : "The Gang Exploits a Miracle",(2,8) : "The Gang Runs for Office",(2,9) : "Charlie Goes America All Over Everybody's Ass",(2,10) : "Dennis and Dee Get a New Dad",
            (3,1) : "The Gang Finds a Dumpster Baby",(3,2) : "The Gang Gets Invincible",(3,3) : "Dennis and Dee's Mom is Dead",(3,4) : "The Gang Gets Held Hostage" ,
            (3,5) : "The Aluminum Monster vs. Fatty Magoo",(3,6) : "The Gang Solves the North Korea Situation",(3,7) : "The Gang Sells Out",(3,8) : "Frank Sets Sweet Dee on Fire",
            (3,9) : "Sweet Dee's Dating a Retarded Person", (3,10) : "Mac is a Serial Killer",(3,11) : "Dennis Looks Like a Registered Sex Offender",(3,12) : "The Gang Gets Whacked (Part 1)",
            (3,13) : "The Gang Gets Whacked (Part 2)",(3,14) : "Bums: Making a Mess All Over the City",(3,15) : "The Gang Dances Their Asses Off",
            (4,1) : "Mac and Dennis: Manhunters", (4,2) : "The Gang Solves the Gas Crisis",(4,3) : "America's Next Top Paddy's Billboard Model Contest",(4,4) : "Mac's Banging the Waitress",
            (4,5) : "Mac and Charlie Die (Part 1)",(4,6) : "Mac and Charlie Die (Part 2)",(4,7) : "Who Pooped the Bed?",(4,8) : "Paddy's Pub: The Worst Bar in Philadelphia",(4,9): "Dennis Reynolds: An Erotic Life",
            (4,10) : "Sweet Dee Has a Heart Attack",(4,11): "The Gang Cracks the Liberty Bell",(4,12): "The Gang Gets Extreme: Home Makeover Edition",(4,13) : "The Knightman Cometh",
            (5,1) : "The Gang Exploits the Mortgage Crisis",(5,2) : "The Gang Hits the Road",(5,3) : "The Great Recession",(5,4): "The Gang Gives Frank an Intervention",(5,5): "The Waitress Is Getting Married",
            (5,6): "The World Series Defense",(5,7): "The Gang Wrestles for the Troops",(5,8): "Paddy's Pub: Home of the Original Kitten Mittens",(5,9) : "Mac and Dennis Break Up",(5,10): "The D.E.N.N.I.S. System",
            (5,11) : "Mac and Charlie Write a Movie",(5,12): "The Gang Reignites the Rivalry",
            (6,1) : "Mac Dights Gay Marriage",(6,2) : "Dennis Gets Divorced",(6,3) : "The Gang Buys a Boat",(6,4): "Mac's Big Break",(6,5) : "Mac and Charlie: White Trash",(6,6) : "Mac's Mom Burns Her House Down",(6,7) : "Who Got Dee Pregnant?",
            (6,8) : "The Gang Gets a New Member",(6,9) : "Dee Reynolds: Shaping America's Youth",(6,10) : "Charlie Kelly: King of the Rats",(6,11): "The Gang Gets Stranded in the Woods",
            (6,12) : "Dee Gives Birth",(6,13): "A Very Sunny Christmas (Part 1)",(6,14): "A Very Sunny Christmas (Part 2)",
            (7,1): "Frank's Pretty Woman",(7,2): "The Gang Goes to the Jersey Shore",(7,3): "Frank Reynolds' Little Beauties",(7,4) : "Sweet Dee Gets Audited",(7,5): "Frank's Brother",(7,6): "The Storm Century",
            (7,7) : "Chardee MacDennis: The Game of Games",(7,8) : "The ANTI-Social Network",(7,9) : "The Gang Gets Trapped",(7,10) : "How Mac Got Fat",(7,11): "Thunder Gun Express",(7,12): "The High School Reunion",(7,13) : "The High School Reunion Part 2: The Gang's Revenge",
            (8,1): "Pop-Pop: The Final Solution",(8,2) : "The Gang Recycles Their Trash",(8,3): "The Maureen Ponderosa Wedding Massacre",(8,4): "Charlie and Dee Find Love",(8,5): "The Gang Gets Analyzed",(8,6): "Charlie's Mom Has Cancer",
            (8,7) : "Frank's Back in Business",(8,8): "Charlie Rules the World",(8,9): "The Gang Dines Out",(8,10) : "Reynolds vs. Reynolds: The Cereal Defense",
            (9,1) : "The Gang Broke Dee",(9,2) : "Gun Fever Too: Still Hot",(9,3) : "The Gang tries Desperately to Win an Award",(9,4): "Mac and Dennis Buy a Timeshare",(9,5) : "Mac Day",(9,6) : "The Gang Saves the Day",
            (9,7) : "The Gang Gets Quarantined",(9,8): "Flowers for Charlie",(9,9): "The Gang Makes Lethal Weapon 6",(9,10) : "The Gang Squashes Their Beefs",
            (10,1): "The Gang Beats Boggs",(10,2) : "The Gang Group Dates",(10,3) : "Pyscho Pete Returns",(10,4): "Charlie Work",(10,5): "The Spies Like U.S.",(10,6): "The Gang Misses the Boat",
            (10,7): "Mac Kills His Dad",(10,8) : "The Gang Goes on Family Fight",(10,9) : "Frank Retires",(10,10): "Ass Kickers United: Mac and Charlie Join a Cult",
            (11,1) : "Chardie MacDennis 2: Electric Boogaloo",(11,2): "Frank Falls Out the Window",(11,3): "The Gang Hits the Slops",(11,4): "Dee Made a Smut Film",(11,5) : "Mac and Dennis Move to the Suburbs",
            (11,6) : "Being Frank",(11,7) : "McPoyle vs. Ponderosa: The Trial of the Century",(11,8): "Charlie Catches a Leprechaun",(11,9) : "The Gang Goes to Hell",(11,10): "The Gang Goes to Hell: Part Two",
            (12,1) : "The Gang Turns Black",(12,2) : "The Gang Goes to a Water Park",(12,3): "Old Lady House: A Situational Comedy",(12,4): "Wolf Cola: A Public Relations Nightmare",(12,5): "Making Dennis Reynolds a Murderer",
            (12,6): "Hero or Hate Crime?",(12,7): "PTSDee",(12,8): "The Gang Tends Bar",(12,9): "A Cricket's Tale",(12,10): "Dennis' Double Life",
            (13,1) : "The Gang Makes Paddy's Great Again",(13,2): "The Gang Escapes",(13,3) : "The Gang Beats Boggs: Ladies Reboot",(13,4): "Time's Up for the Gang",(13,5): "The Gang Gets New Wheels",
            (13,6): "The Gang Solves the Bathroom Problem",(13,7) : "The Gang Does a Clip Show",(13,8): "Charlie's Home Alone",(13,9) : "The Gang Wins the Big Game",(13,10): "Mac Finds His Pride"
                }
season = int(input("Enter a season between 1 and 13 or 0 for random season: "))
keys = list(filter(lambda x: season==0 or x[0]==season, epTitles.keys()))
print('Season', season)
print('Random episode: {}'.format(epTitles[random.choice(keys)]))
