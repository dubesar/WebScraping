soup.title
(gives the title tag of the page)

soup.title.string
(gives the string in the title tag)

soup.a
(gives the output - <a id="top"></a>)
So to get all the links on the page we have:

soup.find_all("a")
(This gives all the links on the page)

soup.find_all('table')
(This gives all the tables on the page)

Inorder to find the table you want we can use:
soup.find_all('table',class_='wikitable sortable plainrowheaders') - This is for example we have to type the class of table we want

#Generate lists
A=[]
B=[]
C=[]
D=[]
E=[]
F=[]
G=[]
for row in right_table.findAll("tr"):
    cells = row.findAll('td')
    states=row.findAll('th') #To store second column data
    if len(cells)==6: #Only extract table body not heading
        A.append(cells[0].find(text=True))
        B.append(states[0].find(text=True))
        C.append(cells[1].find(text=True))
        D.append(cells[2].find(text=True))
        E.append(cells[3].find(text=True))
        F.append(cells[4].find(text=True))
        G.append(cells[5].find(text=True))
        
#import pandas to convert list to data frame
import pandas as pd
df=pd.DataFrame(A,columns=['Number'])
df['State/UT']=B
df['Admin_Capital']=C
df['Legislative_Capital']=D
df['Judiciary_Capital']=E
df['Year_Capital']=F
df['Former_Capital']=G
df
