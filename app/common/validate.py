# funtion for validate if exist data in the database
def validateExist(reference,data,dataCompare):
    database = reference.get()
    if(database):
      for key, value in database.items():
        if(value[f"{dataCompare}"] == data[f"{dataCompare}"]):
          return True

    return False