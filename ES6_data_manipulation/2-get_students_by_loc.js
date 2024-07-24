export default function getStudentsByLocation(array, city) {
  let idArray = [];
  if (Array.isArray(array)) {
    idArray = array.filter((student) => student.location === city);
    return idArray;
  }
  return idArray;
}
