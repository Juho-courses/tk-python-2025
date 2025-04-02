from dataclasses import dataclass


@dataclass
class Fruit:
    id: int
    name: str
    count: int

    # def __init__(self, id, name, count) -> None:
    #     self.id = id
    #     self.name = name
    #     self.count = count

    @staticmethod
    def parse(line: str):
        # 5,asd,123
        splitted = line.split(",")
        fruit_id = int(splitted[0])
        name = splitted[1]
        count = int(splitted[2])
        return Fruit(fruit_id, name, count)

    def __str__(self) -> str:
        return f"Fruit id: {self.id}, name: {self.name}, count: {self.count}"


fruits = {}

try:
    with open("data.csv", "r") as f:
        first_row_skipped = False
        for line in f:
            if not first_row_skipped:
                first_row_skipped = True
                continue
            line = line.strip()
            # print(line)
            fruit = Fruit.parse(line)

            if fruit.count == 0:
                raise Exception("Count oli nolla!")
            # print(fruit)
            fruits[fruit.name] = fruit.count

except FileNotFoundError as ex:
    print(f"Tiedostoa ei löytynyt: {ex.filename}")
except Exception as ex:
    # parempi ottaa kiinni tiettyjä poikkeuksia
    # eikä kaikkia mahdollisia kerralla
    print(ex)

print(fruits)

