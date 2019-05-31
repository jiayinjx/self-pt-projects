
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns
sns.set() 
from IPython.display import display


# In[2]:


train = pd.read_csv('titanic-train.csv')
test = pd.read_csv('titanic-test.csv')
titanic = pd.read_csv('titanic.csv')


# In[3]:


all_data = [titanic]


# In[4]:


for dataset in all_data:
    dataset.loc[ dataset['Age'] <= 12, 'Age'] = 0,
    dataset.loc[(dataset['Age'] > 12) & (dataset['Age'] <= 20), 'Age'] = 1,
    dataset.loc[ dataset['Age'] > 20, 'Age'] = 2


# In[5]:


sex_mapping = {"male": 0, "female": 1}
for dataset in all_data:
    dataset['Sex'] = dataset['Sex'].map(sex_mapping)


# In[6]:


for dataset in all_data:
    dataset.loc[ dataset['SiblingSpouse'] == 0, 'SiblingSpouse'] = 0,
    dataset.loc[ dataset['SiblingSpouse'] > 0, 'SiblingSpouse'] = 1,
    dataset.loc[ dataset['ParentChild'] == 0, 'ParentChild'] = 0,
    dataset.loc[ dataset['ParentChild'] > 0, 'ParentChild'] = 1,


# In[7]:


titanic.head(40)


# In[8]:


titanic.tail(23)


# In[9]:


from sklearn.tree import DecisionTreeClassifier # Import Decision Tree Classifier
from sklearn.model_selection import train_test_split # Import train_test_split function
from sklearn import metrics


# In[10]:


titanic.replace(np.NaN, 0)


# In[11]:


titanic = titanic.fillna(titanic.mean())


# In[12]:


target = titanic['Survived']
data = titanic.drop('Survived', axis=1)


# In[13]:


# Split dataset into training set and test set
X_train, X_test, y_train, y_test = train_test_split(data, target, test_size=40/63, random_state=1) # 70% training and 30% test


# In[14]:


# Create Decision Tree classifer object
clf = DecisionTreeClassifier()

# Train Decision Tree Classifer
clf = clf.fit(X_train,y_train)

#Predict the response for test dataset
y_pred = clf.predict(X_test)


# ### Evaluating Model

# After the prediction , we make a confusion matrix based on the prediction result and target.

# In[15]:


# making a confusion metrix
from sklearn.metrics import confusion_matrix
confusion_matrix = confusion_matrix(y_test, y_pred)
confusion_matrix


# The accuracy fo the decision tree model:

# In[16]:


print("Accuracy:",metrics.accuracy_score(y_test, y_pred))


# Now we got a classification rate of 72.5%. We can improve this accuracy by tuning the parameters in the Decision Tree Algorithm.

# ### Visualization

# In[17]:


from sklearn.tree import export_graphviz
from sklearn.externals.six import StringIO  
from IPython.display import Image  
import pydotplus


# In[18]:


dot_data = StringIO()
feature_cols = list(data.columns.values)
export_graphviz(clf, out_file=dot_data,  
                filled=True, rounded=True,
                special_characters=True,feature_names = feature_cols,class_names=['0','1'])
graph = pydotplus.graph_from_dot_data(dot_data.getvalue())  
graph.write_png('titanic_dt.png')
Image(graph.create_png())

