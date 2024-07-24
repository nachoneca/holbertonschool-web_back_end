export default function getListStudentIds(array) {
  let idArray = [];
  if (Array.isArray(array)) {
    idArray = array.map((student) => student.id);
    return idArray;
  }
  return idArray;
}
