import csv

def read_csv_file(file):

     file_records = []
     citac = csv.DictReader(open(file,'r'))
     
     for red in citac:
         file_records.append(dict(red))
         
     return file_records
     
print("file_records = " + str(read_csv_file("CSV.csv"))) 
