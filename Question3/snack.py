# Simpan nama item dan harga setiap item dalam bentuk list
item_names = ["Popcorn", "Hotdog", "Nachos", "Soft Drink"]
item_prices = [8.50, 7.00, 6.50, 5.00]

# List kosong untuk simpan kuantiti yang user masukkan
quantities = []

# Ulang untuk setiap item dan minta kuantiti daripada user
# item_num baca berapa panjang list item_names
for item_num in range(len(item_names)):
    # Tunjuk nama serta harga item, minta kuantiti daripada pengguna dan tukar kepada nombor bulat
    # 2f untuk display number dua tempat perpuluhan
    qty = int(input(f"Enter the quantity for {item_names[item_num]} (RM{item_prices[item_num]:.2f}): "))
    # Simpan kuantiti dalam list
    quantities = quantities + [qty]

# Mula jumlah harga dengan 0
total_cost = 0
# Kira harga setiap item dan tambah kepada jumlah keseluruhan
for item_num in range(len(item_prices)):
    total_cost = total_cost + (quantities[item_num] * item_prices[item_num])

# Papar jumlah harga sebelum diskaun
print()
print("Total cost: RM ", round(total_cost, 2))

# Semak sama ada jumlah belian layak mendapat diskaun
# guna relational untuk buat jawapan true or false pakai greater than or equal to
if total_cost >= 50:
    # Kira diskaun 5% dan jumlah yang perlu dibayar
    discount = total_cost * 0.05
    final_amount = total_cost - discount
    print("Discount applied (5%): RM ", round(discount, 2))
    print("Final amount to pay: RM ", round(final_amount, 2))
else:
    # Jika kurang RM50, user bayar jumlah asal
    final_amount = total_cost
    print("Final amount to pay: RM ", round(final_amount, 2))