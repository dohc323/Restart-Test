from Classes import ICECar, ElecticCar, Car

def main ():
    my_ev = ElecticCar("Telsa", 250, 500)
    my_ev.drive(distance_km=100)

    my_ICECar = ICECar("Mazda",500, 50, 25)
    my_ICECar.drive(distance_km=2000)

    print(my_ev.__dict__)
    print(my_ev)
    print(my_ICECar.__dict__)
    print(my_ICECar)
    
if __name__ == "__main__":
    main()