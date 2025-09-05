class Animal:
    # Here we deliberately use a silly name instead of "self"
    def __init__(jigglypuffmarshmallow, habitat):
        # It still works, as long as we stay consistent
        jigglypuffmarshmallow.habitat = habitat

    def make_sound(jigglypuffmarshmallow):
        # The method still receives the instance as the first argument
        print("Some generic animal sound")

a = Animal("Savannah")
a.make_sound()  # Works fine, even though "self" wasn't used