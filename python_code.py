import pickle

# Open the file in binary read mode
with open('python_object_files/all.obj', 'rb') as f:
  # Deserialize the object and store it in a variable
  my_object = pickle.load(f)
  highest = 0
  index = 0
  for i in range(len(my_object)):
      if(highest < my_object[i][1]):
          print(i)
          idnex = i
          highest = my_object[i][1]
      #print(my_object[i])
  print(my_object[index])