from rooms import room

room_object = room("toilet, it is dirty.")
living_room = room("living room, it is cozy.")

list_of_rooms = [toilet, living_room]

for each_index, each_room in enumerate(list_of_rooms):
    print(f'{each_index}: {each_room.display()}')