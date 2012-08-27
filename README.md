The attached code and description were created for the [Harvard Business Review 'Vision Statement' Prospect on Kaggle](https://www.kaggle.com/c/harvard-business-review-vision-statement-prospect/prospector)

sentimentToFile.py is the main file, in which a topic can be set and the program will output a file containing the sentiment values of articles whos subject is the chosen topic, a corresponding dates array for the articles, and the titles of the articles with max and min sentiment values. Files used to process, analyze and graph the data can be found in src. 










Sentiment Analysis By Topic over Time

The following project provides visualization of a few common terms found in HBR over the last 90 years and attempts to analyze the net sentiment of the terms over time.

Methods

To begin, the most frequent terms to appear in HBR were consolidated using the the Python Natural Language Toolkit. After observing the most frequent terms and removing the unusable ones,a few notable terms were chosen. Using the senti_classifier package, articles with the subject or title containing these terms were analyzed for there overall sentiment and graphed.

Note : Additional topics can easily be added. Please comment with any suggestions.

Visualization

The graph below displays sentiment by topic over time. Topics include 'American', 'China', 'Innovation', 'Manufacturing','War' and 'Technology'. For each topic the title and date are displayed for the most positive article.

link to Graph 

Observations

For each topic here are a few observations:

China: The maximum positive sentiment was in an article titled "Entering China: An Unconventional Approach" appearing on March 1st, 1997, just as China was appearing as a global superpower. Articles regarding China rarely appeared before 1987. Since 2000, articles about China have been overall extremely positive.

American: The maximum positive sentiment was in an article titled "Tocqueville Revisited: The Meaning of American Prosperity" appearing on January 1st, 2001, one of the most prosperous times for the U.S.. Articles with the keyword American appear spread out over time and are generally highly positive.

Innovation: The maximum positive sentiment was in an article titled "Finding and Grooming Breakthrough Inno[an example](http://example.com/ "Title")vators" appearing on December 1st, 2008, interestingly as the current financial crisis was begining. Overall the term Innovation displayed the highest overall average positive sentiment and has only been popular for the last 30 years.

Manufacturing: The maximum positive sentiment was in an article titled "Breakthrough Manufacturing" appearing on March 1st, 1987. This term appeared frequently in the '70s '80s and '90 but has since ceased to appear as frequently.

Technology: The maximum positive sentiment was in an article titled "Research That Reinvents the Corporation." appearing on January 1st, 1991, just as large tech companies were picking up in the U.S.. This term appeared frequently since the '60s and has a high overall positive sentiment.

War: The maximum positive sentiment was in an article titled "The Peace Must be Won at Home" appearing on January 1st, 1943, during World War II. This term appeared frequently in the '20s '30s and '40s during the World Wars and has a lower average positive sentiment than the rest of the terms.