from djinnlist.models import Category
import csv

def run():
    try:
        with open('djinnlist/catlist.csv') as file:
            reader = csv.reader(file)
            reader.__next__() # header row

            Category.objects.all().delete()

            for row in reader:
                cat = Category(
                    game=row[0],
                    query=row[1],
                    label=row[2]
                )

                cat.save()
                print(cat)
    except(FileNotFoundError):
        print('Could not open the catlist.csv file in the djinnlist folder.')