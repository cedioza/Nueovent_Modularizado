def validateExist(reference,data,dataCompare):
    database = reference.get()
    if(database):
      for key, value in database.items():
        if(value[f"{dataCompare}"] == data[f"{dataCompare}"]):
          return True

    return False

# def validarExisteAlojamiento(reference,data):
#     database = reference.get()
#     if(database):
#       for key, value in database.items():
#         if(value["nit"] == data["nit"]):
#           return True

# def validarExisteEvento(reference,data):
#     database = reference.get()
#     if(database):
#       for key, value in database.items():
#         if(value["cliente"] == data["cliente"]):
#           return True
#         else:
#           return False
#     else:
#       return False