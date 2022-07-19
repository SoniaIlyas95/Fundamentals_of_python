# step 1 import libraries
#import seaborn as sns
#import matplotlib.pyplot as plt

# step 2 set a theme
#sns.set_theme(style="ticks", color_codes=True)

# step 3 load data set/or import your own data
#ship=sns.load_dataset("titanic")
#print(ship)
# step 4 plot basic graph for 1 variable/count plot
#p=sns.countplot(x="sex", data=ship)
#plt.show()

# step 5 plot basic graph with 2 variables/count plot
#p=sns.countplot(x="sex", data=ship, hue="class")
#plt.show()

# step 6 set title
#p=sns.countplot(x="sex", data=ship, hue="class")
#p.set_title("count plot for titanic")
#plt.show()






import seaborn as sns
import matplotlib.pyplot as plt
sns.set_theme(style="ticks", color_codes=True)
titanic=sns.load_dataset("titanic")
sns.catplot(x="sex", y="survived", hue="class", kind="bar", data=titanic)
plt.show()



#import seaborn as sns
#import matplotlib.pyplot as plt
#sns.set_theme(style="ticks", color_codes=True)
#titanic = sns.load_dataset("titanic")
#p1=sns.countplot(x='sex', data=titanic, hue='class')
#p1.set_title("plot for counting")
#plt.show()


#import seaborn as sns
#import matplotlib.pyplot as plt
#sns.set_theme(style="ticks", color_codes=True)
#titanic = sns.load_dataset("titanic")
#g=sns.FacetGrid(titanic, row='sex', hue='alone')
#g=(g.map(plt.scatter, 'age', 'fare').add_legend())
#plt.show()