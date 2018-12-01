# IT-Salaries-Linz

## Regression analysis of self-reported IT salaries in Linz, Austria. (n = 280)

#### Data: [Online survey](https://old.reddit.com/r/Austria/comments/975j7i/itgeh%C3%A4lter_in_%C3%B6sterreich/e47znfy/) of IT professionals in Linz that recorded salary, years of experience, and gender. In total, 307 people replied. 

There were 280 valid responses, of which 242 reported male gender, 32 reported female gender, and 4 did not indicate gender. 

Salaries ranged from €23,100 to 150,000. The median reported salary and years of experience were €47,600 and 6 years, respectively. 

Here are some plots of the data featuring regression from python's numpy library. *All plots show years of experience vs. yearly salary. Men are colored in red, women in blue.*

[All respondents (top 3 outliers removed)](https://i.imgur.com/kTKqYpJ.png)

[Male salaries vs. Female salaries (top 3 outliers removed)](https://i.imgur.com/SsK1CYJ.png)


It is interesting to note that female salaries trended noticably lower than male salaries. Also, women reported less experience on average than their male counterparts. To see what would happen, I disregarded all males who reported higher experience than every female respondent (read: I restricted the analysis to respondents who reported <=12 years of experience). From this restricted sample, I then also removed the 3 respondents who reported the highest salaries. 

Here is the result: [Male salaries vs. Female salaries, with experience <= 12 years, top 3 outliers removed](https://i.imgur.com/4hyl1Bz.png) 


### Notes on the methodology: 


From all the respondents, I only considered those who worked full-time and gave information for y.o.e and salary. (Excluded 27 respondents from the analysis).

Self-reported data has a host of weaknesses, starting with accuracy. Not everyone knows their exact salary, and respondents might have been estimating the value of their total compensation or adding/excluding benefits. 

Selection bias is a problem, since this is informal data from respondents active on reddit. 

Sample size was also rather small, particularly for female respondents. 

Salary data for full-time work ignores exact hours worked per week; i.e. 35000 for 40 hours a week was plotted the same as 35000 with 40 hours + 15 hours overtime. 

[reddit discussion](https://old.reddit.com/r/cscareerquestionsEU/comments/9854bi/analysis_of_it_salaries_in_linz_austria/)


## Instructions:

Make sure you have the numpy, matplotlib and csv modules, then run polyreg.py from the console to render the plots. 


-------- 

This project is licensed under the terms of the MIT license.


 
