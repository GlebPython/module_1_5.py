immutable_tuple=(1,2,3,'Кортеж',True,)
print(immutable_tuple)
#immutable_tuple[0]=2--Выдаёт ошыбку потому, что 'immutable_tuple' это кортеж - неизменяемая упорядоченная коллекция,
# которая может содержать в себе разные типы данных, в том числе и изменяемые такие, как списки.
mutable_list=[1,2,3,'Список',True]
print(mutable_list)
mutable_list[0]=3
mutable_list[2]=1
mutable_list[3]='List'
print(mutable_list)