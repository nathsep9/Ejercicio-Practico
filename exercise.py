# El siguente ejercicio se realizo mediante en visual studio code y con la version de python 3.9.5,
# el cual se realizo con el fin de poder realizar un programa que permita realizar una campaña de vacunacion
# para personas que pertenecen a un rango de edad y estrato, el cual inmplementa la herencia y polimorfismo


# para poder realizar la solucion del problema.

# Se crea la clase persona con sus atributos y metodos
# La clase "Person" es la clase base que representa a una persona y contiene los atributos "nombre", "edad", "sexo" y "estrato".


class Person:
    def __init__(self, name, age, sex, stratum):
        self.name = name
        self.age = age
        self.sex = sex
        self.stratum = stratum

    def __str__(self):
        return f"{self.name}, {self.age}, {self.sex}, {self.stratum}"

# Se crea la clase Beneficiario que hereda de la clase Persona
# La clase "Beneficiary" es la clase derivada que representa a un beneficiario de la campaña de vacunación y contiene los atributos "nombre", "edad", "sexo" y "estrato".
# Agrega un método adicional "is_beneficiary" que determina si una persona es elegible para ser beneficiaria como beneficiaria dependiendo de su género y edad, y su estrato social.


class Beneficiary(Person):
    def __init__(self, name, age, sex, stratum):
        super().__init__(name, age, sex, stratum)

    def __str__(self):
        return f"{self.name} {self.age} {self.sex} {self.stratum}"

    def is_beneficiary(self):
        if self.sex == "M" and self.age <= 35 and self.stratum <= 2:
            return True
        elif self.sex == "F" and self.age <= 30 and self.stratum <= 2:
            return True
        else:
            return False

# La clase "Campaign" representa una campaña de vacunación y contiene una lista de beneficiarios.
# Agrega un método adicional "add_beneficiary" que agrega un beneficiario a la lista de beneficiarios.
# Agrega un método adicional "amount_beneficiary" que determina la cantidad de beneficiarios.
# Agrega un método adicional "average_age_beneficiaries" que determina el promedio de edad de los beneficiarios.
# Agrega un método adicional "amount_beneficiaries_for_sex" que determina la cantidad de beneficiarios por sexo.


class Campaign:
    def __init__(self):
        self.beneficiaries = []

    def add_beneficiary(self, beneficiary):
        self.beneficiaries.append(beneficiary)

    def amount_beneficiary(self):
        amount_beneficiaries = 0
        for beneficiary in self.beneficiaries:
            if beneficiary.is_beneficiary():
                amount_beneficiaries += 1
        return amount_beneficiaries

    def average_age_beneficiaries(self):
        addition_age = 0
        amount_beneficiaries = 0
        for beneficiary in self.beneficiaries:
            if beneficiary.is_beneficiary():
                addition_age += beneficiary.age
                amount_beneficiaries += 1
        return addition_age / amount_beneficiaries

    def amount_beneficiaries_for_sex(self, sex):
        amount_beneficiary = 0
        for beneficiary in self.beneficiaries:
            if beneficiary.is_beneficiary() and beneficiary.sex == sex:
                amount_beneficiary += 1
        return amount_beneficiary

    def average_age_beneficiaries_for_sex(self, sex):
        addition_ages = 0
        amount_beneficiaries = 0
        for beneficiary in self.beneficiaries:
            if beneficiary.is_beneficiary() and beneficiary.sex == sex:
                addition_ages += beneficiary.age
                amount_beneficiaries += 1
        return addition_ages / amount_beneficiaries

# La clase "Campaña" es el núcleo del programa y mantiene una lista de beneficritos. La clase tiene varios métodos para calcular estadísticas sobre la lista de descritos, como la cantidad de descritos, el promedio de edad de los descritos, la cantidad y el promedio de edad de los descritos por género.

    def __str__(self):
        texts = []
        texts.append(
            f"Cantidad de beneficiarios: {self.amount_beneficiary()}"
        )
        texts.append(
            f"Promedio de edad de beneficiarios: {self.average_age_beneficiaries()}"
        )
        texts.append(
            f"Cantidad de beneficiarios hombres: {self.amount_beneficiaries_for_sex('M')}"
        )
        texts.append(
            f"Promedio de edad de beneficiarios hombres: {self.average_age_beneficiaries_for_sex('M')}"
        )
        texts.append(
            f"Cantidad de beneficiarios mujeres: {self.amount_beneficiaries_for_sex('F')}"
        )
        texts.append(
            f"Promedio de edad de beneficiarios mujeres: {self.average_age_beneficiaries_for_sex('F')}")
        return "\n".join(texts)

# En la función "main", se crea una campaña y se agrega una lista de descritos. Luego, se imprime el objeto de la campaña para ver los resultados de las estadísticas.


def main():
    campaign = Campaign()
    campaign.add_beneficiary(Beneficiary("Juan", 30, "M", 1))
    campaign.add_beneficiary(Beneficiary("Pedro", 35, "M", 1))
    campaign.add_beneficiary(Beneficiary("Maria", 30, "F", 1))
    campaign.add_beneficiary(Beneficiary("Ana", 35, "F", 1))
    campaign.add_beneficiary(Beneficiary("Luis", 30, "M", 2))
    campaign.add_beneficiary(Beneficiary("Carlos", 35, "M", 2))
    campaign.add_beneficiary(Beneficiary("Julia", 30, "F", 2))
    campaign.add_beneficiary(Beneficiary("Laura", 35, "F", 2))
    campaign.add_beneficiary(Beneficiary("Carlos", 30, "M", 3))
    campaign.add_beneficiary(Beneficiary("Luisa", 35, "F", 3))
    print(campaign)


if __name__ == "__main__":
    main()
