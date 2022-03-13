violator_songs = [
['World in My Eyes', 4.86],
['Sweetest Perfection', 4.43],
['Personal Jesus', 4.56],
['Halo', 4.9],
['Waiting for the Night', 6.07],
['Enjoy the Silence', 4.20],
['Policy of Truth', 4.76],
['Blue Dress', 4.29],
['Clean', 5.83]
]

names_songs = []
num_songs = int(input("Сколько песен выбрать? "))
for i in range(1, num_songs + 1):
    print("Название", i, "песни: ", end="")
    names_songs.append(input())

time = [song[1] for song in violator_songs if song[0] in names_songs]

print("Общее время звучания песен:", round(sum(time), 2), "минут")
