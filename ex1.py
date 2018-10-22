class Udacian:

    def __init__(self, name, city, enrollment, nanodegree, status):
        self.name = name
        self.city = city
        self.enrollment = enrollment
        self.nanodegree = nanodegree
        self.status = status

    def printUdacian(self):
        return("name:" + self.name + "\ncity: " + self.city + "\nenrollment: " + self.enrollment + "\nnanodegree: " + self.nanodegree + "\nstatus: " + self.status)

udacian = Udacian("Nouf", "Khobar", "yes", "Full Stack Developer", "active")
print(udacian.printUdacian())
