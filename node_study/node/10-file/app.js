const fs = require('fs');

// try{
//  fs.renameSync('./text.txt', './file-txt');
// }catch(e){
//  console.error(e);
// }
// console.log('helloo');

// fs.rename('./file-txt', './file.txt', (error) =>{
//     console.log(error);

// });
console.log("123");

fs.promises
  .rename('./file.txt', './text.txt')
  .then(() => console.log('done!'))
  .catch(console.error);