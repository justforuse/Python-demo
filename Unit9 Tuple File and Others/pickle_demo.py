D = {'name':'Allen', 'age':21}
f = open('p_data.pkl','wb')
import pickle
pickle.dump(D,f)
f.close()

f=open('p_data.pkl','rb')
e=pickle.load(f)
print(e)
print(type(e))
