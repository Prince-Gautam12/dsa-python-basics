package pybasics.oops;

/**
 * OOPS
 */
public class OOPS {
    public static void main(String[] args) {
        Person person = new Person("Puttar", 1);
        person.print();
        Student student = new Student("Prince", 22, 1);
        student.print();

        Person random = new Student("Akshay", 29, 34);

        random.print();
    }


}

class Person {
    private String name;
    private Integer age;  
    public Person(String name, Integer age) {
        this.age = age;
        this.name = name;
    }
    
    public String getName() {
        return this.name;
    }

    public Integer getAge() {
        return this.age;
    }

    public void print() {
        System.out.println("Name: "+this.name + ", age: "+ this.age);
    }
}

class Student extends Person{
    private Integer studentId;
    public Student(String name, Integer age, Integer studentId){
        super(name, age);
        this.studentId = studentId;
    }
    public void print() {
        super.print();
        System.out.println("Above details for student id: "+ this.studentId);
    }
}
