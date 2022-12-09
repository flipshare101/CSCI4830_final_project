import pickle

# Open the file in binary read mode
with open('python_object_files/all.obj', 'rb') as f:
  # Deserialize the object and store it in a variable
  my_object = pickle.load(f)
