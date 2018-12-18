
import random

def main():

    epTitles1 = {"1" : "The Gang Gets Racist",
                 "2" : "Charlie Wants an Abortion",
                 "3" : "Underage Drinking: A National Concern",
                 "4" : "Charlie Has Cancer",
                 "5" : "Gun Fever",
                 "6" : "The Gang Finds a Dead Guy",
                 "7" : "Charlie Got Molested"}

    epTitles2 = {"1" : 	"Charlie Gets Crippled",
                 "2" : "The Gang Goes Jihad",
                 "3" : 	"Dennis and Dee Go on Welfare",
                 "4" : "Mac Bangs Dennis' Mom"	,
                 "5" : "Hundred Dollar Baby"	,
                 "6" : "The Gang Gives Back",
                 "7" : "The Gang Exploits a Miracle",
                 "8" : "The Gang Runs for Office",
                 "9" : "Charlie Goes America All Over Everybody's Ass",
                 "10" : "Dennis and Dee Get a New Dad"}

    epTitles3 = {"1" : "The Gang Finds a Dumpster Baby",
                 "2" : "The Gang Gets Invincible",
                 "3" : "Dennis and Dee's Mom is Dead",
                 "4" : "The Gang Gets Held Hostage"	,
                 "5" : "The Aluminum Monster vs. Fatty Magoo",
                 "6" : "The Gang Solves the North Korea Situation",
                 "7" : "The Gang Sells Out",
                 "8" : "Frank Sets Sweet Dee on Fire",
                 "9" : "Sweet Dee's Dating a Retarded Person",
                 "10" : "Mac is a Serial Killer",
                 "11" : "Dennis Looks Like a Registered Sex Offender",
                 "12" : "The Gang Gets Whacked (Part 1)",
                 "13" : "The Gang Gets Whacked (Part 2)",
                 "14" : "Bums: Making a Mess All Over the City",
                 "15" : "The Gang Dances Their Asses Off"}

    epTitles4 = {"1" : "Mac and Dennis: Manhunters",
                 "2" : "The Gang Solves the Gas Crisis",
                 "3" : "America's Next Top Paddy's Billboard Model Contest",
                 "4" : "Mac's Banging the Waitress",
                 "5" : "Mac and Charlie Die (Part 1)",
                 "6" : "Mac and Charlie Die (Part 2)",
                 "7" : "Who Pooped the Bed?",
                 "8" : "Paddy's Pub: The Worst Bar in Philadelphia",
                 "9" : "Dennis Reynolds: An Erotic Life",
                 "10" : "Sweet Dee Has a Heart Attack",
                 "11" : "The Gang Cracks the Liberty Bell",
                 "12" : "The Gang Gets Extreme: Home Makeover Edition",
                 "13" : "The Knightman Cometh"}

    epTitles5 = {"1" : "The Gang Exploits the Mortgage Crisis",
                 "2" : "The Gang Hits the Road",
                 "3" : "The Great Recession",
                 "4" : "The Gang Gives Frank an Intervention",
                 "5" : "The Waitress Is Getting Married",
                 "6" : "The World Series Defense",
                 "7" : "The Gang Wrestles for the Troops",
                 "8" : "Paddy's Pub: Home of the Original Kitten Mittens",
                 "9" : "Mac and Dennis Break Up",
                 "10" : "The D.E.N.N.I.S. System",
                 "11" : "Mac and Charlie Write a Movie",
                 "12" : "The Gang Reignites the Rivalry"}

    epTitles6 = {"1" : "Mac Dights Gay Marriage",
                 "2" : "Dennis Gets Divorced",
                 "3" : "The Gang Buys a Boat",
                 "4" : "Mac's Big Break",
                 "5" : "Mac and Charlie: White Trash",
                 "6" : "Mac's Mom Burns Her House Down",
                 "7" : "Who Got Dee Pregnant?",
                 "8" : "The Gang Gets a New Member",
                 "9" : "Dee Reynolds: Shaping America's Youth",
                 "10" : "Charlie Kelly: King of the Rats",
                 "11" : "The Gang Gets Stranded in the Woods",
                 "12" : "Dee Gives Birth",
                 "13" : "A Very Sunny Christmas (Part 1)",
                 "14" : "A Verry Sunny Christmas (Part 2)"}

    epTitles7 = {"1" : "Frank's Pretty Woman",
                 "2" : "The Gang Goes to the Jersey Shore",
                 "3" : "Frank Reynolds' Little Beauties",
                 "4" : "Sweet Dee Gets Audited",
                 "5" : "Frank's Brother",
                 "6" : "The Storm Century",
                 "7" : "Chardee MacDennis: The Game of Games",
                 "8" : "The ANTI-Social Network",
                 "9" : "The Gang Gets Trapped",
                 "10" : "How Mac Got Fat",
                 "11" : "Thunder Gun Express",
                 "12" : "The High School Reunion",
                 "13" : "The High School Reunion Part 2: The Gang's Revenge"}

    epTitles8 = {"1" : "Pop-Pop: The Final Solution",
                 "2" : "The Gang Recycles Their Trash",
                 "3" : "The Maureen Ponderosa Wedding Massacre",
                 "4" : "Charlie and Dee Find Love",
                 "5" : "The Gang Gets Analyzed",
                 "6" : "Charlie's Mom Has Cancer",
                 "7" : "Frank's Back in Business",
                 "8" : "Charlie Rules the World",
                 "9" : "The Gang Dines Out",
                 "10" : "Reynolds vs. Reynolds: The Cereal Defense"}

    epTitles9 = {"1" : "The Gang Broke Dee",
                 "2" : "Gun Fever Too: Still Hot",
                 "3" : "The Gang tries Desperately to Win an Award",
                 "4" : "Mac and Dennis Buy a Timeshare",
                 "5" : "Mac Day",
                 "6" : "The Gang Saves the Day",
                 "7" : "The Gang Gets Quarantined",
                 "8" : "Flowers for Charlie",
                 "9" : "The Gang Makes Lethal Weapon 6",
                 "10" : "The Gang Squashes Their Beefs"}

    epTitles10 = {"1" : "The Gang Beats Boggs",
                 "2" : "The Gang Group Dates",
                 "3" : "Pyscho Pete Returns",
                 "4" : "Charlie Work",
                 "5" : "The Spies Like U.S.",
                 "6" : "The Gang Misses the Boat",
                 "7" : "Mac Kills His Dad",
                 "8" : "The Gang Goes on Family Fight",
                 "9" : "Frank Retires",
                 "10" : "Ass Kickers United: Mac and Charlie Join a Cult"}

    epTitles11 = {"1" : "Chardie MacDennis 2: Electric Boogaloo",
                 "2" : "Frank Falls Out the Window",
                 "3" : "The Gang Hits the Slops",
                 "4" : "Dee Made a Smut Film",
                 "5" : "Mac and Dennis Move to the Suburbs",
                 "6" : "Being Frank",
                 "7" : "McPoyle vs. Ponderosa: The Trial of the Century",
                 "8" : "Charlie Catches a Leprechaun",
                 "9" : "The Gang Goes to Hell",
                 "10" : "The Gang Goes to Hell: Part Two"}
    
    epTitles12 = {"1" : "The Gang Turns Black",
                 "2" : "The Gang Goes to a Water Park",
                 "3" : "Old Lady House: A Situational Comedy",
                 "4" : "Wolf Cola: A Public Relations Nightmare",
                 "5" : "Making Dennis Reynolds a Murderer",
                 "6" : "Hero or Hate Crime?",
                 "7" : "PTSDee",
                 "8" : "The Gang Tends Bar",
                 "9" : "A Cricket's Tale",
                 "10" : "Dennis' Double Life"}

    epTitles13 = {"1" : "The Gang Makes Paddy's Great Again",
                 "2" : "The Gang Escapes",
                 "3" : "The Gang Beats Boggs: Ladies Reboot",
                 "4" : "Time's Up for the Gang",
                 "5" : "The Gang Gets New Wheels",
                 "6" : "The Gang Solves the Bathroom Problem",
                 "7" : "The Gang Does a Clip Show",
                 "8" : "Charlie's Home Alone",
                 "9" : "The Gang Wins the Big Game",
                 "10" : "Mac Finds His Pride"}
    
    x = int(input("Enter a season between 1 and 13 or 0 for random season: "))

    print("You selected season:", x)
    
    if x == 0:
        randomSeason = random.randint(1,13)
        print("Random season:", randomSeason)

        if randomSeason == 1:
            episode = random.randint(1,7)           
            print("Episode:", episode)

            if episode == 1:
                print(epTitles1["1"])
            elif episode == 2:
                print(epTitles1["2"])
            elif episode == 3:
                print(epTitles1["3"])
            elif episode == 4:
                print(epTitles1["4"])
            elif episode == 5:
                print(epTitles1["5"])
            elif episode == 6:
                print(epTitles1["6"])
            elif episode == 7:
                print(epTitles1["7"])

        if randomSeason == 2:
            episode = random.randint(1,10)           
            print("Episode:", episode)

            if episode == 1:
                print(epTitles2["1"])
            elif episode == 2:
                print(epTitles2["2"])
            elif episode == 3:
                print(epTitles2["3"])
            elif episode == 4:
                print(epTitles2["4"])
            elif episode == 5:
                print(epTitles2["5"])
            elif episode == 6:
                print(epTitles2["6"])
            elif episode == 7:
                print(epTitles2["7"])
            elif episode == 8:
                print(epTitles2["8"])
            elif episode == 9:
                print(epTitles2["9"])
            elif episode == 10:
                print(epTitles2["10"])

        if randomSeason == 3:
            episode = random.randint(1,15)
            print("Episode:", episode)

            if episode == 1:
                print(epTitles3["1"])
            elif episode == 2:
                print(epTitles3["2"])
            elif episode == 3:
                print(epTitles3["3"])
            elif episode == 4:
                print(epTitles3["4"])
            elif episode == 5:
                print(epTitles3["5"])
            elif episode == 6:
                print(epTitles3["6"])
            elif episode == 7:
                print(epTitles3["7"])
            elif episode == 8:
                print(epTitles3["8"])
            elif episode == 9:
                print(epTitles3["9"])
            elif episode == 10:
                print(epTitles3["10"])
            elif episode == 11:
                print(epTitles3["11"])
            elif episode == 12:
                print(epTitles3["12"])
            elif episode == 13:
                print(epTitles3["13"])
            elif episode == 14:
                print(epTitles3["14"])
            elif episode == 15:
                print(epTitles3["15"])

        if randomSeason == 4:
            episode = random.randint(1,13)
            print("Episode:", episode)

            if episode == 1:
                print(epTitles4["1"])
            elif episode == 2:
                print(epTitles4["2"])
            elif episode == 3:
                print(epTitles4["3"])
            elif episode == 4:
                print(epTitles4["4"])
            elif episode == 5:
                print(epTitles4["5"])
            elif episode == 6:
                print(epTitles4["6"])
            elif episode == 7:
                print(epTitles4["7"])
            elif episode == 8:
                print(epTitles4["8"])
            elif episode == 9:
                print(epTitles4["9"])
            elif episode == 10:
                print(epTitles4["10"])
            elif episode == 11:
                print(epTitles4["11"])
            elif episode == 12:
                print(epTitles4["12"])
            elif episode == 13:
                print(epTitles4["13"])

        if randomSeason == 5:
            episode = random.randint(1,12)
            print("Episode:", episode)

            if episode == 1:
                print(epTitles5["1"])
            elif episode == 2:
                print(epTitles5["2"])
            elif episode == 3:
                print(epTitles5["3"])
            elif episode == 4:
                print(epTitles5["4"])
            elif episode == 5:
                print(epTitles5["5"])
            elif episode == 6:
                print(epTitles5["6"])
            elif episode == 7:
                print(epTitles5["7"])
            elif episode == 8:
                print(epTitles5["8"])
            elif episode == 9:
                print(epTitles5["9"])
            elif episode == 10:
                print(epTitles5["10"])
            elif episode == 11:
                print(epTitles5["11"])
            elif episode == 12:
                print(epTitles5["12"])

        if randomSeason == 6:
            episode = random.randint(1,14)
            print("Episode:", episode)

            if episode == 1:
                print(epTitles6["1"])
            elif episode == 2:
                print(epTitles6["2"])
            elif episode == 3:
                print(epTitles6["3"])
            elif episode == 4:
                print(epTitles6["4"])
            elif episode == 5:
                print(epTitles6["5"])
            elif episode == 6:
                print(epTitles6["6"])
            elif episode == 7:
                print(epTitles6["7"])
            elif episode == 8:
                print(epTitles6["8"])
            elif episode == 9:
                print(epTitles6["9"])
            elif episode == 10:
                print(epTitles6["10"])
            elif episode == 11:
                print(epTitles6["11"])
            elif episode == 12:
                print(epTitles6["12"])
            elif episode == 13:
                print(epTitles6["13"])
            elif episode == 14:
                print(epTitles6["14"])

        if randomSeason == 7:
            episode = random.randint(1,13)
            print("Episode:", episode)

            if episode == 7:
                print(epTitles4["1"])
            elif episode == 2:
                print(epTitles7["2"])
            elif episode == 3:
                print(epTitles7["3"])
            elif episode == 4:
                print(epTitles7["4"])
            elif episode == 5:
                print(epTitles7["5"])
            elif episode == 6:
                print(epTitles7["6"])
            elif episode == 7:
                print(epTitles7["7"])
            elif episode == 8:
                print(epTitles7["8"])
            elif episode == 9:
                print(epTitles7["9"])
            elif episode == 10:
                print(epTitles7["10"])
            elif episode == 11:
                print(epTitles7["11"])
            elif episode == 12:
                print(epTitles7["12"])
            elif episode == 13:
                print(epTitles7["13"])

        if randomSeason == 8:
            episode = random.randint(1,10)
            print("Episode:", episode)

            if episode == 1:
                print(epTitles8["1"])
            elif episode == 2:
                print(epTitles8["2"])
            elif episode == 3:
                print(epTitles8["3"])
            elif episode == 4:
                print(epTitles8["4"])
            elif episode == 5:
                print(epTitles8["5"])
            elif episode == 6:
                print(epTitles8["6"])
            elif episode == 7:
                print(epTitles8["7"])
            elif episode == 8:
                print(epTitles8["8"])
            elif episode == 9:
                print(epTitles8["9"])
            elif episode == 10:
                print(epTitles8["10"])

        if randomSeason == 9:
            episode = random.randint(1,10)
            print("Episode:", episode)

            if episode == 1:
                print(epTitles9["1"])
            elif episode == 2:
                print(epTitles9["2"])
            elif episode == 3:
                print(epTitles9["3"])
            elif episode == 4:
                print(epTitles9["4"])
            elif episode == 5:
                print(epTitles9["5"])
            elif episode == 6:
                print(epTitles9["6"])
            elif episode == 7:
                print(epTitles9["7"])
            elif episode == 8:
                print(epTitles9["8"])
            elif episode == 9:
                print(epTitles9["9"])
            elif episode == 10:
                print(epTitles9["10"])

        if randomSeason == 10:
            episode = random.randint(1,10)
            print("Episode: ", episode)

            if episode == 1:
                print(epTitles10["1"])
            elif episode == 2:
                print(epTitles10["2"])
            elif episode == 3:
                print(epTitles10["3"])
            elif episode == 4:
                print(epTitles10["4"])
            elif episode == 5:
                print(epTitles10["5"])
            elif episode == 6:
                print(epTitles10["6"])
            elif episode == 7:
                print(epTitles10["7"])
            elif episode == 8:
                print(epTitles10["8"])
            elif episode == 9:
                print(epTitles10["9"])
            elif episode == 10:
                print(epTitles10["10"])

        if randomSeason == 11:
            episode = random.randint(1,10)
            print("Episode:", episode)

            if episode == 1:
                print(epTitles11["1"])
            elif episode == 2:
                print(epTitles11["2"])
            elif episode == 3:
                print(epTitles11["3"])
            elif episode == 4:
                print(epTitles11["4"])
            elif episode == 5:
                print(epTitles11["5"])
            elif episode == 6:
                print(epTitles11["6"])
            elif episode == 7:
                print(epTitles11["7"])
            elif episode == 8:
                print(epTitles11["8"])
            elif episode == 9:
                print(epTitles11["9"])
            elif episode == 10:
                print(epTitles11["10"])

        if randomSeason == 12:
            episode = random.randint(1,10)
            print("Episode:", episode)

            if episode == 1:
                print(epTitles12["1"])
            elif episode == 2:
                print(epTitles12["2"])
            elif episode == 3:
                print(epTitles12["3"])
            elif episode == 4:
                print(epTitles12["4"])
            elif episode == 5:
                print(epTitles12["5"])
            elif episode == 6:
                print(epTitles12["6"])
            elif episode == 7:
                print(epTitles12["7"])
            elif episode == 8:
                print(epTitles12["8"])
            elif episode == 9:
                print(epTitles12["9"])
            elif episode == 10:
                print(epTitles12["10"])

        if randomSeason == 13:
            episode = random.randint(1,10)
            print("Episode:", episode)

            if episode == 1:
                print(epTitles13["1"])
            elif episode == 2:
                print(epTitles13["2"])
            elif episode == 3:
                print(epTitles13["3"])
            elif episode == 4:
                print(epTitles13["4"])
            elif episode == 5:
                print(epTitles13["5"])
            elif episode == 6:
                print(epTitles13["6"])
            elif episode == 7:
                print(epTitles13["7"])
            elif episode == 8:
                print(epTitles13["8"])
            elif episode == 9:
                print(epTitles13["9"])
            elif episode == 10:
                print(epTitles13["10"])
    
    if x == 1:
        episode = random.randint(1,7)           
        print("Episode:", episode)

        if episode == 1:
            print(epTitles1["1"])
        elif episode == 2:
            print(epTitles1["2"])
        elif episode == 3:
            print(epTitles1["3"])
        elif episode == 4:
            print(epTitles1["4"])
        elif episode == 5:
            print(epTitles1["5"])
        elif episode == 6:
            print(epTitles1["6"])
        elif episode == 7:
            print(epTitles1["7"])

    elif x == 2:
        episode = random.randint(1,10)
        print("Episode:", episode)

        if episode == 1:
            print(epTitles2["1"])
        elif episode == 2:
            print(epTitles2["2"])
        elif episode == 3:
            print(epTitles2["3"])
        elif episode == 4:
            print(epTitles2["4"])
        elif episode == 5:
            print(epTitles2["5"])
        elif episode == 6:
            print(epTitles2["6"])
        elif episode == 7:
            print(epTitles2["7"])
        elif episode == 8:
            print(epTitles2["8"])
        elif episode == 9:
            print(epTitles2["9"])
        elif episode == 10:
            print(epTitles2["10"])
        
    elif x == 3:
        episode = random.randint(1,15)
        print("Episode:", episode)        

        if episode == 1:
            print(epTitles3["1"])
        elif episode == 2:
            print(epTitles3["2"])
        elif episode == 3:
            print(epTitles3["3"])
        elif episode == 4:
            print(epTitles3["4"])
        elif episode == 5:
            print(epTitles3["5"])
        elif episode == 6:
            print(epTitles3["6"])
        elif episode == 7:
            print(epTitles3["7"])
        elif episode == 8:
            print(epTitles3["8"])
        elif episode == 9:
            print(epTitles3["9"])
        elif episode == 10:
            print(epTitles3["10"])
        elif episode == 11:
            print(epTitles3["11"])
        elif episode == 12:
            print(epTitles3["12"])
        elif episode == 13:
            print(epTitles3["13"])
        elif episode == 14:
            print(epTitles3["14"])
        elif episode == 15:
            print(epTitles3["15"])

    elif x == 4:
        episode = random.randint(1,13)
        print("Episode:", episode)

        if episode == 1:
            print(epTitles4["1"])
        elif episode == 2:
            print(epTitles4["2"])
        elif episode == 3:
            print(epTitles4["3"])
        elif episode == 4:
            print(epTitles4["4"])
        elif episode == 5:
            print(epTitles4["5"])
        elif episode == 6:
            print(epTitles4["6"])
        elif episode == 7:
            print(epTitles4["7"])
        elif episode == 8:
            print(epTitles4["8"])
        elif episode == 9:
            print(epTitles4["9"])
        elif episode == 10:
            print(epTitles4["10"])
        elif episode == 11:
            print(epTitles4["11"])
        elif episode == 12:
            print(epTitles4["12"])
        elif episode == 13:
            print(epTitles4["13"])

    elif x == 5:
        episode = random.randint(1,12)
        print("Episode:", episode)

        if episode == 1:
            print(epTitles5["1"])
        elif episode == 2:
            print(epTitles5["2"])
        elif episode == 3:
            print(epTitles5["3"])
        elif episode == 4:
            print(epTitles5["4"])
        elif episode == 5:
            print(epTitles5["5"])
        elif episode == 6:
            print(epTitles5["6"])
        elif episode == 7:
            print(epTitles5["7"])
        elif episode == 8:
            print(epTitles5["8"])
        elif episode == 9:
            print(epTitles5["9"])
        elif episode == 10:
            print(epTitles5["10"])
        elif episode == 11:
            print(epTitles5["11"])
        elif episode == 12:
            print(epTitles5["12"])
        
    elif x == 6:
        episode = random.randint(1,14)
        print("Episode:", episode)

        if episode == 1:
            print(epTitles6["1"])
        elif episode == 2:
            print(epTitles6["2"])
        elif episode == 3:
            print(epTitles6["3"])
        elif episode == 4:
            print(epTitles6["4"])
        elif episode == 5:
            print(epTitles6["5"])
        elif episode == 6:
            print(epTitles6["6"])
        elif episode == 7:
            print(epTitles6["7"])
        elif episode == 8:
            print(epTitles6["8"])
        elif episode == 9:
            print(epTitles6["9"])
        elif episode == 10:
            print(epTitles6["10"])
        elif episode == 11:
            print(epTitles6["11"])
        elif episode == 12:
            print(epTitles6["12"])
        elif episode == 13:
            print(epTitles6["13"])
        elif episode == 14:
            print(epTitles6["14"])

    elif x == 7:
        episode = random.randint(1,13)
        print("Episode:", episode)

        if episode == 7:
            print(epTitles4["1"])
        elif episode == 2:
            print(epTitles7["2"])
        elif episode == 3:
            print(epTitles7["3"])
        elif episode == 4:
            print(epTitles7["4"])
        elif episode == 5:
            print(epTitles7["5"])
        elif episode == 6:
            print(epTitles7["6"])
        elif episode == 7:
            print(epTitles7["7"])
        elif episode == 8:
            print(epTitles7["8"])
        elif episode == 9:
            print(epTitles7["9"])
        elif episode == 10:
            print(epTitles7["10"])
        elif episode == 11:
            print(epTitles7["11"])
        elif episode == 12:
            print(epTitles7["12"])
        elif episode == 13:
            print(epTitles7["13"])


    elif x == 8:
        episode = random.randint(1,10)
        print("Episode:", episode)

        if episode == 1:
            print(epTitles8["1"])
        elif episode == 2:
            print(epTitles8["2"])
        elif episode == 3:
            print(epTitles8["3"])
        elif episode == 4:
            print(epTitles8["4"])
        elif episode == 5:
            print(epTitles8["5"])
        elif episode == 6:
            print(epTitles8["6"])
        elif episode == 7:
            print(epTitles8["7"])
        elif episode == 8:
            print(epTitles8["8"])
        elif episode == 9:
            print(epTitles8["9"])
        elif episode == 10:
            print(epTitles8["10"])

    elif x == 9:
        episode = random.randint(1,10)
        print("Episode:", episode)

        if episode == 1:
            print(epTitles9["1"])
        elif episode == 2:
            print(epTitles9["2"])
        elif episode == 3:
            print(epTitles9["3"])
        elif episode == 4:
            print(epTitles9["4"])
        elif episode == 5:
            print(epTitles9["5"])
        elif episode == 6:
            print(epTitles9["6"])
        elif episode == 7:
            print(epTitles9["7"])
        elif episode == 8:
            print(epTitles9["8"])
        elif episode == 9:
            print(epTitles9["9"])
        elif episode == 10:
            print(epTitles9["10"])

    elif x == 10:
        episode = random.randint(1,10)
        print("Episode:", episode)

        if episode == 1:
            print(epTitles10["1"])
        elif episode == 2:
            print(epTitles10["2"])
        elif episode == 3:
            print(epTitles10["3"])
        elif episode == 4:
            print(epTitles10["4"])
        elif episode == 5:
            print(epTitles10["5"])
        elif episode == 6:
            print(epTitles10["6"])
        elif episode == 7:
            print(epTitles10["7"])
        elif episode == 8:
            print(epTitles10["8"])
        elif episode == 9:
            print(epTitles10["9"])
        elif episode == 10:
            print(epTitles10["10"])

    elif x == 11:
        episode = random.randint(1,10)
        print("Episode:", episode)

        if episode == 1:
            print(epTitles11["1"])
        elif episode == 2:
            print(epTitles11["2"])
        elif episode == 3:
            print(epTitles11["3"])
        elif episode == 4:
            print(epTitles11["4"])
        elif episode == 5:
            print(epTitles11["5"])
        elif episode == 6:
            print(epTitles11["6"])
        elif episode == 7:
            print(epTitles11["7"])
        elif episode == 8:
            print(epTitles11["8"])
        elif episode == 9:
            print(epTitles11["9"])
        elif episode == 10:
            print(epTitles11["10"])

    elif x == 12:
        episode = random.randint(1,10)
        print("Episode:", episode)

        if episode == 1:
            print(epTitles12["1"])
        elif episode == 2:
            print(epTitles12["2"])
        elif episode == 3:
            print(epTitles12["3"])
        elif episode == 4:
            print(epTitles12["4"])
        elif episode == 5:
            print(epTitles12["5"])
        elif episode == 6:
            print(epTitles12["6"])
        elif episode == 7:
            print(epTitles12["7"])
        elif episode == 8:
            print(epTitles12["8"])
        elif episode == 9:
            print(epTitles12["9"])
        elif episode == 10:
            print(epTitles12["10"])

    elif x == 13:
        episode = random.randint(1,10)
        print("Episode:", episode)

        if episode == 1:
            print(epTitles13["1"])
        elif episode == 2:
            print(epTitles13["2"])
        elif episode == 3:
            print(epTitles13["3"])
        elif episode == 4:
            print(epTitles13["4"])
        elif episode == 5:
            print(epTitles13["5"])
        elif episode == 6:
            print(epTitles13["6"])
        elif episode == 7:
            print(epTitles13["7"])
        elif episode == 8:
            print(epTitles13["8"])
        elif episode == 9:
            print(epTitles13["9"])
        elif episode == 10:
            print(epTitles13["10"])

    print("")
    print("Enjoy, boners")

main()
