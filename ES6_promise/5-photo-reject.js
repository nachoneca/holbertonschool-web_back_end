export default function uploadPhoto(fileName) {
  return new Promise((resolve, reject) => {
    reject(Error('${fileName} cannot be processed'));
  });
}
