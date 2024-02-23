
from ..utils.util_class import distance_between_points
from access_layers.database_access import DataBaseAccessLayer
from access_layers.database_access import FileServerAccessLayer

class Triangle:
    def __init__(self, p1, p2, p3):
       self.p1 = p1
       self.p2 = p2
       self.p3 = p3  

    def show_points(self):
        print(self.p1)
        print(self.p2)
        print(self.p3)


    def area(self):
        base = distance_between_points(self.p1, self.p2)
        db = DataBaseAccessLayer(connection_str="mongo://connection_url")
        ftp = FileServerAccessLayer(ftp_url="ftp://ftp_url")
        print("Calculated the area of the triangle and store it in a database")