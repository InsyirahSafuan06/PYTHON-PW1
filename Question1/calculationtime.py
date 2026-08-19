# user masukkan jumlah saat 
# build in function int() akan tukar value yang dimassukkan oleh user kepada bentuk integer
# value yang diterima assign to total_second
# total_second ialah variable name yang simpan value yang diterima di ruang memory
total_seconds = int(input("Enter the total number of seconds: "))

# Tukar jumlah saat kepada jam, minit, dan saat
# 1 minit = 60 saat
# 1 jam = 60 minit
# dapat 3600 kerana 60 minit darab 60 saat
hours = total_seconds // 3600
minutes = (total_seconds % 3600) // 60
seconds = total_seconds % 60

# Papar masa yang telah ditukar
print(total_seconds,  "seconds is equivalent to" , hours , "hours" , minutes , "minutes, and ", seconds)