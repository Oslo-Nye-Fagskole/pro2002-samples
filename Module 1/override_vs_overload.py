class Animal:
    def make_sound(self, times=1):   # overload-like: default parameter
        for _ in range(times):
            print(f"Some generic animal sound repeated {times} times")

a = Animal()
a.make_sound()       # single sound
a.make_sound(3)      # repeats 3 times