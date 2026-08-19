# Sediakan list untuk simpan semua nombor
numbers = []
# Sediakan list untuk nombor genap dan ganjil
even_list = []
odd_list = []

# Minta nombor daripada user
# build in function int() akan tukar value yang dimassukkan oleh user kepada bentuk integer
# value yang diterima assign to value_number
# value_number ialah variable name yang simpan value yang diterima di ruang memory
value_number = int(input("Enter an integer (enter 0 to stop): "))

# Ulang input sehingga user masukkan 0
#kalau user massukan value selain daripada 0 
while value_number != 0:
    # Simpan nombor yang dimasukkan
    # Python akan tukar nilai 'value_number' menjadi bentuk list [] dan menggabungkannya ke dalam list 'numbers'
    numbers = numbers + [value_number]
    value_number = int(input("Enter an integer (enter 0 to stop): "))

# Periksa setiap nombor dan asingkan genap atau ganjil
for num_val in numbers:
    #guna modulus sebab nak cari baki
    if num_val % 2 == 0:
        # Baki 0 bermaksud nombor genap
        even_list = even_list + [num_val]
    else:
        # Selain baki 0 bermaksud nombor ganjil
        odd_list = odd_list + [num_val]

# Papar senarai dan jumlah nombor
print("Even numbers:", even_list)
print("Odd numbers:", odd_list)
print("Total even numbers:", len(even_list))
print("Total odd numbers:", len(odd_list))