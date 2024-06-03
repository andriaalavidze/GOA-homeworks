def Abbreviation_of_name(fullname):
    splited_fullname = fullname.split(" ")

    firstname = splited_fullname[0]
    lastname = splited_fullname[1]
    
    result = firstname[0] + "." + lastname[0]
    print(result)
   
Abbreviation_of_name("Andria Alavidze")