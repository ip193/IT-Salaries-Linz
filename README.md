# IT-Salaries-Linz


## Instructions:

Make sure you have the numpy, matplotlib and csv modules, then simply run polyreg.py from the console to render the plots. 






----------

Regression analysis of self-reported IT salaries in Linz, Austria. (n = 300)

I recently stumbled upon a [link](https://old.reddit.com/r/Austria/comments/975j7i/itgeh%C3%A4lter_in_%C3%B6sterreich/e47znfy/) to a survey of IT professionals in Linz that recorded salary, years of experience, and gender. In total, 307 people replied. 



In the end, there were 280 valid responses, of which 242 reported male gender, 32 reported female gender, and 4 did not indicate gender. 

Salaries ranged from €23,100 to 150,000. The median reported salary and years of experience were €47,600 and 6 years, respectively. 

Here are some plots of the data featuring regression from python's numpy library. *All plots show years of experience vs. yearly salary. Men are colored in red, women in blue.*

[All respondents (top 3 outliers removed)](https://i.imgur.com/kTKqYpJ.png)

[Male salaries vs. Female salaries (top 3 outliers removed)](https://i.imgur.com/SsK1CYJ.png)


It's interesting to note that female salaries trended noticably lower than male salaries. Also, women reported less experience on average than their male counterparts. To see what would happen, I disregarded all males who reported higher experience than every female respondent (read: I restricted the analysis to respondents who reported <=12 years of experience). From this restricted sample, I then also removed the 3 respondents who reported the highest salaries. 

Here is the result: [Male salaries vs. Female salaries, with experience <= 12 years, top 3 outliers removed](https://i.imgur.com/4hyl1Bz.png) 


*Some notes on the methodology: * 


From all the respondents, I only considered those who worked full-time and gave information for y.o.e and salary. 7 participants indicated they are working part-time, so they have been excluded from the analysis. Similarly, 20 respondents did not indicate their years of experience, so they too were removed. 


Take the results of this survey with a grain of salt. Self-reported data has a host of weaknesses, starting with accuracy. Not everyone knows their exact salary, and respondents might have been estimating the value of their total compensation. Some might have been answering in bad faith. 

Selection bias is a problem, since this is informal data from respondents active on reddit. 

Sample size was also rather small, particularly for female respondents. 

Note also that respondents could indicate how many hours of overtime are in their contract, but I did not factor that into the analysis, meaning I plotted 35000 for 40 hours a week the same as 35000 with 40 hours + 15 hours overtime. 


[Here is the source code and the survey data](https://github.com/ip193/IT-Salaries-Linz/), if anyone is interested. Thanks for reading!

 
