import signUpUser from './4-user-promise';
import uploadPhoto from './5-photo-reject';

export default function handleProfileSignup(firstName, lastName, fileName) {
  return Promise.all([
    signUpUser(firstName, lastName)
      .then((dataprom) => ({ status: 'fulfilled', value: dataprom }))
      .catch((errordata) => ({ status: 'rejected', value: Error('${fileName} cannot be processed')})),
    uploadPhoto(fileName)
      .then((dataprom) => ({ status: 'fulfilled', value: dataprom }))
      .catch((errordata) => ({ status: 'rejected', value: Error('${fileName} cannot be processed')})),
  ]).then((response) => response);
}
