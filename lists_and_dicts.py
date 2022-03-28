def main():
    my_list = [1, 'Hello', True, 4.5]
    my_dict = {'firstname':'Javier', 'lastname':'González'}

    super_list = [ #lista de diccionarios
        {'firstname':'Javier', 'lastname':'González'},
        {'firstname':'Emanuel', 'lastname':'Andrade'},
        {'firstname':'Fernanda', 'lastname':'Romero'},
        {'firstname':'Maria', 'lastname':'Mejía'}
    ]

    super_dict = { #diccionario de listas
        'natural_nums' :[1,2,3,4,5],
        'integer_nums' :[-1,-2,0,1,2],
        'floating_nums':[1.1,4.5,6.3,4.2]
    }

    for key, value in super_dict.items():
        print(key,'-',value)
    
    for values in super_list:
        print(values.items())

        
if __name__ == '__main__':
    main()