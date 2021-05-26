class BaseClass:
    number_base_calls = 0

    def call_me(self):
        print("Calling method on Base Class")
        self.number_base_calls += 1


class LeftSubclass(BaseClass):
    number_left_calls = 0

    def call_me(self):
        super().call_me()
        print("Calling method on Left Subclass")
        self.number_left_calls += 1


class RightSubclass(BaseClass):
    number_right_calls = 0

    def call_me(self):
        super().call_me()
        print("Calling method on Right Subclass")
        self.number_right_calls += 1


class Subclass(LeftSubclass, RightSubclass):
    number_sub_calls = 0

    def call_me(self):
        super().call_me()
        print("Calling method on SUbclass")
        self.number_sub_calls += 1


if __name__ == '__main__':
    s = Subclass()
    s.call_me()
