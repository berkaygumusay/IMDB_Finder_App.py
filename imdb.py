
import requests
import time
import sys

from bs4 import BeautifulSoup
while True:
    print("""
*** SOMETHING TO WATCH ***
1.  Find Me Movies
2.  Find Me Tv Series
3.  What Is Something To Watch
4.  Exit
    """)
    menuLoop1 = int(input("    Make Your Choice :"))
    if(menuLoop1 == 1):
        favMovies = []
        movieUrlPart1 = "https://www.imdb.com/search/title/?genres="
        movieUrlPart2 = "&sort=user_rating,desc&title_type=feature&num_votes=25000,&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=5aab685f-35eb-40f3-95f7-c53f09d542c3&pf_rd_r=1C3JJQN07WFQ6JQD2YR0&pf_rd_s=right-6&pf_rd_t=15506&pf_rd_i=top&ref_=chttp_gnr_1"
        print("""    Hi!
    What Are Your Top 3 Movie Genres??
        """)
        for i in range(0,3):
            favMovie = input("   {} : ".format((i+1)))
            favMovie = favMovie.lower()
            favMovies.append(favMovie)
        for i in range(0,3):
            movieUrl = movieUrlPart1 + favMovies[i] + movieUrlPart2
            responseMovie = requests.get(movieUrl)
            contentMovie = responseMovie.content
            soupMovie = BeautifulSoup(contentMovie,"html.parser")
            loopCounter = 0
            print("-----------------------------------------------------------------------")
            print("**** {} Movie Recommendations ****\n".format(favMovies[i].capitalize()))
            for i in soupMovie.find_all("h3",{"class":"lister-item-header"}):
                if(loopCounter == 5):
                    break
                else:
                    i=i.text
                    i = i.strip()
                    i = i.replace("\n","")
                    print(i)
                    loopCounter+=1
    elif(menuLoop1 == 2):
        tvserieUrlPart1 = "https://www.imdb.com/search/title/?genres="
        tvserieUrlPart2 = "&sort=user_rating,desc&title_type=tv_series,mini_series&num_votes=5000,&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=f85d9bf4-1542-48d1-a7f9-48ac82dd85e7&pf_rd_r=1XT5450GV8PWGRP2NBKN&pf_rd_s=right-6&pf_rd_t=15506&pf_rd_i=toptv&ref_=chttvtp_gnr_1"
        print("""    Hi!
    What Are Your Top 3 Tv Series Genres??
                """)
        favTvseries = []
        for i in range(0,3):
            favTvserie = input("   {} : ".format((i+1)))
            favTvserie = favTvserie.lower()
            favTvseries.append(favTvserie)
        for i in range(0,3):
            tvserieUrl = tvserieUrlPart1 + favTvseries[i] + tvserieUrlPart2
            responseSerie = requests.get(tvserieUrl)
            contentSerie = responseSerie.content
            soupSerie = BeautifulSoup(contentSerie,"html.parser")
            loopCounter = 0
            print("-----------------------------------------------------------------------")
            print("**** {} Series Recommendations ****\n".format(favTvseries[i].capitalize()))
            for i in soupSerie.find_all("h3", {"class": "lister-item-header"}):
                if (loopCounter == 5):
                    break
                else:
                    i = i.text
                    i = i.strip()
                    i = i.replace("\n", "")
                    print(i)
                    loopCounter += 1
    elif(menuLoop1 == 3):
        print("""
    'Something To Watch' Is Basically A Movie Or Series Finder
    Firstly You Enter Your Top 3 Movie or Series Genres
    Than This App Finds Top 5 Movies or Series In This Genres
    And All You Have To Do Is Sit Back And Enjoy The Movie Or Series :)""")
    elif(menuLoop1 == 4):
        print("*** Exited Succesfully ***")
        time.sleep(1)
        sys.exit()
    else:
        print("!!! Please Enter Valid Value !!!")
        time.sleep(3)
        pass
