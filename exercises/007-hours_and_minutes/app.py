#Complete the function to calculate how many hours and minutes are passed since midnight.
def hours_minutes(secs):
  #minutes = secs // 60
  #hours = minutes // 60
  #minutes = minutes % 60 
  #return (hours, minutes)
  
  return secs//3600, (secs//60)%60 
#secs//60 son los minutos, los minutos % 60 son los minutos que sobran más allá de la hora
#secs//3600 son las horas
#Invoke the funtion and pass any interger as its argument.
print(hours_minutes(3900))