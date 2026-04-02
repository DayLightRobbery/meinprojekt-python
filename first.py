name = input("Wie heißt Du ? ")
alter = int(input("Wie alt bist Du? "))

if alter < 18:
    print("Du bist noch minderjährig,",name)
else:
    print("Willkommen,",name, "- du bist volljährig")