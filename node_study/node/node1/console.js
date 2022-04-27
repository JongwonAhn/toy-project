console.log('logging..');

const student = {name : 'jongwon', age: 20};

console.table(student);

console.time('for loop');
for (let i = 0; i < 10; i++){
    i++;
};
console.timeEnd('for loop');