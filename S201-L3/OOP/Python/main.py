from person import Person
from student import Student
from teacher import Teacher

pessoa1 = Person("Larry", 25)
estudante1 = Student("Darry", 15)
professor1 = Teacher("Merry", 54)

pessoa1.print_nome()
pessoa1.getIdade()

estudante1.print_nome()
estudante1.getIdade()

professor1.print_nome()
professor1.getIdade()