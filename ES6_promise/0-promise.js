export default function getResponseFromAPI() {
  return new Promise((resolve, reject) => {
    const True = 'funca';
    if (True) {
      resolve('Si funca');
    } else {
      reject(Error('No funca'));
    }
  });
}
