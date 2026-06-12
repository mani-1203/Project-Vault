from abc import ABC,abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def perimeter(self):
        pass
class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return 3.1415*self.radius*self.radius
    def perimeter(self):
        return 2*3.1415*self.radius
# c=Circle(10)
# print(c.perimeter())

class PaymentGateway(ABC):
    @abstractmethod
    def authenticate(self,pin):
        pass
    @abstractmethod
    def pay(self,amount):
        pass
    @abstractmethod
    def refund(self):
        pass
class UPIPayment(PaymentGateway):
    def __init__(self,pin):
        self.pin=pin
    def authenticate(self):
        if self.pin=="120312":
            print("Correct pin")
        else:
            print("Invalid pin")
    def pay(self, amount):
        if self.pin=='120312':
            print(f"{amount} is deducted")

    def refund(self):
        if self.pin=='120312':
            print('amount is refunded')
u=UPIPayment("120312")
u.authenticate()
u.refund()
class MediaPlayer(ABC):

    @abstractmethod
    def load(self, filename):
        pass

    @abstractmethod
    def play(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class MP3Player(MediaPlayer):
    def load(self, filename):
        print(f"Loading MP3 file: {filename}")

    def play(self):
        print("Playing MP3 file...")

    def stop(self):
        print("Stopping MP3 playback.")

class WAVPlayer(MediaPlayer):
    def load(self, filename):
        print(f"Loading WAV file: {filename}")

    def play(self):
        print("Playing WAV file...")

    def stop(self):
        print("Stopping WAV playback.")

class AACPlayer(MediaPlayer):
    def load(self, filename):
        print(f"Loading AAC file: {filename}")

    def play(self):
        print("Playing AAC file...")

    def stop(self):
        print("Stopping AAC playback.")

# players=[MP3Player(), WAVPlayer(),AACPlayer()]
# for player in players:
#     player.load('movie')
#     player.play()
#     player.stop()

class RobotCommand(ABC):
    @abstractmethod
    def execute(self,moment):
        pass
    @abstractmethod
    def undo(self,moment):
        pass
class PickCommand(RobotCommand):
    def execute(self,moment):
        print(f'Robot executed this {moment} moment.')
    def undo(self,moment):
        print(f'Robot undone this {moment} moment.')
class PlaceCommand(RobotCommand):
    def execute(self,moment):
        print(f'Robot executed this {moment} moment.')
    def undo(self, moment):
        print(f'Robot undone this {moment} moment.')
class MoveCommand(RobotCommand):
    def execute(self, moment):
        print(f'Robot executed this {moment} moment.')
    def undo(self, moment):
        print(f'Robot undone this {moment} moment.')
# commands=[PickCommand(),PlaceCommand(),MoveCommand()]
# for i in commands:
#     i.execute('pick')
#     i.undo('pick')