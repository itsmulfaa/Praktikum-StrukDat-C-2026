tim_frontend = {"HTML", "CSS", "JavaScript", "React"}
tim_backend = {"Python","JavaScript", "SQL", "NodeJS"}

#keahlian yang dimiliki kedua tim (irisan)
irisan = tim_frontend & tim_backend
print("Keahlian yang dimiliki keduat tim :",irisan)

#keahlian yang hanya dimiliki tim_backend
hanya_backend = tim_backend - tim_frontend
print("Keahlian yang hanya dimiliki tim_backend :", hanya_backend)

#keahlian yang hanya dimiliki tim_frontend
hanya_frontend = tim_frontend - tim_backend
print("Keahlian yang hanya dimiliki tim_frontend", hanya_frontend)

#gabungan seluruh keahlian
gabungan = tim_frontend | tim_backend
print("Total kealian unik: ", gabungan)

