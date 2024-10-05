immutable_var=1,2,3,'a','b'
#immutable_var[2]=7  нельзя изменять элементы кортежа
print(immutable_var)
print(type(immutable_var))
#immutable_var[2]=apple
print(immutable_var)
mutable_list=[1,2,3,'a','b','banan']
mutable_list[5]="modified"
print(mutable_list)
#mutable_list=[1,2,3,'a','b','modified']
#print(mutable_list)