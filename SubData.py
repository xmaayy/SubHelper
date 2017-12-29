import praw
import math
import TimePeriods
import os
import csv

#ARK, ENG, XLM, XRB, ICX
IGNORE = 'If this submission has been flaired inaccurately'

class DataFetcher:
    targetSub = ''
    reddit = praw.Reddit

    def __init__(self, subreddit):
        self.targetSub = subreddit;
        filename = 'config.file'
        fin = open(filename, 'r');
        CLIENT_ID = fin.readline().strip()
        CLIENT_SECRET = fin.readline().strip()
        USER_AGENT = fin.readline().strip()
        self.reddit = praw.Reddit(client_id = CLIENT_ID,
                             client_secret = CLIENT_SECRET,
                             user_agent = USER_AGENT)

    #Get the avgerage number of comments on all posts for a given time period
    #TimeTuple: A tuple or start and end times in that order
    #ignoreZero: Wether or not to ignore posts with zero Comments
    def avgComments(self, TimeTuple, ignoreZero):
        total_comments = 0;
        num_posts = 0;
        relevant_submissions = self.reddit.subreddit(self.targetSub).submissions(TimeTuple[1],TimeTuple[0])
        for submission in relevant_submissions:
            if submission.num_comments!=0 and ignoreZero or not ignoreZero:
                num_posts+=1;
                total_comments+=submission.num_comments;

        print('There were ' + str(num_posts) + ' posts and ' + str(total_comments) + ' comments.')
        return(total_comments/num_posts)

    #This function saves the previous week worth of comments to a csv file
    #This has a set subdirectory and IDC enough to make it customizeable for you
    def saveLastWeekC(self):
        print("Opening dir...")
        try:
            f = csv.writer(open('DATA/' + self.targetSub + '/lastWeek.csv', 'w'))
        except FileNotFoundError:
            print("Dir not there \n Making dir...")
            os.makedirs('DATA/' + self.targetSub + '/');
            f = csv.writer(open('DATA/' + self.targetSub + '/lastWeek.csv', 'w'))
        print("Fetching submissions...")
        f.writerow(['comment'])
        time = TimePeriods.lastWeek();
        relevant_submissions = self.reddit.subreddit(self.targetSub).submissions(time[1],time[0])
        for submission in relevant_submissions:
            print("\033c")
            print("Currently saving:\n "+submission.title + "\n it has " + str(submission.num_comments()))
            for comment in submission.comments:
                try:
                    if IGNORE not in comment.body:
                        f.writerow([comment.body])
                except AttributeError:
                    print("Submission Had No Comments...")
        print("\033c")
        print("Done, last week of comments saved as \'lastWeek.csv\'")

    #This function saves the previous 24h worth of comments to a csv file
    #Again, this has a set subdirectory and IDC enough to make it customizeable for you
    def saveLast24C(self):
        print("Opening dir...")
        try:
            f = csv.writer(open('DATA/' + self.targetSub + '/last24.csv', 'w'))
        except FileNotFoundError:
            print("Dir not there \n Making dir...")
            os.makedirs('DATA/' + self.targetSub + '/');
            f = csv.writer(open('DATA/' + self.targetSub + '/last24.csv', 'w'))
        print("Fetching submissions...")
        f.writerow(['comment'])
        time = TimePeriods.last24();
        relevant_submissions = self.reddit.subreddit(self.targetSub).submissions(time[1],time[0])
        for submission in relevant_submissions:
            print("\033c")
            print("Currently saving:\n "+submission.title + "\n it has " + str(submission.num_comments))
            for comment in submission.comments:
                try:
                    if IGNORE not in comment.body:
                        f.writerow([comment.body])
                except AttributeError:
                    print("Submission Had No Comments...")
        print("\033c")
        print("Done, last 24 hrs of comments saved as \'last24.csv\'")
