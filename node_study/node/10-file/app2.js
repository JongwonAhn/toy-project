const fs = require('fs').promises;

fs.readFile('./text.txt', 'utf-8')
 .then(data => console.log(data))
 .catch(console.error);

 fs.writeFile('./text.txt', 'hello hello')
  .catch(console.error());

  fs.appendFile('./text.txt', '123123 hello hello')
  .catch(console.error());