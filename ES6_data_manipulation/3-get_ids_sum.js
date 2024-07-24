export default function getStudentsByLocation(array) {
  let idArray = [];
  if (Array.isArray(array)) {
    idArray = array.reduce((res, student) => res + student.id, 0);
    return idArray;
  }
  return idArray;
}
