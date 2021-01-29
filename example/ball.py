class Ball:
    def __init__(self, color:str, size:float, weight: float, ball_type:str) -> None:
        self.color = color
        self.size = size
        self.weight = weight
        self.ball_type = ball_type

    def bounce(self):
        if self.ball_type.lower() == 'bowling':
            print("Bowloing balls can't bounce!")
        else:
            print(f"The {self.ball_type} ball is bouncing!")