import pandas as pd 
import itertools 
import collections
from operator import itemgetter

data = pd.read_csv('faculty.csv', skipinitialspace =True)

#Create a dictionary in the below format:
# faculty_dict = { 'Ellenberg': [\
#               ['Ph.D.', 'Professor', 'sellenbe@upenn.edu'],\
#               ['Ph.D.', 'Professor', 'jellenbe@mail.med.upenn.edu']
#                             ],
#               'Li': [\
#               ['Ph.D.', 'Assistant Professor', 'liy3@email.chop.edu'],\
#               ['Ph.D.', 'Associate Professor', 'mingyao@mail.med.upenn.edu'],\
#               ['Ph.D.', 'Professor', 'hongzhe@upenn.edu']
#                             ]
#             }

last_names = data['name'].map(lambda x: x.rsplit(' ')[-1]).tolist()
first_names = data['name'].map(lambda x: x.rsplit(' ')[0]).tolist()
titles =data['title'].map(lambda y: y.rsplit(' ',2)[0]).tolist()
degrees = data['degree'].tolist()
emails =data['email'].tolist()

def createdict(dataframe):
  faculty_dict = {}

  for i in range(len(last_names)):
    faculty_dict[last_names[i]] = faculty_dict.get(last_names[i], []) + [[degrees[i], titles[i], emails[i]]]
  #print(faculty_dict)

  #sort faculty_dict into a list
  faculty_list = sorted(faculty_dict.items(), key=itemgetter(0))

  #print the first three key value pairs
  print(faculty_list[0:3])



def createnewdict(dataframe):
# professor_dict = {('Susan', 'Ellenberg'): ['Ph.D.', 'Professor', 'sellenbe@upenn.edu'],\
#                 ('Jonas', 'Ellenberg'): ['Ph.D.', 'Professor', 'jellenbe@mail.med.upenn.edu'],\
#                 ('Yimei', 'Li'): ['Ph.D.', 'Assistant Professor', 'liy3@email.chop.edu'],\
#                 ('Mingyao','Li'): ['Ph.D.', 'Associate Professor', 'mingyao@mail.med.upenn.edu'],\
#                 ('Hongzhe','Li'): ['Ph.D.', 'Professor', 'hongzhe@upenn.edu']
#             }
  professor_dict = {}
  for i in range(len(first_names)):
    professor_dict[(first_names[i],last_names[i])] = professor_dict.get((first_names[i],last_names[i]),[]) + [degrees[i], titles[i], emails[i]]
  
  #print first three key value pairs of professor_dict sorted by first name
  y = list(itertools.islice(sorted(professor_dict.items()), 0, 3))
  print(y)

  #print the first three sorted by last name
  ordered = collections.OrderedDict(sorted(professor_dict.items(), key =lambda x: x[0][1]))
  professor_list = list(ordered.items())
  print(professor_list[:3])

createdict(data)
createnewdict(data)
