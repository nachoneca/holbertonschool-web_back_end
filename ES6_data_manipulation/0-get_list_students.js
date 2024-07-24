export default function getListStudents() {
  function Object(id, firstName, location) {
    this.id = id;
    this.firstName = firstName;
    this.location = location;
  }
  const students = [];
  const Guillaume = new Object(1, 'Guillaume', 'San Francisco');
  const Jamese = new Object(2, 'James', 'Columbia');
  const Serena = new Object(5, 'Serena', 'San Francisco');
  students.push(Guillaume, Jamese, Serena);

  return students;
}
